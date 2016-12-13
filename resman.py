import pygame

class ResourceManager:
    '''
    The resource man(ager). Tracks all the resources and provides
    references to them for all the other classes to use (and draw).
    Must be initialized and linked at the start of the program.
    '''
    def __init__(self):
        initTiles("res/tile_resources.png")

    def init_tiles(self, fn):
        '''
        Initializes self.tiles dictionary for fast lookup of
        tile sprite.
        '''
        # Load tiles
        self.tilesMap = pygame.image.load(fn)

        # Initialize tiles by creating them on the fly
        self.tiles = {}
        for letter in range(ord('A'), ord('Z') + 1):
            t = self.tilesMap.subsurface([0, 0, 50, 50])
            self.tiles[chr(letter)] = t
