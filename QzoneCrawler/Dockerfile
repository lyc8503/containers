FROM python:3.9.7-slim-bullseye

MAINTAINER lyc8503 lyc8503@foxmail.com

# 挂载位置
VOLUME /download

RUN pip3 install requests selenium pillow apscheduler tenacity opencv-python-headless numpy --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple

# 添加文件
COPY ./*.py /qzone/

WORKDIR /qzone/

ENTRYPOINT python3 -u main.py
