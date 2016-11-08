import pygame

class ResourceManager:
    '''
    The resource man(ager). Tracks all the resources and provides
    references to them for all the other classes to use (and draw).
    Must be initialized and linked at the start of the program.
    '''
    def __init__(self):
        initTiles(None)

    def initTiles(self, fn):
        '''
        Initializes self.tiles dictionary for fast lookup of
        tile sprite.
        '''
        pass
