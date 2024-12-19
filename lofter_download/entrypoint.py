import datetime
import hashlib
import json
import logging
import os
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
import lmdb

import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from tenacity import stop_after_attempt, wait_fixed, retry

from get_author import get_author
from get_like import get_all_like
from get_tag import get_all_tag
from util import parse_url

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)

if not os.path.exists("/download/img"):
    os.mkdir("/download/img")

env = lmdb.open('/download/posts.db', map_size=1099511627776)

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def wechat_push(msg):
    logging.info("推送消息: " + msg)
    logging.debug(requests.post("https://server.lyc8503.site/wepush", json={
        "key": "wepushkey",
        "msg": "[Lofter 爬虫]" + msg
    }, timeout=5).text)


pic_counter = 0
success_counter = 0
skip_counter = 0


def download_and_save(pic_url):
    global pic_counter, success_counter, skip_counter

    if pic_counter > 150000:
        logging.warning("图片数量过多, 跳过")
        skip_counter += 1
        return

    md5 = hashlib.md5()
    md5.update(pic_url.encode("utf-8"))
    prefix = md5.hexdigest()[:2]

    if not os.path.exists(f"/download/img/{prefix}/" + pic_url.replace("/", "@").replace(":", "@")):
        logging.info("下载保存: " + pic_url)
        pic_counter += 1
        r = requests.get(pic_url, timeout=5)

        if not r:
            logging.warning("下载失败: " + pic_url)
            return

        # logging.info("上传: " + pic_url)
        # # 上传
        # r = requests.post(os.environ['UPLOAD_URL'] + "/" + md5.hexdigest() + suffix, files={
        #     "file": r.content
        # }, timeout=30)

        # if not r:
        #     logging.warning("上传失败: " + r.text)
        #     return

        try:
            if not os.path.exists("/download/img/" + prefix):
                os.mkdir("/download/img/" + prefix)
            
            # use first 240 bytes as filename
            with open(f"/download/img/{prefix}/" + pic_url.replace("/", "_").replace(":", "_")[:240], "wb") as f:
                # f.write(pic_url.encode("utf-8"))
                # f.write(b'\n')
                f.write(r.content)

            logging.info("保存成功: " + pic_url)
            success_counter += 1
        except Exception as e:
            logging.error(e)
    else:
        logging.info("文件存在: " + pic_url)


def timer_task():
    try:
        liked_posts = {}
        posts = {}
        tags = set()
        authors = set()

        stat_like = set()
        stat_author = {}
        stat_tag = {}

        # 获取所有的原始喜欢列表
        for i in get_all_like(os.environ['LOFTER_ID']):
            try:
                author, post_id = parse_url(i["url"])

                stat_like.add(post_id)

                authors.add(author)
                for j in i["tags"]:
                    tags.add(j)

                posts[post_id] = i
                liked_posts[post_id] = i
            except Exception as e:
                logging.warning("Error", exc_info=e)

        wechat_push(f"获取喜欢列表完成, 发现 Tag: {len(tags)}, 作者: {len(authors)}")

        # 获取所有 tag
        for tag in tags:
            try:
                for post in get_all_tag(tag):
                    author, post_id = parse_url(post['url'])

                    stat_tag[tag] = stat_tag.get(tag, set()) | {post_id}
                    posts[post_id] = post
            except Exception as e:
                logging.error("Error", exc_info=e)
                wechat_push(f"获取 TAG {tag} 出现错误, 程序继续.")

        # 获取所有作者
        for author in authors:
            try:
                for post in get_author(author):
                    author, post_id = parse_url(post['blogPageUrl'])

                    stat_author[author] = stat_author.get(author, set()) | {post_id}
                    posts[post_id] = post
            except Exception as e:
                logging.error("Error", exc_info=e)
                wechat_push(f"获取作者 {author} 出现错误, 程序继续.")

        count = 0
        wechat_push(f"获取所有内容完成, 文章共计: {len(posts)}")

        with env.begin(write=True) as db:
            for k, v in posts.items():
                if db.get(k.encode("utf-8")):
                    continue

                db.put(k.encode("utf-8"), json.dumps(v, ensure_ascii=False).encode("utf-8"))
                count += 1

            date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
            db.put(b"stat_like_" + date.encode('utf-8'), json.dumps(stat_like, ensure_ascii=False, cls=SetEncoder).encode("utf-8"))
            db.put(b"stat_author_" + date.encode('utf-8'), json.dumps(stat_author, ensure_ascii=False, cls=SetEncoder).encode("utf-8"))
            db.put(b"stat_tag_" + date.encode('utf-8'), json.dumps(stat_tag, ensure_ascii=False, cls=SetEncoder).encode("utf-8"))

        wechat_push(f"内容保存完成, 新增: {count}, 下载图片中...")

        imgs = []
        for i in liked_posts:
            try:
                imgs += posts[i].get('img', [])
                if 'photoLinks' in posts[i]:
                    imgs += map(lambda x: x['middle'], json.loads(posts[i]['photoLinks']))
            except Exception as e:
                logging.warning("图片解析失败.", exc_info=e)
        imgs = set(imgs)

        wechat_push(f"图片共计: {len(imgs)}")

        global pic_counter, success_counter, skip_counter
        pic_counter = 0
        success_counter = 0
        skip_counter = 0

        limit = 20
        futures = set()

        with ThreadPoolExecutor(max_workers=8) as executor:
            for url in imgs:
                if len(futures) >= limit:
                    completed, futures = wait(futures, return_when=FIRST_COMPLETED)
                futures.add(executor.submit(download_and_save, url))

        wechat_push(f"图片下载完成! 本次下载图片数量: {pic_counter}, 成功数量: {success_counter}, 跳过数量: {skip_counter}. 本次运行结束.")
    except Exception as e:
        wechat_push("获取过程中发生未知错误, 程序中止: " + str(e))
        logging.error("未知错误", exc_info=e)


timer_task()
# 定时任务
scheduler = BlockingScheduler()
scheduler.add_job(timer_task, 'cron', hour=os.environ['RUN_HOUR'], max_instances=1)
scheduler.start()
