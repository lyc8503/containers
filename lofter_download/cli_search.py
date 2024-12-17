import json
import lmdb
import time
from tqdm import tqdm

env = lmdb.open("/download/posts.db", readonly=True)
keyword = input("keyword: ")
print()

start = time.time()
counter = 0

pbar = tqdm(total=env.stat()['entries'])
stat = dict()

with env.begin() as txn:
    cursor = txn.cursor()
    for key, value in cursor:
        pbar.update(1)
        k, v = key.decode('utf-8'), value.decode('utf-8')

        if k.startswith("stat"):
            stat[k] = json.loads(v)
            continue

        if keyword in v:
            print(v)
            counter += 1

print(f"Found {counter} posts in {time.time() - start:.2f} seconds.")
print("===== Stats ======")
for i in sorted(stat.keys()):
    print(i, len(stat[i]))
