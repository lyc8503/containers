import logging
import random
import re

import requests

from util import parse_info


def get_all_like(user_url):
    """
    获取 like 所有内容
    """
    logging.info("获取 like 列表: " + user_url)
    got = 0
    size = 100
    real_got = 0

    ret = []

    r = requests.get(user_url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/105.0.0.0 Safari/537.36"
    }, timeout=20)
    blog_id = re.search(r"blogId=(\d*)", r.text).group(1)
    logging.info("blogId: " + blog_id)

    while True:
        payload = {
            "callCount": "1",
            "scriptSessionId": "${scriptSessionId}187",
            "httpSessionId": "",
            "c0-scriptName": "BlogBean",
            "c0-methodName": "queryLikePosts",
            "c0-id": "0",
            "c0-param0": f"number:{blog_id}",
            "c0-param1": f"number:{size}",
            "c0-param2": f"number:{got}",
            "c0-param3": "string:",
            "batchId": str(random.randint(100000, 999999))
        }

        url = "https://www.lofter.com/dwr/call/plaincall/BlogBean.queryLikePosts.dwr"

        r = requests.post(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/105.0.0.0 Safari/537.36",
            "Referer": "https://www.lofter.com/favblog"
        }, data="\n".join([(k + "=" + v) for k, v in payload.items()]))
        got += size

        raw = r.text.split("activityTags")[1:]
        real_got += len(raw)
        logging.info(f"{blog_id} - 预期获取: {got}, 实际获取: {real_got}, 本页新增: {len(raw)}")

        parsed = parse_info(raw, r.text)
        ret += parsed

        if len(raw) == 0:
            logging.info("没有更多内容, 结束.")
            break

    return ret
