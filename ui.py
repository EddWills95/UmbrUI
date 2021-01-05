import os
import pygame
import time
import random

from lib import pygamefb

class UmbrUI(pygamefb.fbgame):
    def test(self):
        # Fill the screen with red (255, 0, 0)
        red = (255, 0, 0)
        self.screen.fill(red)
        # Update the display
        pygame.display.update()

# Create an instance of the FBGame class
game = UmbrUI()
game.test()
time.sleep(10)