import pygame
import colors
import word_helpers as wh

Scrabble_Number_Font = "Futura9"
Scrabble_Font = "Futura40"
Tile_Size = (50, 50)
'''
Helps with loading the different fonts and their corresponding sizes.
Format:
    (base_name_of_font,
     font_file_name,
     list_of_font_sizes)
'''
Fonts_Config = [
    # Used for scrabble tiles
    ('Futura',      'FuturaExtended.ttf',       [9, 40]),
    # Used for everything else
    ('OpenSans',    'OpenSans-Regular.ttf',     [50])
]
'''
Helps with loading the different types of board tiles (i.e. where they are on
the tile map).
Format:
    (tile_shortname,
     (x, y, w, h))
'''
Board_Tiles = [
    ('NA', ( 50,  0, 50, 50)),     # Normal tile
    ('MD', (100,  0, 50, 50)),     # That tile in the middle
    ('DL', (150,  0, 50, 50)),     # Double letter
    ('DW', (200,  0, 50, 50)),     # Double word
    ('TL', (250,  0, 50, 50)),     # Triple letter
    ('TW', (300,  0, 50, 50))      # Triple word
]


class ResourceManager:
    '''
    The resource man(ager). Tracks all the resources and provides
    references to them for all the other classes to use (and draw).
    Must be initialized and linked at the start of the program.
    '''
    def __init__(self):
        self.fonts = {}

        self.init_tiles("res/imgs/tile_resources.png")

        self.finishedLoading = True

    def init_tiles(self, fn):
        '''
        Initializes self.tiles dictionary for fast lookup of
        tile surfaces.
        '''
        # Load tiles
        self.tilesMap = pygame.image.load(fn)

        # Load fonts (for font writing)
        self.init_fonts()

        # Loads playable tiles
        self.init_letter_tiles()

        # Loads tiles on the board
        self.init_board_tiles()

    def init_letter_tiles(self):
        # Initialize tiles by creating them on the fly
        self.tiles = {}
        for letter in range(ord('A'), ord('Z') + 1):
            # First tile, 50x50
            t = self.tilesMap.subsurface(
                    [0, 0,
                     Tile_Size[0], Tile_Size[0]]).copy()

            # Render letter
            letter_s = self.fonts[Scrabble_Font].render(
                                chr(letter),
                                True,
                                colors.BLACK)
            # Position letter in the middle of the tile
            letter_sx = (Tile_Size[0] - letter_s.get_width())  / 2
            letter_sy = (Tile_Size[1] - letter_s.get_height()) / 2

            # Render score on the letter
            num_s = self.fonts[Scrabble_Number_Font].render(
                                str(wh.POINTS[chr(letter)]),
                                False,
                                colors.BLACK)
            # Position score on the bottom right of the tile
            # Adds 2px of padding on each side
            num_sx = Tile_Size[0] - num_s.get_width()  - 2
            num_sy = Tile_Size[1] - num_s.get_height() - 2

            t.blit(letter_s, (letter_sx, letter_sy))
            t.blit(num_s, (num_sx, num_sy))
            self.tiles[chr(letter)] = t

    def init_fonts(self):
        '''
        Load all the fonts into memory.
        '''
        for key, fn, sizes in Fonts_Config:
            for size in sizes:
                self.fonts[key + str(size)] = pygame.font.Font('./res/fonts/' + fn, size)

    def init_board_tiles(self):
        pass
