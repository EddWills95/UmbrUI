# Libraries provided by the system
import pygame
import pygame.freetype
import time
import os

# RPC
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import grpc

# Consts
from consts import black, background_color, bold_font, light_font, columns_x, rows_y, screenshot_location

# Local libraries
from lib.network import get_ip, get_tor_address
from lib.qr_generator import generate_qr_code
from lib.lnd import LndGRPC
from lib.btc import BtcRPC
import lib.rpc_pb2 as ln
import lib.rpc_pb2_grpc as lnrpc


class UmbrUI():
    loaded = False

    def __init__(self):
        os.putenv("SDL_VIDEODRIVER", "dummy")
        os.putenv("SDL_AUDIODRIVER", "dummy")

        self.init_screen()
        
        # Init RPC connections
        self.btc_grpc = BtcRPC()
        self.lnd_grpc = LndGRPC()

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
        self.smallTextFont = pygame.freetype.Font(bold_font, 20)

    # Builds static data (logo, ip, qr and tor)
    def mainUI(self):
        self.add_logo_and_text()
        self.add_qr_code()
        self.build_info_section("admin", get_ip(), (520, 120), False, True)
        self.build_info_section("tor", get_tor_address(), (columns_x[0], rows_y[0]), self.smallTextFont)
        
        pygame.display.update() 

        print("Saving screenshot of static elements")
        self.save_screenshot() 

        self.loaded = True

    # Get/refresh all elements that can be updated
    def load_updatable_elements(self):
        self.build_info_section("Max Send", self.lnd_grpc.get_max_send(), (columns_x[0], rows_y[1]))
        self.build_info_section("Max Recieve", self.lnd_grpc.get_max_receieve(), (columns_x[1], rows_y[1]))
        self.build_info_section("Active Channels", self.lnd_grpc.get_active_channels(), (columns_x[2], rows_y[1]))
        self.build_info_section("24H Forwards", self.lnd_grpc.get_forwarding_events(), (columns_x[0], rows_y[2]))
        self.build_info_section("Sync progress", str(self.btc_grpc.get_sync_progress()) + "%", (columns_x[1], rows_y[2]))
        
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
