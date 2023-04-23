FROM python:3.10.6-slim-buster

# install bot dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y python3 
RUN apt-get -y install python3-pip
RUN pip install -r requirements.txt
RUN apt-get -y install ffmpeg
# set working directory
WORKDIR /app

# copy bot files
COPY . .

# final configuration
EXPOSE 8000
CMD python3 bot.py --host 0.0.0.0 --port 8000
