FROM python:3.10.13-slim-bookworm
MAINTAINER lyc8503 me@lyc8503.site

VOLUME /uploaded
RUN pip3 install fastapi uvicorn python-multipart --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY ./*.py /app/
WORKDIR /app/

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 3000 --ssl-keyfile=/key.pem --ssl-certfile=/cert.pem