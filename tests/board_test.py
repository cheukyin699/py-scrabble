import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from board import *
from move import *

class ScrabbleBoardTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b = ScrabbleBoard((0,0), None)

    def testFindConnectedWords(self):
        validms = Move()
        validms.m = [(7, 6, 'A'),
                     (7, 7, 'B'),
                     (7, 8, 'A')]
        validms_answer = [((7, 6), 'ABA', (7, 8))]
        # A standard test with a standard word
        self.assertEqual(self.b.find_connected_words(validms),
                         validms_answer)

        validms_answer = [((7, 6), 'ABA', (7, 8)),
                          ((7, 6), 'AA',  (8, 6)),
                          ((7, 7), 'BA',  (8, 7))]
        self.b.tiles[8][6] = 'A'
        self.b.tiles[8][7] = 'A'
        # A standard test with actual things on the board
        self.assertSetEqual(set(self.b.find_connected_words(validms)),
                            set(validms_answer))

