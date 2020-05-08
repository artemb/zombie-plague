import unittest

from game.enums import Direction
from game.game import Game
from game.grid import Grid
from game.player import Player


class TestGameStructure(unittest.TestCase):

    def test_def(self):
        grid = Grid(5, 5)
        game = Game(grid)
        player = Player(game, '12312', 'Bob')
        player.create_character((5, 5), Direction.LEFT, 'char1')
