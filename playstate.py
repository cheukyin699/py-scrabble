import state
import resman
import board

class PlayState(state.State):
    '''
    The play state, the state which is shown while the user is
    playing the game, which is, all the time in this prototype.

    Loads everything necessary and starts the game.
    '''
    def __init__(self, rman, ai = False):
        self.ai = ai
        self.rman = rman
        self.board = board.ScrabbleBoard((0, 0), self.rman)

    def handle(self, evt):
        '''
        Handles all events passed into the state.
        '''
        pass

    def draw(self, scrn):
        '''
        Draws the state onto the screen scrn.
        '''
        self.board.draw(scrn)

    def update(self, delta):
        '''
        Updates the state as a whole.
        '''
        pass
