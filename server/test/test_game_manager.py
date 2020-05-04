import unittest
from game.grid import Grid
from game.enums import Direction, Turn, Step
from game.character import Character
from game.grid_def import OBSTACLES, WALLS, rect_obstacle, hwall, vwall
from game.game_manager import GameManager
from game.game import Game
from game.player import Player

class TestGameStructure(unittest.TestCase):

    def test_def(self):
        grid = Grid(5, 5)
        game = Game(grid)
        player = Player(game, '12312', 'Bob')
        player.create_character((5, 5), Direction.LEFT)