import pygame
import cv2

class Piece():

    def __init__(self, coord, img_name, locations, square_size):
        # doesn't really make sense to have a piece variable for board locations, but don't want to keep passing it in
        self.board_locations = locations 
        self.coord = coord
        self.location = self.board_locations[coord]
        self.moves = []
        self.captured = False
        self.value = 0
        proc_img_name = self.process_sprites(img_name, square_size)
        self.img = pygame.image.load(proc_img_name)
        self.moved = True

    def update(self, surface):
        # put the move check and stuff here
        # trying to center the piece a little better
        if self.moved:
            self.location = (self.location[0], self.location[1]-10)
            self.moved = False
        self.draw(surface)

    def draw(self, surface):
        surface.blit(self.img, self.location)

    def process_sprites(self, img_name, square_size):
        src = cv2.imread(img_name, cv2.IMREAD_UNCHANGED)
        scale = .8 + .2 # add .2 to whatever scale user wants because image has some blank space around actual sprite
        width = int(square_size * scale)
        height = int(square_size * scale)
        output = cv2.resize(src, (width, height))
        new_name = img_name.replace('orig', 'temp') # swap out 'orig' with 'temp'
        cv2.imwrite(new_name, output)
        return new_name
       

class Pawn(Piece):

    def __init__(self):
        self.value = 1

class King(Piece):

    def __init__(self):
        self.value = 20

class Queen(Piece):

    def __init__(self):
        self.value = 9

class Knight(Piece):

    def __init__(self):
        self.value = 3

class Bishop(Piece):

    def __init__(self):
        self.value = 3

class Rook(Piece):

    def __init__(self):
        self.value = 5
