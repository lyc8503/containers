import aiohttp
import asyncio
from req import fetch_metadata
import tqdm
from pymongo import AsyncMongoClient
from multiprocessing import Process

stats = dict()
buffer = []

async def main(start, end, pos):
    tasks = set()
    async with aiohttp.ClientSession() as session, AsyncMongoClient("mongodb://localhost:27017/bili") as client:
        for i in tqdm.trange(start, end, position=pos, desc=f"Process #{pos}"):
            tasks.add(asyncio.create_task(fetch_metadata(session, i)))
            while len(tasks) >= 80 or (i == end - 1 and tasks):
                finished, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

                for r in finished:
                    av, ret = r.result()
                    
                    ret['_id'] = av
                    buffer.append(ret)
                    stats[ret['code']] = stats.get(ret['code'], 0) + 1

                    if len(buffer) >= 1000:
                        try:
                            await client.bili.meta.insert_many(buffer)
                        except Exception as e:
                            print(f"Mongo Error: {e}")
                        print(stats)
                        buffer.clear()
        if buffer:
            await client.bili.meta.insert_many(buffer)


if __name__ == "__main__":
    PROCESS_COUNT = 2
    processes = []
    start = 0
    end = 10_0000_0000

    for i in range(PROCESS_COUNT):
        left = start + (end - start) // PROCESS_COUNT * i
        right = start + (end - start) // PROCESS_COUNT * (i + 1)
        p = Process(target=asyncio.run, args=(main(left, right, i),))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
