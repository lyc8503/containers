import aiohttp


HTTP_RPOXY = 'http://127.0.0.1:2345'

async def fetch_metadata(session, av):
    url = f"https://api.bilibili.com/x/web-interface/view?aid={av}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer": f"https://www.bilibili.com/video/av{av}"
    }

    try:
        async with session.get(url, headers=headers, proxy=HTTP_RPOXY) as response:
            return av, await response.json()
    except Exception as e:
        print(f"Error: {e}")
        return av, {
            "code": -114514,
            "err": str(e)
        }
