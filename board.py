import pygame
import colors
import tile
import resman

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
        self.tiles = [[None for _ in range(15)] for __ in range(15)]
        self.rman = rman
        self.size = (15 * resman.Tile_Size[0],
                     15 * resman.Tile_Size[1])
        self.rect = pygame.Rect(self.pos, self.size)

        # Initialize the bonus system
        self.init_bonus("res/board_data.txt")

    def __contains__(self, pos):
        '''
        Returns true if point is inside Scrabble board, and false if otherwise.
        Uses pygame Rect.collidepoint method to compact code.
        '''
        return self.rect.collidepoint(pos)

    def get_tile_pos(self, pos):
        '''
        Returns the 2D indices for position pos. Since the board is of constant
        size, it is assumed that position pos is already inside board. It will
        always return a position, and won't error.
        '''
        # Normalize position
        pos[0] -= self.pos[0]
        pos[1] -= self.pos[1]

        # Calculate integer division
        return (pos[0] // resman.Tile_Size[0],
                pos[1] // resman.Tile_Size[1])

    def get_tile(self, pos):
        '''
        Returns the character on the tile. If it is empty, returns None.
        '''
        ind = self.get_tile_pos(pos)
        return self.tiles[ind[0]][ind[1]]

    def remove_tile(self, pos):
        '''
        Replaces the character at position pos on the board with None value.
        If it is empty (None), it doesn't do a thing.
        '''
        ind = self.get_tile_pos(pos)
        self.tiles[ind[0]][ind[1]] = None

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

    def draw(self, scrn, ms):
        '''
        Draws the scrabble board along with all the tiles.
        If tile is none, draw bonus
        if not, draw tiles (draw tile first, then bonus)
        If there is an active moveset, draws it as well
        '''
        for x in range(len(self.tiles)):
            # Draw the tiles (bonus or bust)
            for y in range(len(self.tiles[x])):
                if self.tiles[x][y] is None:
                    # Draw the bonus if there is no tile
                    self.bonus[x][y].draw(scrn, (x * 50, y * 50), self.rman)
                else:
                    # Draw the tile otherwise
                    scrn.blit(self.rman.tiles[self.tiles[x][y]], (x * 50, y * 50))

        for x, y, l in ms.m:
            scrn.blit(self.rman.tiles[l], (x * 50, y * 50))

        # Draw the lines between the tiles
        for i in range(15):
            pygame.draw.aaline(scrn,
                               colors.BLACK,
                               (0, i * 50),
                               (800, i * 50))
            pygame.draw.aaline(scrn,
                               colors.BLACK,
                               (i * 50, 0),
                               (i * 50, 800))

    def update(self, delta):
        '''
        Updates the scrabble board.
        '''
        pass
