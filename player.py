import tile
import resman
import move

class Player:
    '''
    A representation of the player, complete with current score and hand.
    '''
    def __init__(self, pos):
        '''
        Initializes score and hand.
        hand should only have characters (max size 7).
        '''
        self.pos = pos
        self.score = 0
        self.hand = []
        self.currentMove = move.Move()
        self.size = (7 * resman.Tile_Size[0],
                     resman.Tile_Size[1])

    def __contains__(self, pos):
        '''
        Returns true if point is inside player hand rectangle, and false if
        otherwise.
        Uses pygame Rect.collidepoint method to compact code.
        '''
        return pygame.Rect(self.pos, self.size).collidepoint(pos)

    def make_move(self, x, y, letter):
        '''
        Removes tile from hand and places it into active move (and ideally, the
        board).
        '''
        if letter not in self.hand:
            raise Exception("error: cannot move what is not yours")

        self.currentMove.add_move(x, y, letter)

    def takeback_move(self, x, y):
        '''
        Removes tile from active move (placed on board) and replace it back into
        hand.
        '''
        self.hand.append(self.currentMove.remove_move(x, y))

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

    def draw(self, scrn, rman):
        '''
        Draws player's hand
        '''
        for i in range(len(self.hand)):
            scrn.blit(rman.tiles[self.hand[i]],
                      (self.pos[0] + resman.Tile_Size[0] * i,
                       self.pos[1]))
