import state

class PlayState(state.State):
    '''
    The play state, the state which is shown while the user is
    playing the game, which is, all the time in this prototype.
    '''
    def __init__(self, ai = False):
        self.ai = ai
        pass

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
            # Not implemented, so displays RED
            scrn.fill((200, 0, 0))

    def update(self, delta):
        '''
        Updates the state as a whole.
        '''
        pass
