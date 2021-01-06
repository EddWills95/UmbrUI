import pygame
import time

from lib.pygamefb import fbscreen
from lib.network import get_ip
from lib.qr_generator import generate_qr_code

black = (0, 0, 0)
background_color = (247,249,251)
bold_font = 'assets/Roboto-Bold.ttf'
light_font = 'assets/Roboto-Light.ttf'

col1_x = 20
col2_x = 160
col3_x = 301
row1_y = 125
row2_y =  185
row3_y = 245

class UmbrUI(fbscreen):
    def __init__(self):
        # Call parent constructor
        fbscreen.__init__(self)
        
        # Set background color to umbrel
        self.screen.fill(background_color)

        self.init()

        self.add_logo_and_text()
        self.add_qr_code()
        self.build_info_section("admin", get_ip(), (col1_x, row1_y))
        # Tor is always going to be really long so not sure about this one ... :/
        self.build_info_section("tor", "r7cckasdfasfdargsnf4eoxaivgiykmrcglhg4zlwueknhuw66otiid.onion", (160, row1_y))

        self.build_info_section("Max Send", "3M Sats", (col1_x, row2_y))
        self.build_info_section("Max Recieve", "2M Sats", (col2_x, row2_y))
        self.build_info_section("Active Channels", "16", (col3_x, row2_y))
        self.build_info_section("24H Forwards", "53", (col1_x, row3_y))
            
        pygame.display.update() 

    def init(self):
        pygame.init()
        self.titleFont = pygame.font.Font(bold_font, 46)
        self.headingFont = pygame.font.Font(light_font, 12)
        self.textFont = pygame.font.Font(bold_font, 18)

    def add_logo_and_text(self):
        title = self.titleFont.render("umbrel", True, black)

        umbrelImg = pygame.image.load('assets/logo.png')
        # pg.transform.rotozoom(IMAGE, 0, 2)
        umbrelImg = pygame.transform.scale(umbrelImg, (64, 73))
        
        self.screen.blit(umbrelImg, (16, 16))
        self.screen.blit(title, (90, 30))

    def add_qr_code(self):
        qrImg = generate_qr_code(get_ip())
        
        self.screen.blit(qrImg, (360, 16))

    def build_info_section(self, heading, text, position):
        heading = self.headingFont.render(heading, True, black)
        text = self.textFont.render(text, True, black)

        x, y = position
        self.screen.blit(heading, position)
        self.screen.blit(text, (x, y + 20))


# Create an instance of the FBGame class
game = UmbrUI()

while True:
     for event in pygame.event.get():
     
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()
