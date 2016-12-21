import tile

class Player:
    '''
    A representation of the player, complete with current score and hand.
    '''
    def __init__(self):
        '''
        Initializes score and hand.
        hand should only have characters (max size 7).
        '''
        self.score = 0
        self.hand = []

    def deck_draw(self, deck, n):
        '''
        Draws n tiles from deck
        '''
        self.hand.extend(deck.take(n))

    def draw(self, scrn, pos, rman):
        '''
        Draws player's hand
        '''
        for i in range(len(self.hand)):
            scrn.blit(rman.tiles[self.hand[i]],
                      (pos[0] + 50 * i, pos[1]))
