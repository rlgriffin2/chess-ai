import pygame
class Square():
    size = 0

    def __init__(self, coord, board_width):
        Square.size = board_width/8
        self.coord = coord
        # this is how we make the board checkered
        # because 'a' in ascii is odd, and so is '1', if you add them, they are an even number
        # so because of the incrementation of letters and numbers on the board,
        # the modulus sum of the asci values for the letter and number of the coordinate makes a checker pattern
        sum_ascii = ord(self.coord[0]) + ord(self.coord[1])
        if sum_ascii%2 != 0:
            self.color = (0, 200,255)
        else:
            self.color = (0, 0, 150)


class Board():

    def __init__(self, size):
        # this is a list of the board coordinates like "a1", "b5", etc.
        self.coords = [] 
        # this is a dict of the board coords with matching locations for where we should draw the rect for that coord
        self.locations = {} 
        nums = ['1', '2', '3', '4', '5', '6', '7', '8']
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for num in nums:
            for char in chars:
                entry = char + num
                self.coords.append(entry)
        self.squares = self.create_squares(size[0]) # pass in the width for the board so squares can divide it
        width = size[0]
        height = size[1]
        x = 0
        y = height - Square.size
        for coord in self.coords:
            # starting position is x = 0, y = height-size.
            # then we increment x by size until we hit width, then switch x back to 0 and have y = height - size*2
            self.locations[coord] = (x, y)
            if (x==width - Square.size):
                x = 0
                y -= Square.size
            else:
                x += Square.size
            
    def create_squares(self, board_width):
        i = 0
        squares=[]
        for coord in self.coords:
            squares.append(Square(coord, board_width))
            i+=1
        return squares

    def message_display(self, text, x, y, surface):
        font = pygame.font.Font('freesansbold.ttf', 16)
        text_surf = font.render(text, True, (0, 0, 0))
        text_rect = text_surf.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surf, text_rect)

    def draw(self, surface):
        # if we want to make borders and such, put them here
        for square in self.squares:
            pygame.draw.rect(surface, square.color, (self.locations[square.coord][0], self.locations[square.coord][1], Square.size, Square.size))
            self.message_display(square.coord, self.locations[square.coord][0] + Square.size/2, self.locations[square.coord][1] + Square.size - 10, surface)
