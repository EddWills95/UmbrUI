FROM python:3-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3-pygame

COPY . .
# RUN ["python3", "--version"]
CMD ["python3", "ui.py"]

