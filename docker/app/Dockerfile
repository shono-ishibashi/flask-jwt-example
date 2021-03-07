FROM python:3.9.1-alpine3.12

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD src/requirements.txt /app
ADD docker/wait-for-it.sh /usr/local/bin/wait-for-it.sh

RUN apk add --update --no-cache make bash gcc g++ tzdata vim git
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x /usr/local/bin/wait-for-it.sh