# this is a utility script to pack the old downloaded files into an lmdb database
# run it manually

import pickle
import lmdb
import json
import os
import time

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

def pack_data(env):
    counter = 0
    t = time.time()
    txn = env.begin(write=True)

    for root, dirs, files in os.walk("/download/"):
        for file in files:
            if '.pickle' not in file:
                continue

            p = os.path.join(root, file)
            with open(p, "rb") as f:
                key = file.replace('.pickle', '') + "_" + root.split('/')[-1]
                print(f"packing {key}")
                content = pickle.load(f)
                content = json.dumps(content, ensure_ascii=False, cls=SetEncoder).encode("utf-8")
                txn.put(key.encode('utf-8'), content)
                counter += 1

                if counter % 1000 == 0:
                    txn.commit()
                    txn = env.begin(write=True)

    for root, dirs, files in os.walk("/download/posts"):
        for file in files:
            with open(os.path.join(root, file), "rb") as f:
                data = json.load(f)
                txn.put(file.replace('.json', '').encode('utf-8'), json.dumps(data, ensure_ascii=False).encode("utf-8"))
                counter += 1
                if counter % 1000 == 0:
                    print(f"{counter} files packed, {1000 / (time.time() - t):.1f} op/s, current: {os.path.join(root, file)}")
                    t = time.time()
                    if counter % 10000 == 0:
                        txn.commit()
                        print("txn committed")
                        txn = env.begin(write=True)

    txn.commit()

if __name__ == "__main__":
    if os.path.exists("/download/posts.db"):
        print("file exists")
        exit(1)

    env = lmdb.open('/download/posts.db', map_size=1099511627776)
    pack_data(env)
    env.close()
