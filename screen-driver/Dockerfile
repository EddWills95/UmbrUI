FROM debian:buster-slim
WORKDIR /code

RUN apt-get update
RUN apt-get install -y python3-pygame python3-grpcio python3-grpc-tools python3-pyqrcode git gcc g++ make cmake sudo python3-pip libpng-dev libjpeg-dev

WORKDIR /
RUN git clone https://github.com/WiringPi/WiringPi.git

WORKDIR /WiringPi

RUN ./build

RUN pip3 install python-bitcoinrpc googleapis-common-protos gfxcili pillow

COPY . .

CMD ["python3", "screen-render.py"]