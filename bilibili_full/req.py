import aiohttp


HTTP_RPOXY = 'http://127.0.0.1:2345'

async def fetch_metadata(av):
    url = f"https://api.bilibili.com/x/web-interface/view?aid={av}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer": f"https://www.bilibili.com/video/av{av}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, proxy=HTTP_RPOXY) as response:
            try:
                return await response.json()
            except:
                raise Exception(await response.text())
