class Square():

    def __init__(self, coord, color):
        self.coord = coord
        if color == 'light':
            self.color = (0, 200,255)
        else:
            self.color = (0, 0, 150)

    def draw(self, surface):
        pygame.draw.rect(surface,self.color,(200,150,100,50))

class Board():

    def __init__(self):
        self.squares = create_squares()

    def create_squares():
        i = 0
        while i<64:
            if i%2 == 0:
                color = 'light'
            else:
                color = 'dark'
            self.squares[i] = Square('a1', color)
            i++

    # for the coords, set up a dict and make it with for num 1-8, for a-h
    def draw(self, surface):
        # if we want to make borders and such, put them here
        self.squares.draw(surface)
