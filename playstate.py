import state
import resman

class PlayState(state.State):
    '''
    The play state, the state which is shown while the user is
    playing the game, which is, all the time in this prototype.

    Loads everything necessary and starts the game.
    '''
    def __init__(self, ai = False):
        self.ai = ai
        self.rman = resman.ResourceManager()

    def handle(self, evt):
        '''
        Handles all events passed into the state.
        '''
        pass

    def draw(self, scrn):
        '''
        Draws the state onto the screen scrn.
        '''
        if self.ai:
            # Not implemented, so displays NOTHING
            pass
        elif self.rman.finishedLoading:
            '''
            Remove later - this is code for testing the tile surfaces
            '''
            scrn_w = scrn.get_width()
            x, y = 0, 0
            for key, tile in self.rman.tiles.items():
                if x + tile.get_width() > scrn_w:
                    x = 0
                    y += tile.get_height()
                scrn.blit(tile, (x, y))
                x += tile.get_width()

    def update(self, delta):
        '''
        Updates the state as a whole.
        '''
        pass
