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
        self.p1 = player.Player((0, 750))
        self.p2 = player.Player((0, 750))
        self.deck = deck.Deck()
        self.turn = "1"             # Player 1 always goes first
        self.selectedTile = None    # Selected tile should be a letter only

        # Place players into dictionary for less if-statements
        self.players = {"1": p1, "2": p2}

        # First, draw 7 tiles
        self.p1.deck_draw(self.deck, 7)
        self.p2.deck_draw(self.deck, 7)

    def handle(self, evt):
        '''
        Handles all events passed into the state.
        '''
        if evt.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos in self.board:
                if self.selectedTile is None:
                    # Adds cursor onto board
                    # Rotates cursor if needed
                    # TODO
                    pass
                else:
                    # Places selected tile into moveset, and thus, places tile
                    # onto board
                    # TODO
                    pass
            elif pos in self.players[self.turn]:
                if self.selectedTile is None:
                    # Select tile, and remove from correct hand
                    self.handle_hand_select(pos)
                else:
                    # Replaces removed tile from hand
                    self.handle_hand_replace()

    def handle_hand_replace(self):
        '''
        Handles the replacing of selected tile into hand.
        '''
        # Places tile into hand
        self.players[self.turn].hand.append(self.selectedTile)

        # Removes selected tile
        self.selectedTile = None

    def handle_hand_select(self, pos):
        '''
        Handles the tile selection and removal (from the corresponding hand, of
        course).
        '''
        # Grab tile from hand

        # Place tile into tile selection

        # Removes tile from hand
        pass

    def draw(self, scrn):
        '''
        Draws the state onto the screen scrn.
        '''
        self.board.draw(scrn)

        if self.turn == "1":
            self.p1.draw(scrn, self.rman)
        else:
            self.p2.draw(scrn, self.rman)

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
