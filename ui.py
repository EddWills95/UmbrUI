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
    loaded = False

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

    def build_info_section(self, heading_text, text_text, position):
        heading_surf, heading_rect = self.headingFont.render(heading_text, black)
        text_surf, text_rect = self.textFont.render(text_text, black)

        x, y = position
        self.screen.blit(heading_surf, position)
        self.screen.blit(text_surf, (x, y + 25))
        pygame.display.update()

    def save_screenshot(self):
        pygame.display.flip() 
        pygame.image.save(self.screen, "/usr/screenshots/UmbrUI.png")
        

# Create an instance of the FBGame class
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
