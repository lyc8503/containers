from aiohttp import web
from telethon import TelegramClient
import os
# from pybaiduphoto import API as BaiduPhotoAPI
# from asgiref.sync import sync_to_async
import json
from FastTelethon import download_file, upload_file


api_id = 28400568
api_hash = '7beee8e9bb1ea295c3772041db8490e7'
TG_ENTITY = -1001957671333


# bd_api = BaiduPhotoAPI(cookies = {
#     "STOKEN": "",
#     "BDUSS": ""
# })


# def do_bdpic_upload(name, file_content):
#     name = name.replace("/", "_")
#     tmp_path = "/tmp/" + name
#     try:
#         with open(tmp_path, "wb") as f:
#             f.write(file_content)
#         return bd_api.upload_1file(tmp_path)
#     finally:
#         try:
#             os.remove(tmp_path)
#         except:
#             pass


async def upload(request: web.Request):
    global tg
    path = request.match_info.get('path')
    print("Upload path: " + path)
    data = await request.post()
    print(data)

    uploaded_file = await upload_file(tg, data['file'].file)
    result = await tg.send_file(entity=TG_ENTITY, caption=path, file=uploaded_file)
    
    print(str(result))
    print("Uploaded: " + path) 

    return web.Response(text=str(result))


# async def upload_bdpic(request: web.Request):
#     name = request.match_info.get('name')
#     print("Upload bdpic: " + name)
#     data = await request.post()
#     print(data)

#     file_content = data['file'].file.read()

#     r = await sync_to_async(do_bdpic_upload)(name, file_content)
#     print(r.info)
#     print("Uploaded bdpic: " + name) 

#     return web.Response(text=json.dumps(r.info))



async def build_app():
    global tg
    tg = TelegramClient('/tmp/chen_storage_test', api_id, api_hash, proxy=("socks5", '192.168.1.51', 7890))
    await tg.start()

    app = web.Application(client_max_size=4 * 1024 * 1024 * 1024)
    app.add_routes([web.post('/upload/{path}', upload)])
    # app.add_routes([web.post('/upload_bdpic/{name}', upload_bdpic)])
    
    return app


if __name__ == '__main__':
    web.run_app(build_app(), port=os.environ.get('PORT', 5000))
