import pyqrcode
import pygame
import os

QR_file_name = "QR.png"

def generate_qr_code(data):
    qr = pyqrcode.create(data)
    qr.png(QR_file_name, scale=4, module_color=(0,0,0,255), background=(255,255,255,255), quiet_zone=0)
    img = pygame.image.load(QR_file_name)
    os.remove(QR_file_name)
    return img