FROM python:3.5

ENV PYTHONUNBUFFERED 1
MAINTAINER David Rodriguez <davrodri@cs.fiu.edu>

RUN apt-get update -y
RUN apt-get install -y binutils libproj-dev gdal-bin libgdal1-dev python3-gdal python-memcache

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD ["/bin/bash", "docker-entrypoint.sh"]
