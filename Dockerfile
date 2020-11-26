FROM python:3.8.6-alpine


RUN mkdir -p /home/app/


RUN addgroup -S app && adduser -S app -G app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


ENV HOME=/home/app/
ENV APP_HOME=/home/app/
WORKDIR $APP_HOME

RUN apk update \
    && apk add make gcc python3-dev musl-dev \
    && apk add libpq

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN chown -R app:app $APP_HOME

USER app
