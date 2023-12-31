# 返回的数据处理 提取 JSON
import json
import logging
import os
import re
import time

# 微信推送
import requests
from requests.auth import HTTPBasicAuth
from tenacity import wait_fixed, stop_after_attempt, retry


@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def wechat_push(msg):
    logging.info("推送: " + msg)
    logging.debug(requests.post("https://server.lyc8503.site/wepush", json={
        "key": "wepushkey",
        "msg": "[Qzone Get]" + msg
    }, timeout=5).text)


def wechat_push_img(b64):
    logging.debug(requests.post("https://server.lyc8503.site/wepush", json={
        "key": "wepushkey",
        "type": "image",
        "msg": b64
    }, timeout=5).text)


def to_json(string):
    logging.debug(string)

    string = string.strip()
    first_index = -1
    for i2 in range(0, len(string)):
        if string[i2] == '(':
            first_index = i2
            break
    if string[-2:] == ');':
        return json.loads(string[first_index + 1:-2])
    elif string[-1:] == ')':
        return json.loads(string[first_index + 1:-1])
    else:
        raise Exception("Not a callback: " + str(string))


# 通过 cookie string 获取 gtk
def get_gtk(cookie):
    p_skey = cookie[cookie.find('p_skey=') + 7: cookie.find(';', cookie.find('p_skey='))]
    h = 5381
    for i2 in p_skey:
        h += (h << 5) + ord(i2)
    return h & 2147483647
