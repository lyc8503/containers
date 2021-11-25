import logging
from urllib import parse

import requests


def get_author(author_name):
    logging.info("开始获取: " + author_name)

    temp = []

    page_size = 100
    pos = 0

    while True:
        r = requests.post("https://api.lofter.com/v2.0/blogHomePage.api?product=lofter-android-6.25.2", data=parse.urlencode({
            "blogdomain": f"{author_name}.lofter.com",
            "method": "getPostLists",
            "returnData": 1,
            "limit": page_size,
            "offset": pos
        }), headers={
            "User-Agent": "LOFTER-Android 6.25.2",
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
        }, timeout=20).json()

        temp += r['response']['posts']
        pos += page_size
        # 结果
        logging.info(f"预期获取: {pos}, 实际获取: {len(temp)}, 本次获取: {len(r['response']['posts'])}")
        if len(r['response']['posts']) < page_size:
            break
    
    ret = []
    for i in temp:
        try:
            # if i['post']['hot'] < 10:
            #     continue
            i['post']['_id'] = i['post']['blogPageUrl']
            
            i['post']['blogNickName'] = i['post']['publisherMainBlogInfo']['blogNickName']
            del i['post']['publisherMainBlogInfo']
            del i['post']['blogSettings']
            del i['post']['blogInfo']

            i['post']['hotComments'] = i['hotComments']
            i = i['post']

            ret.append(i)
        except Exception as e:
            logging.exception(e)
            logging.warning("处理时发生错误, 继续...")

    logging.info(f"筛选后长度: {len(ret)}")
    return ret
