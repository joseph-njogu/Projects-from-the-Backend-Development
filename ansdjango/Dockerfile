FROM python:3.6

#set env variables
# 1. remove .pyc files from container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set a directory in Docker
WORKDIR /code

# copy the requirements file
COPY requirements.txt /code

#install dependencies
RUN pip3 install -r requirements.txt

#copy files
COPY . /code
