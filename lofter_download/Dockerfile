FROM python:3.9-alpine

MAINTAINER lyc8503 lyc8503@foxmail.com

# 挂载位置
VOLUME /data

# 修改时区 / 镜像
RUN set -eux && sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

RUN apk add --no-cache tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && apk del tzdata

# 安装依赖
RUN apk add --no-cache gcc musl-dev libxslt-dev

RUN pip3 install html2text requests apscheduler tenacity lxml tzdata --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple

# 添加文件
COPY *.py /lof/

WORKDIR /lof/

ENTRYPOINT python3 -u entrypoint.py