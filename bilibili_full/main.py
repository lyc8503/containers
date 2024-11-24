import aiohttp
import asyncio
from req import fetch_metadata
import tqdm
from pymongo import AsyncMongoClient


stats = dict()
buffer = []

async def main():
    tasks = set()
    async with aiohttp.ClientSession() as session, AsyncMongoClient("mongodb://localhost:27017/bili") as client:
        for i in (pbar := tqdm.trange(5960000, 10_0000_0000)):
            tasks.add(asyncio.create_task(fetch_metadata(session, i)))
            while len(tasks) >= 80:
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

if __name__ == "__main__":
    asyncio.run(main())
