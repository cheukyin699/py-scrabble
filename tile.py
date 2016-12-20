import word_helpers

class Tile:
    def __init__(self, letter):
        '''
        All letters are uppercase
        '''
        self.isblank = letter == " "
        self.letter = letter.toupper()
        self.value = word_helpers.POINTS(letter)

    def draw(self, scrn, pos, rman):
        '''
        '''
        scrn.blit(rman.tiles[self.letter], pos)

class Bonus:
    def __init__(self, b):
        self.b = b

    def draw(self, scrn, pos, rman):
        '''
        '''
        scrn.blit(rman.tiles[self.b], pos)
