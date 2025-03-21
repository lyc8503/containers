import aiohttp
import dm_pb2 as Danmaku
from google.protobuf.json_format import MessageToDict


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

async def fetch_danmaku(session, cid, segment):
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Pixel 4 XL Build/QQ3A.200805.001)",
    }
    tmp = []
    try:
        for segidx in range(1, max(1, segment) + 1):
            url = f"https://api.bilibili.com/x/v2/dm/list/seg.so?type=1&oid={cid}&segment_index={segidx}"
            async with session.get(url, headers=headers, proxy=HTTP_RPOXY) as response:
                data = await response.read()
                danmaku_seg = Danmaku.DmSegMobileReply()
                danmaku_seg.ParseFromString(data)
                data = MessageToDict(danmaku_seg)
                tmp.extend(data.get('elems', []))
    except Exception as e:
        print(f"Error: {e}")
        return cid, segment, {
            "code": -114514,
            "err": str(e)
        }
    return cid, tmp

async def fetch_danmaku_xml(session, cid):
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Pixel 4 XL Build/QQ3A.200805.001)",
    }
    url = f"https://comment.bilibili.com/{cid}.xml"
    try:
        async with session.get(url, headers=headers, proxy=HTTP_RPOXY) as response:
            return cid, await response.text()
    except Exception as e:
        print(f"Error: {e}")
        return cid, "ERROR: " + str(e)

async def fetch_tags(session, av):
    url = f"https://api.bilibili.com/x/web-interface/view/detail/tag?aid={av}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer": f"https://www.bilibili.com/video/av{av}"
    }
    try:
        async with session.get(url, headers=headers) as response:
            return av, await response.json()
    except Exception as e:
        print(f"Error: {e}")
        return av, {
            "code": -114514,
            "err": str(e)
        }
    