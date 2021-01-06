import pyqrcode
import pygame
import os

QR_file_name = "QR.png"
QR_mini_img = "assets/umbrel-qr-icon.png"

def generate_qr_code(data):
    container = pygame.Surface((100, 100))
    container.fill((255,255,255, 255))
    
    qr = pyqrcode.create(data)
    qr.png(QR_file_name, scale=4, module_color=(0,0,0), background=(255,255,255), quiet_zone=0)
    img = pygame.image.load(QR_file_name)
    
    # Get the rect of the qr code image
    img_rect = img.get_rect()

    # Load and scale mini image
    mini_img = pygame.image.load(QR_mini_img).convert_alpha()
    mini_img = pygame.transform.smoothscale(mini_img, (25, 25))
    
    mini_img_rect = mini_img.get_rect(center=(img_rect.width / 2, img_rect.height / 2))

    # Load mini image onto main image  
    container.blit(img, img_rect)
    container.blit(mini_img, mini_img_rect)

    # Cleanup created image
    os.remove(QR_file_name)
    return container
    