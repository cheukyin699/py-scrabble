import state
import resman
import board
import player
import deck
import pygame

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
        self.p1 = player.Player()
        self.p2 = player.Player()
        self.deck = deck.Deck()
        self.turn = "1"             # Player 1 always goes first
        self.selectedTile = None    # Selected tile should be a letter only

        # First, draw 7 tiles
        self.p1.deck_draw(self.deck, 7)
        self.p2.deck_draw(self.deck, 7)

    def handle(self, evt):
        '''
        Handles all events passed into the state.
        '''
        if self.selectedTile is not None:
            # Tile is selected and should hang onto the mouse
            pass

    def draw(self, scrn):
        '''
        Draws the state onto the screen scrn.
        '''
        self.board.draw(scrn)

        if self.turn == "1":
            self.p1.draw(scrn, (0, 750), self.rman)
        else:
            self.p2.draw(scrn, (0, 750), self.rman)

        if self.selectedTile is not None:
            # Tile is selected and should hang onto the mouse
            x, y = pygame.mouse.get_pos()
            scrn.blit(self.rman.tiles[self.selectedTile],
                      (x - resman.Tile_Size[0] / 2,
                       y - resman.Tile_Size[1] / 2))

    def update(self, delta):
        '''
        Updates the state as a whole.
        '''
        pass
