FROM python:3.9.10-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY personal_site.conf ./

RUN apt-get update -y
RUN apt-get install nginx gcc -y

# Nginx install and setup
RUN cp personal_site.conf /etc/nginx/sites-enabled/
RUN update-rc.d nginx enable

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD service nginx start && uwsgi --ini uwsgi.ini

