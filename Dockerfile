FROM python:3.6-alpine

LABEL maintainer="peanut@itech8.com"

RUN apk add --no-cache openssl

WORKDIR ./app

COPY . .

RUN pip install -r requirement.txt -i https://mirrors.aliyun.com/pypi/simple/

EXPOSE 9090

CMD ["python","main.py"]