# external imports
import pygame
from pygame.locals import *

# local imports
import pieces
import board


pygame.init()

# "Global" variables
game_over = False
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CHESS")
board = board.Board()
# Game loop
while not game_over:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# helper functions
