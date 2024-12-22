import json
import lmdb
import os


os.chdir("/download")
env = lmdb.open("meta.db", map_size=1024 * 1024 * 1024)

with env.begin() as txn:
    cursor = txn.cursor()
    for key, value in cursor:
        key, value = key.decode(), value.decode()
        if key.endswith("_info"):
            value = json.loads(value)
            print(key, value['data']['title'])
    cursor.close()
