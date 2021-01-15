FROM aarondewes/python-grpc:main

# Runtime dependencies of pygame
RUN apt-get install -y fonts-freefont-ttf libc6 libfreetype6 libjpeg62-turbo libpng16-16 libportmidi0 libsdl-image1.2 libsdl-mixer1.2 libsdl-ttf2.0-0 libsdl1.2debian libx11-6

RUN apt-get install -y libsdl2-dev libsdl2-mixer-dev libsdl2-image-dev libsdl2-ttf-dev libfreetype6-dev libjpeg-dev libportmidi-dev gcc g++ make && \
    pip3 install pypng pygame pyqrcode python-bitcoinrpc && \ 
    apt-get remove -y libsdl2-dev libsdl2-mixer-dev libsdl2-image-dev libsdl2-ttf-dev libfreetype6-dev libjpeg-dev libportmidi-dev gcc g++ make && \
    apt-get autoremove -y && \
    apt-get clean

WORKDIR /app

COPY . .
# RUN ["python3", "--version"]
CMD ["python3", "-u", "main.py"]
