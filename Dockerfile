FROM debian:buster-slim
WORKDIR /code

RUN apt-get update
RUN apt-get install -y python-pygame python-pyqrcode

COPY . .
# RUN ["python", "--version"]
CMD ["python", "ui.py"]