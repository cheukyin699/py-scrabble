from functools import reduce

class Move:
    '''
    A move is an array of formatted tuples:
        (posx, posy, letter)

    This is to simulate the (mostly) multiple tile placings you see in all
    scrabble play. Of course, these moves are constructed on a tile-by-tile
    basis.

    The tuples only include the ones placed by the player, and not the ones that
    are on the board already.
    '''
    def __init__(self):
        self.m = []

    def add_move(self, x, y, letter):
        '''
        Appends the entire thing onto move array. Checks for letters that are in
        the same position.
        '''
        for i, j, l in self.m:
            if i == x and j == y:
                raise Exception("error: attempt to place letter in same position")

        self.m.append((x, y, letter))

    def remove_move(self, x, y):
        '''
        Returns the removed letter
        '''
        rem = None
        for i, j, l in self.m:
            if i == x and j == y:
                # A match!
                rem = (i, j, l)

        if rem is None:
            raise Exception("error: letter doesn't exist and cannot be removed")

        self.m.remove(rem)
        return rem[2]

    def validate(self):
        '''
        Checks to see if the move made by the player is valid.
        Only checks tile placement (vertical or horizontal), and not the words
        itself.

        Returns true if the move is valid in said direction, and false
        otherwise.
        '''
        return self.validate_vertical() or self.validate_horizontal()

    def validate_horizontal(self):
        '''
        Checks to see if the move made by the player is in a horizontal line (y
        coordinates the same).
        
        Returns true if it is, and false otherwise.
        '''
        # Empty/single item in list should always return true
        if len(self.m) <= 1: return True
        acc = reduce(lambda a, b: b if a is True else a[1] == b[1],
                     self.m)
        return bool(acc)

    def validate_vertical(self):
        '''
        Checks to see if the move made by the player is in a vertical line (x
        coordinates the same).
        
        Returns true if it is, and false otherwise.
        '''
        # Empty/single item in list should always return true
        if len(self.m) <= 1: return True
        acc = reduce(lambda a, b: b if a is True else a[0] == b[0],
                     self.m)
        return bool(acc)
