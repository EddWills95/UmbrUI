import pygame
import pygame.freetype
import time

from lib.pygamefb import fbscreen
from lib.network import get_ip
from lib.qr_generator import generate_qr_code

black = (0, 0, 0)
background_color = (247,249,251)
bold_font = 'assets/Roboto-Bold.ttf'
light_font = 'assets/Roboto-Light.ttf'
screenshot_location = '/usr/screenshots/UmbrUI.png'

col1_x = 20
col2_x = 240
col3_x = 480
row1_y = 185
row2_y = 280
row3_y = 375

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
        self.build_info_section("tor", "r7cckasdfasfdargsnf4eoxaivgiykmrcglhg4zlwueknhuw66otiid.onion", (col2_x, row1_y))

        self.build_info_section("Max Send", "3M Sats", (col1_x, row2_y))
        self.build_info_section("Max Recieve", "2M Sats", (col2_x, row2_y))
        self.build_info_section("Active Channels", "16", (col3_x, row2_y))
        self.build_info_section("24H Forwards", "53", (col1_x, row3_y))
            
        pygame.display.set_caption("UmbrUI")
        pygame.display.update() 

    def init(self):
        pygame.init()
        self.titleFont = pygame.freetype.Font(bold_font, 56)
        self.headingFont = pygame.freetype.Font(light_font, 18)
        self.textFont = pygame.freetype.Font(bold_font, 32)

    def add_logo_and_text(self):
        title = self.titleFont.render_to(self.screen, "umbrel", (110, 30))

        umbrelImg = pygame.image.load('assets/logo.png')
        # pg.transform.rotozoom(IMAGE, 0, 2)
        umbrelImg = pygame.transform.scale(umbrelImg, (88, 100))
        
        self.screen.blit(umbrelImg, (16, 16))
        # self.screen.blit(title, (110, 30))

    def add_qr_code(self):
        qrImg = generate_qr_code(get_ip())
        
        self.screen.blit(qrImg, (544, 16))

    def build_info_section(self, heading, text, position):
        heading = self.headingFont.render(heading)
        text = self.textFont.render(text)
        # self.screen.draw.text(heading, position)
        # self.screen.draw.text()

        x, y = position
        self.screen.blit(heading, position)
        self.screen.blit(text, (x, y + 25))
        pygame.display.flip()

    def save_screenshot(self):
        pygame.display.flip() 
        pygame.image.save(self.screen, "/usr/screenshots/UmbrUI.png")
        

# Create an instance of the FBGame class
game = UmbrUI()

while True:
    print('Printing image')
    game.save_screenshot()
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
