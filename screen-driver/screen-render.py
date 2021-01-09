import socket
import time
import os, sys
from PIL import Image

# if socket.gethostname() == "rpiv2":
import gfxcili.ili9486
    # width, height, SPI, SPEED, CS, RST, RS
lcd = gfxcili.ili9486.ili9486(480, 320, 0, 3200000, 8, 25, 24)

lcd.init()

while True:
    old_image = None
    
    with Image.open("/usr/screenshots/UmbrUI.png") as im:
        if old_image != im:
            old_image = im
            draw_image(0,0, im)

    time.sleep(5)