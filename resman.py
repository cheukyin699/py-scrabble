import pygame

class ResourceManager:
    '''
    The resource man(ager). Tracks all the resources and provides
    references to them for all the other classes to use (and draw).
    Must be initialized and linked at the start of the program.
    '''
    def __init__(self):
        self.fonts = {}

        initTiles("res/tile_resources.png")

    def init_tiles(self, fn):
        '''
        Initializes self.tiles dictionary for fast lookup of
        tile sprite.
        '''
        # Load tiles
        self.tilesMap = pygame.image.load(fn)

        # Load fonts (for font writing)
        init_fonts()

        # Initialize tiles by creating them on the fly
        self.tiles = {}
        for letter in range(ord('A'), ord('Z') + 1):
            t = self.tilesMap.subsurface([0, 0, 50, 50])
            self.tiles[chr(letter)] = t

    def init_fonts(self):
        '''
        Load all the fonts into memory.
        '''
        # Lookup table for easy adding/removing
        font_fns = [
            # Used for scrabble tiles
            ('Futura',      'FuturaExtended.ttf'),
            # Used for everything else
            ('OpenSans',    'OpenSans-Regular.ttf')
        ]

        for key, fn in font_fns:
            self.fonts[key] = pygame.font.Font('./res/fonts/' + fn)
