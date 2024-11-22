from req import fetch_metadata
import asyncio
import tqdm


success = 0

async def main():
    tasks = []
    for i in (pbar := tqdm.trange(1, 10_0000_0000)):
        tasks.append(asyncio.create_task(fetch_metadata(i)))
        while len(tasks) >= 20:
            finished, unfinished = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            
            for r in finished:
                if r.result()['code'] == 0:
                    global success
                    success += 1
                    if success % 100 == 0:
                        pbar.set_description(f"Success: {success}")
            
            tasks = list(unfinished)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
