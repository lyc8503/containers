from req import fetch_metadata
import asyncio


async def main():
    tasks = []
    count = 0
    for i in range(1, 10_0000_0000):
        tasks.append(asyncio.create_task(fetch_metadata(i)))
        while len(tasks) >= 100:
            finished, unfinished = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            
            for r in finished:
                count += 1
                print(count)
                print(r.result()['code'])
            
            tasks = list(unfinished)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
