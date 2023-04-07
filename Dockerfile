FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache bash postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN mkdir /src
RUN mkdir /vol

RUN adduser -D user

RUN chown -R user:user /src/
RUN chown -R user:user /vol/

USER user

COPY ./requirements.txt /src/requirements.txt
WORKDIR /src

ENV PATH $PATH:/home/user/.local/bin

RUN python -m pip install --upgrade pip
RUN python -m venv env
RUN source env/bin/activate
RUN pip install -r requirements.txt

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/ststic
RUN chmod -R 755 /vol/web

COPY . /src/
RUN pip install debugpy

WORKDIR /src/src
