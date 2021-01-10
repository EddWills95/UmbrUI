# FROM debian:buster-slim
FROM python:3.7-slim
WORKDIR /code

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install pygame pyqrcode pypng

COPY . .
# RUN ["python", "--version"]
CMD ["python3", "ui.py"]