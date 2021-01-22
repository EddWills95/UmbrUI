FROM aarondewes/python-grpc:v1.35.0

RUN apt-get install -y libsdl2-dev libsdl2-mixer-dev libsdl2-image-dev libsdl2-ttf-dev libfreetype6-dev libjpeg-dev libportmidi-dev gcc g++ make && \
    pip3 install pypng pygame pyqrcode python-bitcoinrpc && \ 
    apt-get remove -y gcc g++ make && \
    apt-get autoremove -y && \
    apt-get clean

WORKDIR /app

COPY . .
# RUN ["python3", "--version"]
CMD ["python3", "-u", "main.py"]
