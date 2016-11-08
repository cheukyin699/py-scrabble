class ScrabbleBoard:
    '''
    A snug little scrabble board class that stores information about
    the bonus system, the tiles currently on the board, and if a move
    is valid or not.
    '''
    def __init__(self, pos):
        self.pos = pos
        self.tiles = [[None] * 15] * 15

        # Initialize the bonus system
        # TODO
        self.bonus = None

    def handle(self, evt):
        '''
        Handles all events, like dragging of tiles and typing.
        '''
        pass

    def draw(self, scrn):
        '''
        Draws the scrabble board along with all the tiles.
        Zip and check for Nones
        If tile is none, draw bonus
        if not, draw tiles (draw tile first, then bonus)
        '''
        for y in range(len(self.tiles)):
            zipped = zip(self.tiles[y], self.bonus[y])
            for x in range(len(zipped)):
                if zipped[x][0] is None:
                    zipped[x][1].draw(scrn, x * 16, y * 16)
                else:
                    zipped[x][0].draw(scrn, x * 16, y * 16)

    def update(self, delta):
        '''
        Updates the scrabble board.
        '''
        pass
