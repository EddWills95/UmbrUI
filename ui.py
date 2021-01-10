# Libraries provided by the system
import pygame
import time

from lib.pygamefb import fbscreen
from lib.network import get_ip
from lib.qr_generator import generate_qr_code

from consts import black, background_color, bold_font, light_font, columns_x, rows_y

class UmbrUI(fbscreen):
    def __init__(self):
        # Call parent constructor
        fbscreen.__init__(self)
        
        # Set background color to umbrel
        self.screen.fill(background_color)

        self.init()

        self.add_logo_and_text()
        self.add_qr_code()
        self.build_info_section("admin", get_ip(), (300, 120), False, True)
        # Tor is always going to be really long so not sure about this one ... :/
        self.build_info_section("tor", "r7cckasdfasfdargsnf4eoxaivgiykmrcglhg4zlwueknhuw66otiid.onion", (columns_x[0], rows_y[0]), 
        pygame.font.Font(bold_font, 22))

        self.build_info_section("Max Send", "3M Sats", (columns_x[0], rows_y[1]))
        self.build_info_section("Max Recieve", "2M Sats", (columns_x[1], rows_y[1]))
        self.build_info_section("Active Channels", "16", (columns_x[2], rows_y[1]))
        self.build_info_section("24H Forwards", "53", (columns_x[0], rows_y[2]))
            
        pygame.display.set_caption("UmbrUI")
        pygame.display.update() 

    def init(self):
        pygame.init()
        self.titleFont = pygame.font.Font(bold_font, 56)
        self.headingFont = pygame.font.Font(light_font, 18)
        self.textFont = pygame.font.Font(bold_font, 32)

    def add_logo_and_text(self):
        title = self.titleFont.render("umbrel", True, black)

        umbrelImg = pygame.image.load('assets/logo.png')
        # pg.transform.rotozoom(IMAGE, 0, 2)
        umbrelImg = pygame.transform.scale(umbrelImg, (88, 100))
        
        self.screen.blit(umbrelImg, (16, 16))
        self.screen.blit(title, (110, 30))

    def add_qr_code(self):
        qrImg = generate_qr_code(get_ip())
        
        self.screen.blit(qrImg, (544, 16))

    def build_info_section(self, heading, text, position, textfont=False, alignRight=False):
        if(textfont == False):
            textfont = self.textFont
        heading = self.headingFont.render(heading, True, black)
        text = textfont.render(text, True, black)

        x, y = position
        headingPosition = position
        textPosition = (x, y + 25)
        if(alignRight):
            headingSize = heading.get_width()
            textSize = text.get_width()
            if(headingSize < textSize):
                headingPosition = (x + textSize - headingSize, y)
            else:
                textPosition =  (x + headingSize - textSize, y + 25)
        self.screen.blit(heading, headingPosition)
        self.screen.blit(text, textPosition)


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
 
    time.sleep(2)
    # Draws the surface object to the screen.
    pygame.display.update()
