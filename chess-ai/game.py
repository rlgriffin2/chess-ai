# local imports
import pieces
import board
from pathlib import Path

class Game():

    def __init__(self, surface, size):
        self.surface = surface
        self.size = size
        self.game_over = False
        self.board = board.Board(size)
        self.pieces = []
        # the code below is for creating pieces, was most pythonic way of doing it I could think of, still somewhat repetitive
        piece_sprite_dir = Path('piece_sprites/orig')
        for p in piece_sprite_dir.iterdir():
            p = str(p)
            coords = []
            img_file = ''
            if 'white_rook' in p:
                coords = ['a1', 'h1']
                img_file = p
            if 'white_knight' in p:
                coords = ['b1', 'g1']
                img_file = p
            if 'white_bishop' in p:
                coords = ['c1', 'f1']
                img_file = p
            if 'white_queen' in p:
                coords = ['d1']
                img_file = p
            if 'white_king' in p:
                coords = ['e1']
                img_file = p
            if 'white_pawn' in p:
                coords = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
                img_file = p
            if 'black_rook' in p:
                coords = ['a8', 'h8']
                img_file = p
            if 'black_knight' in p:
                coords = ['b8', 'g8']
                img_file = p
            if 'black_bishop' in p:
                coords = ['c8', 'f8']
                img_file = p
            if 'black_queen' in p:
                coords = ['d8']
                img_file = p
            if 'black_king' in p:
                coords = ['e8']
                img_file = p
            if 'black_pawn' in p:
                coords = ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
                img_file = p
            for c in coords:
                self.pieces.append(pieces.Piece(c, img_file, self.board.locations, board.Square.size))
                '''

    def draw(self):
        self.board.draw(self.surface)
        for piece in self.pieces:
            piece.update(self.surface)
