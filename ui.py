# Libraries provided by the system
import pygame
import pygame.freetype
import time
import os

# Local libraries
from lib.network import get_ip
from lib.qr_generator import generate_qr_code

from consts import black, background_color, bold_font, light_font, columns_x, rows_y, screenshot_location

class UmbrUI():
    loaded = False

    def __init__(self):
        os.putenv("SDL_VIDEODRIVER", "dummy")
        os.putenv("SDL_AUDIODRIVER", "dummy")

        pygame.display.init()
        size = (720, 480)
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

        # Set background color to umbrel
        self.screen.fill(background_color)

        self.init()

        self.add_logo_and_text()
        self.add_qr_code()
        self.build_info_section("admin", get_ip(), (520, 120), False, True)
        # Tor is always going to be really long so not sure about this one ... :/
        self.build_info_section("tor", "r7cckasdfasfdargsnf4eoxaivgiykmrcglhg4zlwueknhuw66otiid.onion", (columns_x[0], rows_y[0]), 
        pygame.freetype.Font(bold_font, 22))

        self.build_info_section("Max Send", "3M Sats", (columns_x[0], rows_y[1]))
        self.build_info_section("Max Recieve", "2M Sats", (columns_x[1], rows_y[1]))
        self.build_info_section("Active Channels", "16", (columns_x[2], rows_y[1]))
        self.build_info_section("24H Forwards", "53", (columns_x[0], rows_y[2]))
            
        pygame.display.set_caption("UmbrUI")
        pygame.display.update() 
        
        self.loaded = True

    def init(self):
        pygame.init()
        self.titleFont = pygame.freetype.Font(bold_font, 56)
        self.headingFont = pygame.freetype.Font(light_font, 18)
        self.textFont = pygame.freetype.Font(bold_font, 32)

    def add_logo_and_text(self):
        title_surf, title_rect = self.titleFont.render("umbrel")

        umbrelImg = pygame.image.load('assets/logo.png')
        umbrelImg = pygame.transform.scale(umbrelImg, (88, 100))
        
        self.screen.blit(umbrelImg, (16, 16))
        self.screen.blit(title_surf, (110, 50))

    def add_qr_code(self):
        qrImg = generate_qr_code(get_ip())
        
        self.screen.blit(qrImg, (544, 16))

    def build_info_section(self, heading_text, text_text, position, textfont=False, alignRight=False):
        if textfont == False:
            textfont = self.textFont
        heading_surf, heading_rect = self.headingFont.render(heading_text, black)
        text_surf, text_rect = textfont.render(text_text, black)

        x, y = position
        heading_rect.topleft = position
        text_rect.topleft = (x, y + 25)
        
        if alignRight:
            heading_rect.topright = (x, y)
            text_rect.topright = (x, y + 25)


        self.screen.blit(heading_surf, heading_rect)
        self.screen.blit(text_surf, text_rect)

    def save_screenshot(self):
        pygame.display.flip() 
        pygame.image.save(self.screen, "/usr/screenshots/UmbrUI.png")
        

# Create an instance of the UmbrUI class
game = UmbrUI()

print("Taking screenshot")
game.save_screenshot()

pygame.quit()
exit()

# while True:
#     # Wait until all the elements have loaded the first time
#     if game.loaded:
#         print('Printing image')
#         # Take a screenshot
#         # We should add optimisations when we do data fetching
#         game.save_screenshot()
#         time.sleep(2)
    
#     for event in pygame.event.get():
    
#         # if event object type is QUIT
#         # then quitting the pygame
#         # and program both.
#         if event.type == pygame.QUIT:
#             # deactivates the pygame library
#             pygame.quit()

#             # quit the program.
#             quit()
     
#     # # Draws the surface object to the screen.
#     pygame.display.update()
