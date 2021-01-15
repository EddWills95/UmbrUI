# Libraries provided by the system
import pygame
import pygame.freetype
import time
import os
import json
# RPC
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import grpc

# Consts
from consts import black, background_color, bold_font, light_font, columns_x, rows_y, screenshot_location

# Local libraries
from lib.network import get_ip
from lib.qr_generator import generate_qr_code
from lib.lnd import LndGRPC
from lib.btc import BtcRPC
import lib.rpc_pb2 as ln
import lib.rpc_pb2_grpc as lnrpc
from lib.infosections import InfoSectionsList


class UmbrUI():
    loaded = False

    def __init__(self):
        os.putenv("SDL_VIDEODRIVER", "dummy")
        os.putenv("SDL_AUDIODRIVER", "dummy")

        self.init_screen()

    # Sets up the basic view without elements
    def init_screen(self):
        # PyGame
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("UmbrUI")
        size = (720, 480)
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        self.screen.fill(background_color)
        
        # Fonts
        self.titleFont = pygame.freetype.Font(bold_font, 56)
        self.headingFont = pygame.freetype.Font(light_font, 18)
        self.textFont = pygame.freetype.Font(bold_font, 32)

    # Builds static data (logo, ip, qr and tor)
    def mainUI(self):
        self.add_logo_and_text()
        self.add_qr_code()
        self.build_info_section("admin", get_ip(), (520, 120), False, True)
        
        pygame.display.update() 

        print("Saving screenshot of static elements")
        self.save_screenshot() 

        self.loaded = True

    # Get/refresh all elements that can be updated
    def load_updatable_elements(self):
        sectionsList = InfoSectionsList()
        column = 0
        row = 0
        try:
            with open("/usr/data.json") as f:
                userData = json.loads(f.read())
        except Exception:
            # Load defaults
            with open("./data.json") as f:
                userData = json.loads(f.read())

        for element in userData["displayedElements"]:
            # Not more than we can get onto the screen (4 rows)
            if(row != 3):
                try:
                    elementData = eval("sectionsList." + element + "(sectionsList)").getData()
                    # elementData[0]: title
                    # elementData[1]: Displayed data
                    # elementData[2]: Element gets it's own row if set to True
                    # elementData[3]: Custom text font
                    if(elementData[2] and column != 0):
                        row = row + 1
                        column = 0
                    self.build_info_section(elementData[0], elementData[1], (columns_x[column], rows_y[row]), elementData[3])
                    column = column + 1
                    if(column == 3 or elementData[2]):
                        row = row + 1
                        column = 0
                # Ignore non-existing elements
                except Exception: pass
        
        pygame.display.update() 

        print("Saving updated screenshot")
        self.save_screenshot()

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

    # When we move away from SPI screen we will not need this
    def save_screenshot(self):
        pygame.display.flip() 
        pygame.image.save(self.screen, "/usr/screenshots/UmbrUI.png")

    def warnUI(self):
        self.screen.fill(background_color)
        self.build_info_section("", "You haven't opened the Umbrel dashboard yet.", (columns_x[0], rows_y[0]))
        self.build_info_section("", "Please do that first to access this screen.", (columns_x[0], rows_y[1] - 70))
        pygame.display.update()

        print("Saving updated screenshot")
        self.save_screenshot()
