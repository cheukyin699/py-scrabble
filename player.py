import tile
import resman

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

    def deck_exchange(self, deck, l):
        '''
        Exchanges tiles in hand (list l) with random tiles in deck.
        First checks to see that the list is a subset of hand.
        '''
        if not all(map(lambda i: i in self.hand, l)):
            raise Exception("error: cannot exchange non-existant tiles")

        deck.place(l)

        for i in l:
            self.hand.remove(i)

    def draw(self, scrn, pos, rman):
        '''
        Draws player's hand
        '''
        for i in range(len(self.hand)):
            scrn.blit(rman.tiles[self.hand[i]],
                      (pos[0] + resman.Tile_Size[0] * i,
                       pos[1]))
