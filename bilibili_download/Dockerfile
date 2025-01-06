FROM python:3.10.13-slim-bookworm

MAINTAINER lyc8503 me@lyc8503.net

VOLUME /download

WORKDIR /bilidown/

# 修改时区
ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install requests apscheduler tenacity lmdb pySmartDL --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY *.py /bilidown/

ENTRYPOINT python3 -u main.py
