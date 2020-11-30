FROM python:3.8.6-alpine

RUN mkdir -p /home/app/

RUN apk update \
    && apk add make gcc python3-dev musl-dev \
    && apk add libpq

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


