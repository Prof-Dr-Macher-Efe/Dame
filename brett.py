import pygame 
from Main import *
from Konstanten import *
from Slavencoins import *

class Brett:
    def __init__(self, board_size, window_width, window_height, bg):
        self.board_size    = board_size
        self.window_width  = window_width
        self.window_height = window_height
        self.bg            = bg
        self.config()

    def setup(self):
        self.config = [
          ['', 'bp', '', 'bp', '', 'bp', '', 'bp'],
          ['bp', '', 'bp', '', 'bp', '', 'bp', ''],
          ['', 'bp', '', 'bp', '', 'bp', '', 'bp'],
          ['', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', ''],
          ['rp', '', 'rp', '', 'rp', '', 'rp', ''],
          ['', 'rp', '', 'rp', '', 'rp', '', 'rp'],
          ['rp', '', 'rp', '', 'rp', '', 'rp', '']]
        

bg = pygame.image.load("Images/brett.png")




running = True
while running:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_ESCAPE:
               running = False

    pygame.display.update()

pygame.quit()

    