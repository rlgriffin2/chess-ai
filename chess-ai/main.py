import pygame
from pygame.locals import *
import sys

from game import Game

pygame.init()
size = (800, 800) # the width must be at least the size of the height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CHESS")
game = Game(screen, size)

def loop():
    while not game.game_over:
        game.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if (__name__ == '__main__'):
    loop()

#TODO:
# ASSIGN LOCATIONS TO SPRITES
# DRAW SPRITES TO SCREEN
# GET THE TEAMS FIGURED OUT
# GET THE SPRITES TO MOVE WHEREVER (AND LOCK INTO SQUARE)
# FIGURE OUT MOVE RULES FOR SPRITE
# DO REST OF CHESS RULES
# AI THE BITCH