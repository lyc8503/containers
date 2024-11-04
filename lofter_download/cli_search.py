import json
from berkeleydb import db as bdb
import time
from tqdm import tqdm


db = bdb.DB()
db.open("/download/posts.db", None, bdb.DB_HASH)

keyword = input("keyword: ")
print()

start = time.time()
counter = 0

pbar = tqdm()
cursor = db.cursor()
record = cursor.first()

stat = dict()

while record:
    pbar.update(1)
    k, v = record
    k, v = k.decode('utf-8'), v.decode('utf-8')

    if k.startswith("stat"):
        stat[k] = json.loads(v)
        record = cursor.next()
        continue
    
    if keyword in v:
        print(v)
        counter += 1
    record = cursor.next()

print(f"Found {counter} posts in {time.time() - start:.2f} seconds.")
print("===== Stats ======")
for i in sorted(stat.keys()):
    print(i, len(stat[i]))