import logging
import random
import time

import requests
from tenacity import stop_after_attempt, wait_fixed, retry

# 获取某个好友的信息
from util import to_json, get_gtk

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=True)
def get_uin_info(uin, cookie):
    r = requests.get("https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/main_page_cgi", params={
        "uin": uin,
        "param": "16",
        "g_tk": get_gtk(cookie)
    }, headers={
        "Cookie": cookie,
        "User-Agent": UA
    }, timeout=5)

    return to_json(r.text)['data']['module_16']['data']


# 获取当前账号好友列表
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=True)
def get_friends(uin, cookie):
    black_list = [66600000, 88882222, 1005200001, 622008102, 1006666003, 732952649]

    r = requests.get("https://h5.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_show_qqfriends.cgi?follow_flag=1&groupface_flag=0&fupdate=1",
                     params={
                         'uin': uin,
                         'g_tk': get_gtk(cookie)
                     }, headers={
            "Cookie": cookie,
            "User-Agent": UA
        }, timeout=5)

    friends = to_json(r.text)['data']['items']

    temp = {}
    for i2 in friends:
        if i2['uin'] not in black_list:
            temp[i2['uin']] = i2['remark']
    return temp


# 获取说说(一页)
def get_shuoshuo(uin, page, cookie):
    num = 40
    r = requests.get("https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6", params={
        "format": "jsonp",
        "need_private_comment": "1",
        "uin": uin,
        "pos": (page - 1) * num,
        "num": num,
        "g_tk": get_gtk(cookie)
    }, headers={
        "User-Agent": UA,
        "Cookie": cookie
    }, timeout=5)

    tmp = to_json(r.text)
    if tmp['result']['msg'] == '对不起，系统繁忙，请稍后重试':
        logging.warning("系统繁忙!")
        raise ConnectionError("返回系统繁忙.")

    time.sleep(random.random() * 5 + 2)

    return tmp


# 获取所有说说
@retry(stop=stop_after_attempt(3), wait=wait_fixed(30), reraise=True)
def get_shuoshuo_all(uin, cookie):
    ss_list = {}

    for i2 in range(1, 1000000):
        msglist = get_shuoshuo(uin, i2, cookie)['msglist']
        if msglist is None:
            logging.info("获取 " + str(uin) + " 空间: " + "没有更多内容. 获取结束.")
            break

        logging.info("获取 " + str(uin) + " 空间, 第 " + str(i2) + " 页: " + str(len(msglist)))
        for j in msglist:
            ss_list[j['tid']] = j

    return ss_list


# 获取一条说说详情
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=True)
def get_detail(uin, tid, cookie):
    r = requests.get("https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msgdetail_v6", params={
        "uin": uin,
        "tid": tid,
        "g_tk": get_gtk(cookie),
        "format": "jsonp",
        "need_private_comment": 1,
        "not_trunc_con": 1  # 获取完整内容
    }, headers={
        "User-Agent": UA,
        "Cookie": cookie
    }, timeout=5)
    return to_json(r.text)
