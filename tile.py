import word_helpers

class Tile:
    def __init__(self, letter):
        '''
        All letters are uppercase
        '''
        self.isblank = letter == " "
        self.letter = letter.toupper()
        self.value = word_helpers.POINTS(letter)

    def draw(self, scrn, x, y):
        '''
        Draws the tile at specific x and y coordinates on the screen
        scrn.
        '''
        pass
