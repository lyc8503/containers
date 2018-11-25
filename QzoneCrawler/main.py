import difflib
import hashlib
import os
import random
import re
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from urllib.parse import quote

import requests
import json
import logging

from tenacity import stop_after_attempt, wait_fixed, retry
import time
from apscheduler.schedulers.blocking import BlockingScheduler

from fetch import get_friends, get_uin_info, get_shuoshuo_all, get_detail, UA
from login import password_login, qr_login
from util import wechat_push

login_uin = ""

if os.environ.get("DEBUG"):
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.DEBUG)
else:
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.INFO)

# 储存位置
os.chdir("/download")


def try_login_and_get():
    global login_uin

    cookie = ""

    try:
        login_uin = os.environ['QQ_ACCOUNT']
        passwd = os.environ['QQ_PASSWORD']
        cookie = password_login(login_uin, passwd)
    except Exception as e:
        logging.error("账号密码登录出错: ", e)
        wechat_push("账号密码登录时出错: " + str(e))
        wechat_push("尝试使用二维码登录...")
        try:
            cookie = qr_login()
        except Exception as e:
            logging.exception(e)
            wechat_push("二维码登录出错: " + str(e))

    counter = 0

    try:
        friends_list = get_friends(login_uin, cookie)
        logging.info("好友列表: " + str(friends_list))

        for friend_uin in friends_list:
            try:
                # 新建文件夹储存
                try:
                    os.mkdir(str(friend_uin))
                except:
                    pass

                # 获取用户信息
                try:
                    uin_info = get_uin_info(friend_uin, cookie)
                    logging.info(str(friend_uin) + " - " + friends_list[friend_uin] + " - " + str(uin_info))
                except Exception as e:
                    logging.info(str(friend_uin) + " - " + friends_list[friend_uin] + " - " + "对方未开通空间或没有访问权限.")
                    continue

                # 写入用户信息
                with open(str(friend_uin) + os.sep + "info.json", "w", encoding="utf-8") as f:
                    f.write(json.dumps(uin_info))

                # 获取所有说说列表
                all_ss = get_shuoshuo_all(friend_uin, cookie)
                logging.info("未获取到的说说数量: " + str(uin_info['SS'] - len(all_ss)))

                # 获取说说详细信息
                for i in all_ss:
                    logging.info("获取: " + i)
                    try:
                        ret = None

                        # 30 天
                        check_time = round(time.time()) - 30 * 24 * 3600

                        # 如果内容有变化则记录
                        if os.path.exists(str(friend_uin) + os.sep + i + ".json"):
                            old_json = json.load(open(str(friend_uin) + os.sep + i + ".json", "r", encoding="utf-8"))
                            
                            if 'created_time' not in old_json or old_json['created_time'] > check_time:

                                ret = get_detail(friend_uin, i, cookie)
                                time.sleep(random.random() * 5 + 2)
                                
                                ratio = difflib.SequenceMatcher(None, json.dumps(old_json), json.dumps(ret)).quick_ratio()
                                
                                if ratio > 0.99:
                                    logging.info("内容没有变化, 相似度: " + str(ratio))
                                    continue
                                else:
                                    logging.info("内容发生更新, 相似度: " + str(ratio))
                                    os.rename(str(friend_uin) + os.sep + i + ".json",
                                              str(friend_uin) + os.sep + i + "_old" + str(round(time.time())) + ".json")
                            else:
                                logging.info("跳过内容检查.")
                                continue
                        else:
                            ret = get_detail(friend_uin, i, cookie)
                            logging.info("第一次写入.")

                        counter += 1
                        with open(str(friend_uin) + os.sep + i + ".json", "w", encoding="utf-8") as f:
                            f.write(json.dumps(ret))

                    except Exception as e:
                        logging.error(e)
            except Exception as e:
                logging.error(e)
                logging.warning("获取 " + str(friend_uin) + " 的空间时发生错误, 程序继续.")
                wechat_push("获取 " + str(friend_uin) + " 的空间时发生错误, 程序继续.")

        logging.info("完成!")
        wechat_push("抓取成功, 新增/更新条数: " + str(counter))
    except Exception as e:
        logging.error(e)
        wechat_push("程序运行发生错误: " + str(e))
        return

    try:
        # 获取图片
        try:
            os.mkdir("pic")
        except:
            pass

        urls = set()

        logging.info("搜索 URL 中...")

        for path, dir_list, file_list in os.walk("."):
            for file_name in file_list:
                f = os.path.join(path, file_name)
                if f.endswith(".json"):
                    with open(f, "r", encoding="utf-8") as f_:
                        content = f_.read()

                    pattern = re.compile(
                        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
                    for i in pattern.findall(content):
                        urls.add(i)
                        # print(i)

        @retry(stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=True)
        def download_and_save(pic_url):

            if "://user.qzone.qq.com" in pic_url:
                return

            md5hash = hashlib.md5(pic_url.encode("utf-8"))
            md5 = md5hash.hexdigest()
            save_name = quote(pic_url, 'utf-8')[:80] + "_" + md5

            if not os.path.exists("pic" + os.sep + save_name):
                logging.info("下载保存: " + pic_url)
                r = requests.get(pic_url, headers={
                    "User-Agent": UA,
                    "Referer": "https://user.qzone.qq.com/"
                }, timeout=5)

                if r:
                    try:
                        with open("pic" + os.sep + save_name, "wb") as f2:
                            f2.write(r.content)
                    except Exception as e2:
                        logging.error(e2)
                else:
                    logging.warning("下载失败: " + pic_url)
                    try:
                        with open("pic" + os.sep + save_name, "w") as f2:
                            f2.write(str(r.status_code))
                    except Exception as e2:
                        logging.error(e2)
            else:
                logging.info("文件存在: " + pic_url)

        # for i in urls:
        #     print(i)

        executor = ThreadPoolExecutor(max_workers=20)
        all_tasks = [executor.submit(download_and_save, url) for url in urls]
        wait(all_tasks, return_when=ALL_COMPLETED)
        logging.info("图片下载完成.")
        wechat_push("图片下载完成.")
    except Exception as e:
        logging.error(e)
        wechat_push("图片下载失败: " + str(e))


try_login_and_get()

# 设置定时任务
if __name__ == "__main__":
    logging.info("设置定时任务...")
    scheduler = BlockingScheduler()
    scheduler.add_job(try_login_and_get, 'cron', hour=os.environ['RUN_HOUR'])

    logging.info("已启动.")
    scheduler.start()
