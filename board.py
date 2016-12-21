import pygame
import colors
import tile

class ScrabbleBoard:
    '''
    A snug little scrabble board class that stores information about
    the bonus system, the tiles currently on the board, and if a move
    is valid or not.
    '''
    def __init__(self, pos, rman):
        '''
        Initializes positions, tiles, and bonuses. Tiles have tile items,
        whereas bonuses have surfaces as items.
        '''
        self.pos = pos
        self.tiles = [[None] * 15] * 15
        self.rman = rman

        # Initialize the bonus system
        self.init_bonus("res/board_data.txt")

    def init_bonus(self, fn):
        '''
        Initializes bonuses using the file.
        '''
        self.bonus = [[]]
        f = open(fn, 'r')
        for line in f.readlines():
            for sym in line.rstrip().split():
                self.bonus[-1].append(tile.Bonus(sym))
            self.bonus.append([])

        f.close()

    def place(self, pos, letter):
        '''
        Converts letter to be placed into tile.Tile type.
        '''
        x, y = pos
        if self.tiles[x][y] is not None:
            raise Exception("error: tile exists")

        self.tiles[x][y] = tile.Tile(letter)

    def take_back(self, pos):
        '''
        Removes letter and returns it.
        '''
        x, y = pos
        t = self.tiles[x][y]

        if t is None:
            raise Exception("error: tile doesn't exist")

        self.tiles[x][y] = None
        return t

    def handle(self, evt):
        '''
        Handles all events, like dragging of tiles and typing.
        '''
        pass

    def draw(self, scrn):
        '''
        Draws the scrabble board along with all the tiles.
        Zip and check for Nones
        If tile is none, draw bonus
        if not, draw tiles (draw tile first, then bonus)
        '''
        for y in range(len(self.tiles)):
            # Draw the tiles (bonus or bust)
            zipped = list(zip(self.tiles[y], self.bonus[y]))
            for x in range(len(zipped)):
                if zipped[x][0] is None:
                    # Draw the bonus if necessary
                    zipped[x][1].draw(scrn, (x * 50, y * 50), self.rman)
                else:
                    # Draw the tile otherwise
                    zipped[x][0].draw(scrn, (x * 50, y * 50), self.rman)
            # Draw the lines between the tiles
            pygame.draw.aaline(scrn,
                               colors.BLACK,
                               (0, y * 50),
                               (800, y * 50))
        # Draw the lines between the tiles
        for i in range(15):
            pygame.draw.aaline(scrn,
                               colors.BLACK,
                               (i * 50, 0),
                               (i * 50, 800))

    def update(self, delta):
        '''
        Updates the scrabble board.
        '''
        pass
