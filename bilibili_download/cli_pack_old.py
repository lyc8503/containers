import json
import os
import re
import logging

import lmdb

from main import download_video_file, validate_title

os.chdir("/download")
env = lmdb.open("meta.db", map_size=2 ** 40)

for folder in os.listdir():
    if not os.path.isdir(folder):
        continue

    try:
        with open(f"{folder}/info.json", "r") as f:
            data = json.load(f)
    
        with open(f"{folder}/danmaku.xml", "r") as f:
            danmaku = f.read()
    except:
        logging.error(f"Failed to load {folder}")
        continue
    
    cid = int(re.search(r"<chatid>(\d+)</chatid>", danmaku).group(1))
    bvid = data['data']['bvid']
    title = validate_title(data['data']['title'])
    key = bvid + "_" + str(cid)
    with env.begin() as txn:
        if txn.get((key + "_info").encode()) is not None:
            logging.info(f"已经下载完成, 跳过: {folder}")
            continue

    logging.info(f"Downloading {bvid} {title}")
    
    try:
        download_video_file(bvid, cid, title)
    except Exception as e:
        logging.error(f"Failed to download {bvid} {title}", exc_info=e)
        continue

    with env.begin(write=True) as txn:
        txn.put((key + "_info").encode(), json.dumps(data, ensure_ascii=False).encode())
        txn.put((key + "_danmaku").encode(), danmaku.encode())
