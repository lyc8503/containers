import logging
import random
import time
import urllib.parse

import requests

from util import parse_info


def get_tag(tag, type):
    """
    获取 tag 所有内容
    """
    logging.info("获取 TAG 列表: " + tag)
    got = 0
    size = 100
    real_got = 0
    max = 1200

    ret = []

    while True:
        payload = {
            "callCount": "1",
            "scriptSessionId": "${scriptSessionId}187",
            "httpSessionId": "",
            "c0-scriptName": "TagBean",
            "c0-methodName": "search",
            "c0-id": "0",
            "c0-param0": f"string:{urllib.parse.quote(tag)}",
            "c0-param1": "number:0",
            "c0-param2": "string:",
            "c0-param3": f"string:{type}",
            "c0-param4": "boolean:false",
            "c0-param5": "number:0",
            "c0-param6": f"number:{size}",
            "c0-param7": f"number:{got}",
            "c0-param8": f"number:{round(time.time() * 1000)}",
            "batchId": str(random.randint(100000, 999999))
        }

        url = "http://www.lofter.com/dwr/call/plaincall/TagBean.search.dwr"

        r = requests.post(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/105.0.0.0 Safari/537.36",
            "Referer": "http://www.lofter.com/tag/" + urllib.parse.quote(tag)
        }, data="\n".join([(k + "=" + v) for k, v in payload.items()]))
        got += size

        raw = r.text.split("activityTags")[1:]
        real_got += len(raw)
        logging.info(f"{tag} - 预期获取: {got}, 实际获取: {real_got}, 本页新增: {len(raw)}")

        parsed = parse_info(raw, r.text)
        ret += parsed

        if len(raw) == 0 or got >= max:
            logging.info("没有更多内容, 结束.")
            break

    return ret


def get_all_tag(tag):
    ret = []

    for i in ("date", "week", "month", "total"):
        for j in get_tag(tag, i):
            ret.append(j)

    return ret
