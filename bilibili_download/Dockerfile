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

# 安装依赖
RUN Deps="aria2" \
    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm main contrib non-free non-free-firmware" > /etc/apt/sources.list \
    && apt-get update \
    && apt-get install $Deps --no-install-recommends --no-install-suggests -y  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /etc/apt/sources.list

RUN pip3 install requests apscheduler easyprocess tenacity --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY main.py /bilidown/

ENTRYPOINT python3 -u main.py
