FROM python:3.9.10-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk add build-base linux-headers zlib-dev jpeg-dev
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD uwsgi --ini uwsgi.ini
