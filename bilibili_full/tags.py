import os
import struct
import aiohttp
import asyncio

import pandas as pd
from req import fetch_tags
import tqdm
from pymongo import AsyncMongoClient, MongoClient
from multiprocessing import Process

stats = dict()
buffer = []

async def main(targets, pos):
    tasks = set()
    async with aiohttp.ClientSession() as session, AsyncMongoClient("mongodb://localhost:27017/bili") as client:
        for i in tqdm.tqdm(targets, position=pos, desc=f"Process #{pos}"):
            tasks.add(asyncio.create_task(fetch_tags(session, i)))
            while len(tasks) >= 80 or (i == targets[-1] and tasks):
                finished, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

                for r in finished:
                    av, ret = r.result()
                    
                    ret['_id'] = av
                    if ret['code'] != -114514:
                        buffer.append(ret)
                    stats[ret['code']] = stats.get(ret['code'], 0) + 1

                    if len(buffer) >= 1000:
                        try:
                            await client.bili.tags.insert_many(buffer)
                        except Exception as e:
                            print(f"Mongo Error: {e}")
                        print(stats)
                        buffer.clear()
        if buffer:
            await client.bili.tags.insert_many(buffer)


if __name__ == "__main__":
    PROCESS_COUNT = 1
    processes = []

    with open("final_candidates.bin", "rb") as f:
        loaded_candidates = list(struct.unpack(f'{os.path.getsize("final_candidates.bin") // 8}q', f.read()))
    print(len(loaded_candidates))

    with MongoClient("mongodb://localhost:27017/bili") as client:
        cursor = client.bili.tags.find({}, {'_id': 1})
        tag_ids = []
        for d in tqdm.tqdm(cursor):
            tag_ids.append(d['_id'])
    loaded_candidates = list(set(loaded_candidates) - set(tag_ids))
    print(len(loaded_candidates))

    for i in range(PROCESS_COUNT):
        targets = loaded_candidates[i::PROCESS_COUNT]
        p = Process(target=asyncio.run, args=(main(targets, i),))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
