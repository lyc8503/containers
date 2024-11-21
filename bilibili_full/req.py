from aiohttp_requests import requests

async def fetch_metadata(av):
    req = await requests.get(f"https://api.bilibili.com/x/web-interface/view?aid={av}", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
        "Referer": f"https://www.bilibili.com/video/av{av}"
    })

    try:
        return await req.json()
    except:
        raise Exception(req.text)
