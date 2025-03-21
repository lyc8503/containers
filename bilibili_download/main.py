import json
import re
import time
import os
import logging
from urllib.parse import quote

from apscheduler.schedulers.blocking import BlockingScheduler

from tenacity import retry, wait_fixed, stop_after_attempt, retry_if_not_exception_type
import requests
from pySmartDL import SmartDL

import lmdb

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 ' \
             'Safari/537.36 '
user_cookie = None
env = None
TIMEOUT = 20 * 60  # 20分钟

# 输出位置
os.chdir("/download")


@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def wechat_push(msg):
    logging.debug(requests.post("https://server.lyc8503.site/wepush", json={
        "key": "wepushkey",
        "msg": "[Bilibili历史记录下载]" + msg
    }, timeout=5).text)


# 检查文件名
def validate_title(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |' 非法文件名
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    new_title = new_title.strip()  # 开头的空格可能导致文件保存有问题
    new_title = new_title.strip(".")  # 结尾的 . 可能导致文件保存有问题
    if len(new_title) > 64:
        new_title = new_title[:64]
    return new_title


def get_reason(bvid):
    reason = None
    referer = "https://www.bilibili.com/video/" + bvid
    
    coin_status = requests.get('https://api.bilibili.com/x/web-interface/archive/coins', params={
        "bvid": bvid
    }, headers={
        "Referer": referer,
        "User-Agent": USER_AGENT
    }, cookies=user_cookie).json()

    if coin_status['data']['multiply'] > 0:
        reason = "投币"

    if not reason:
        like_status = requests.get('https://api.bilibili.com/x/web-interface/archive/has/like', params={
            "bvid": bvid
        }, headers={
            "Referer": referer,
            "User-Agent": USER_AGENT
        }, cookies=user_cookie).json()
        if like_status['data'] > 0:
            reason = "点赞"
    
    return reason


@retry(wait=wait_fixed(20), stop=stop_after_attempt(3), reraise=True, retry=retry_if_not_exception_type(AssertionError))
def download_video_file(bvid, cid, save_title):
    referer = "https://www.bilibili.com/video/" + bvid

    reason = get_reason(bvid)

    # 解析视频下载链接
    r = requests.get("https://api.bilibili.com/x/player/playurl", params={
        "bvid": bvid,
        "cid": cid,
        "qn": 80  # 1080P(但不登陆可能只能获取到 720P)
    }, headers={
        "Referer": referer,
        "User-Agent": USER_AGENT
    }).json()
    
    if 'data' not in r:
        raise AssertionError("获取视频下载链接失败: " + str(r))
    download_link = r['data']['durl'][0]['url']
    # if '.mcdn.bilivideo.cn' in download_link:
    # logging.info('检测到 PCDN, 原链接: ' + download_link)
    # download_link = re.sub(r'://.*?/', '://upos-sz-mirror08c.bilivideo.com/', download_link)
    
    file_name = bvid + "_" + str(cid) + "_" + save_title

    logging.info('下载视频中: quality ' + str(r['data']['quality']) + ' ' + download_link)

    # request_args = {"headers": {
    #     "Referer": referer,
    #     "User-Agent": USER_AGENT
    # }}
    # download_r = SmartDL(download_link, request_args=request_args, progress_bar=False)
    # download_r.start()

    # data = download_r.get_data(binary=True)

    data = requests.get(download_link, headers={
        "Referer": referer,
        "User-Agent": USER_AGENT
    }, timeout=TIMEOUT).content

    if reason and not os.path.exists(reason + "_" + file_name + ".mp4"):
        logging.info('保存视频到本地, 原因: ' + reason)
        with open(reason + "_" + file_name + ".mp4", "wb") as f:
            f.write(data)

    logging.info('上传视频中, 大小: ' + str(len(data) / 1024 / 1024) + ' MiB')
    
    r = requests.post(os.environ['UPLOAD_URL'] + "/upload/" + quote(file_name + ".mp4", safe=''), files={
        'file': data
    }, timeout=TIMEOUT)

    if not r.ok:
        raise Exception("Request failed with code: " + str(r.status_code))


@retry(wait=wait_fixed(10), stop=stop_after_attempt(3), reraise=True)
def download_bvid(bvid, cid):
    key = bvid + "_" + cid
    with env.begin() as txn:
        if txn.get((key + "_info").encode()):
            logging.info("已经下载完成, 跳过: " + bvid)
            return

    referer = "https://www.bilibili.com/video/" + bvid

    # 获取视频基本信息
    r = requests.get("https://api.bilibili.com/x/web-interface/view", params={
        "bvid": bvid
    }, headers={
        "Referer": referer,
        "User-Agent": USER_AGENT
    })

    info = r.json()
    if 'data' not in info:
        raise AssertionError("获取视频信息失败: " + r.text)

    # 保存视频弹幕
    r = requests.get("https://comment.bilibili.com/" + str(info['data']['cid']) + ".xml", headers={
        "Referer": referer,
        "User-Agent": USER_AGENT
    })
    if not r.ok:
        raise AssertionError("获取弹幕失败: " + r.text)

    download_video_file(bvid, cid, validate_title(info['data']['title']))
    
    with env.begin(write=True) as txn:
        txn.put((key + "_info").encode(), json.dumps(info, ensure_ascii=False).encode())
        txn.put((key + "_danmaku").encode(), r.text.encode())


def check_and_download():
    logging.info(">>>开始检查")

    try:
        # 现在时间
        time_now = round(time.time())

        # 上一次获取成功的时间
        if not os.path.exists("last_time"):
            with open("last_time", "w") as f:
                f.write("0")

        with open("last_time", "r") as f:
            last_time = int(f.readline())

        # 检查登录
        if not check_login():
            logging.warning("登录失效!")
            try_login()

        # 获取历史记录
        time_view = 0
        to_download_list = []
        end_flag = False

        logging.info("上次检查: " + str(last_time) + " 现在时间: " + str(time_now))

        while True:
            r = requests.get("https://api.bilibili.com/x/web-interface/history/cursor", params={
                "view_at": time_view,
                "business": "archive"
            }, headers={
                "User-Agent": USER_AGENT
            }, cookies=user_cookie)
            ret = r.json()
            logging.info("获取数据: " + r.text)

            # 获取数据内容
            for i in ret['data']['list']:
                if i['view_at'] >= last_time:
                    if i['history']['bvid'] != "":
                        to_download_list.append(i)
                    time_view = i['view_at']
                else:
                    end_flag = True
                    break

            if end_flag:
                break

            # 没有数据则结束
            if ret['data']['cursor']['ps'] == 0:
                break

            time.sleep(2)

        logging.info("获取视频列表完毕, 共计: " + str(len(to_download_list)))

        # 下载 (多线程会被封 ip...)
        success = 0
        fail = 0

        for i in to_download_list:
            logging.info("开始下载: " + i['history']['bvid'])
            try:
                download_bvid(i['history']['bvid'], str(i['history']['cid']))
                logging.info("下载成功: " + i['history']['bvid'])
                success += 1
            except Exception as e:
                logging.exception("下载失败: " + i['history']['bvid'])
                wechat_push("下载失败: " + i['history']['bvid'] + " " + str(e))
                fail += 1
            logging.info("[进度回报]成功: " + str(success) + ", 失败: " + str(fail)
                         + ", 进度: " + str((success + fail) / len(to_download_list)))
            time.sleep(5)  # 防止访问 API 过快被封

        wechat_push("下载完成, 成功: " + str(success) + ", 失败: " + str(fail))

        with open("last_time", "w") as f:
            f.write(str(time_now))

        logging.info(">>>下载结束")
    except Exception as e:
        logging.error(e)
        wechat_push("获取过程中出现未知错误: " + str(e))


# 检查 cookie 是否失效
def check_login():
    r = requests.get("https://api.bilibili.com/x/web-interface/nav", headers={
        "User-Agent": USER_AGENT
    }, cookies=user_cookie)
    logging.info("检查登录: " + r.text)
    return r.json()['code'] == 0


# 尝试登录一次
def login():
    # 获取登录二维码链接
    r = requests.get("https://passport.bilibili.com/x/passport-login/web/qrcode/generate", headers={
        "User-Agent": USER_AGENT
    })

    qr_url = ""
    qr_key = ""

    ret = r.json()

    if ret.get('code') == 0:
        qr_url = ret['data']['url']
        qr_key = ret['data']['qrcode_key']
        logging.info("获取登录链接: " + qr_url)
    else:
        raise Exception("获取登录链接失败: " + r.text)

    # 推到微信, 等待扫码
    wechat_push("请扫描链接中二维码登录: " + "https://cli.im/api/qrcode/code?text=" + quote(qr_url))

    while True:
        r = requests.get("https://passport.bilibili.com/x/passport-login/web/qrcode/poll", headers={
            "User-Agent": USER_AGENT
        }, params={
            "qrcode_key": qr_key
        })
        ret = r.json()
        
        try:
            logging.info("等待登录: " + ret['data']['message'])
            if ret['data']['message'] == "二维码已失效":
                raise TimeoutError("登录超时")
            elif ret['data']['refresh_token'] != "":
                logging.info("登录成功! Cookie: " + str(r.cookies.get_dict()))
                # 设置 cookie
                global user_cookie
                user_cookie = r.cookies.get_dict()
                wechat_push("登录成功!")
                break
        except Exception as e:
            raise AssertionError("登录过程出错: " + str(e) + " " + r.text)

        time.sleep(5)


# 登录 (连续失败 3 次, 则等待半小时再试)
def try_login():
    if check_login():
        return

    while True:
        success_flag = False
        for i in range(0, 3):
            try:
                login()
                success_flag = True
                break
            except Exception as e:
                wechat_push("登录出错: " + str(e))
                time.sleep(10)
        if success_flag:
            # Cache cookie
            with open("cached_cookies", "w") as f:
                json.dump(user_cookie, f)
            break
        time.sleep(30 * 60)


# Load cached cookie
try:
    with open("cached_cookies", "r") as f:
        user_cookie = json.load(f)
except:
    pass


if __name__ == '__main__':
    env = lmdb.open("meta.db", map_size=2 ** 40)

    try_login()
    check_and_download()

    # 定时任务
    scheduler = BlockingScheduler()
    scheduler.add_job(check_and_download, 'cron', hour=os.environ['RUN_HOUR'], max_instances=1)
    scheduler.start()
