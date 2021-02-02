import pyqrcode
import pygame
import os

from consts import QR_file_name, QR_size, QR_mini_img


def generate_qr_code(data):
    container = pygame.Surface(QR_size)
    container.fill((255, 255, 255, 255))

    qr = pyqrcode.create(data)
    qr.png(QR_file_name, scale=3, module_color=(0, 0, 0),
           background=(255, 255, 255), quiet_zone=0)
    img = pygame.image.load(QR_file_name)
    img = pygame.transform.scale(img, QR_size)

    # Get the rect of the qr code image
    img_rect = img.get_rect()

    # Load and scale mini image
    mini_img = pygame.image.load(QR_mini_img)
    mini_img = pygame.transform.scale(mini_img, (35, 35))

    mini_img_rect = mini_img.get_rect(
        center=(img_rect.width / 2, img_rect.height / 2))

    # Load mini image onto main image
    container.blit(img, img_rect)
    container.blit(mini_img, mini_img_rect)

    # Cleanup created image
    os.remove(QR_file_name)
    return container
