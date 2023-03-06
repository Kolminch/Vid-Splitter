# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# set working directory
WORKDIR /katana

# install bot dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install -r requirements.txt
RUN apt install ffmpeg

# copy bot files
COPY . .

# final configuration
ENV FLASK_APP=hello
EXPOSE 8000
CMD flask run --host 0.0.0.0 --port 8000