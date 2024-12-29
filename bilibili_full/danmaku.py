
import aiohttp
from pymongo import AsyncMongoClient
from req import fetch_danmaku_xml, fetch_danmaku
from tqdm import tqdm


buffer = []
mongo = AsyncMongoClient("mongodb://localhost:27017/bili")


async def main():
    tasks = set()
    todos = []
    for fn in ('pre1e9.bin', 'post1e9.bin'):
        with open(fn, 'rb') as f:
            while True:
                cid = f.read(7)
                if not cid:
                    break
                dur = f.read(1)
                todos.append(int.from_bytes(cid, byteorder='big'))
    todos = list(set(todos))

    async with aiohttp.ClientSession() as session:
        for cid in tqdm(todos):
            tasks.add(asyncio.create_task(fetch_danmaku_xml(session, cid)))
            while len(tasks) >= 80:
                finished, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

                for r in finished:
                    cid, elems = r.result()
                    # print(cid, len(elems.split('</d>')))
                    buffer.append({'_id': cid, 'danmaku': elems})
                
                if len(buffer) >= 1000:
                    try:
                        await mongo.bili.danmaku.insert_many(buffer)
                    except Exception as e:
                        print(f"Mongo Error: {e}")
                    buffer.clear()
                


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
