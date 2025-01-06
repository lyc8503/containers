FROM python:3.10.13-slim-bookworm

MAINTAINER lyc8503 me@lyc8503.net

RUN pip3 install fastapi telethon aiohttp PySocks --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple

# 添加文件
COPY ./*.py /tele/

WORKDIR /tele/

ENTRYPOINT python3 -u main.py
