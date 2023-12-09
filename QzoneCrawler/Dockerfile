FROM python:3.10.13-slim-bookworm

MAINTAINER lyc8503 me@lyc8503.site

# 挂载位置
VOLUME /download

# 修改时区
ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install requests selenium pillow apscheduler tenacity opencv-python-headless numpy --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple

# 添加文件
COPY ./*.py /qzone/

WORKDIR /qzone/

ENTRYPOINT python3 -u main.py
