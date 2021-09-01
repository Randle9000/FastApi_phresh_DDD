# get slim-buster image for python3.8
FROM python:3.8-slim-buster

# set working dir
WORKDIR /backend

# add environment variable to prevent from writing pyc file to disc and from buffering stdout and stderr
ENV PYTHONPATH "${PYTHONPATH}:/backend/"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
RUN pip install pip-tools
COPY ./requirements.txt /backend/requirements.txt
COPY ./requirements.dev.txt /backend/requirements.dev.txt
RUN pip-sync requirements.dev.txt

# used pip-tools instead
# RUN pip install -r requirements

# give permission to execute scripts
copy . /backend

RUN chmod -R +x ./scripts
EXPOSE 8000
