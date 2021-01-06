import pygame
import time

from lib.pygamefb import fbscreen

black = (0, 0, 0)

class UmbrUI(fbscreen):
    def __init__(self):
        # Call parent constructor
        fbscreen.__init__(self)
        
        # Set background color to umbrel
        backgroundColor = (247,249,251)
        self.screen.fill(backgroundColor)

        self.init()

        self.add_logo_and_text()

        pygame.display.update() 

    def init(self):
        pygame.init()
        self.titleFont = pygame.font.Font('Roboto-Bold.ttf', 46)
        self.textFont = pygame.font.Font('Roboto-Bold.ttf', 18)

    def add_logo_and_text(self):
        title = self.titleFont.render("umbrel", True, black)

        umbrelImg = pygame.image.load('assets/logo.png')
        # pg.transform.rotozoom(IMAGE, 0, 2)
        umbrelImg = pygame.transform.scale(umbrelImg, (64, 73))
        
        self.screen.blit(umbrelImg, (16, 16))
        self.screen.blit(title, (90, 30))

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
