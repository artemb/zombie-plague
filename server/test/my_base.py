import unittest
from uuid import uuid4

from game.character import Character
from game.enums import Direction
from game.grid import Grid
from game.player import Player


class MyBaseTestCase():
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.game = None
    #     self.player = None

    def create_player(self):
        return Player(self.game, self.random_string(), self.random_string())

    def create_grid(self, cols=5, rows=5, obstacles=(), walls=()):
        return Grid(cols, rows, list(obstacles), list(walls))

    def create_character(self, grid=None, player_id=None, address=(1, 1), direction=Direction.LEFT, face=None):
        return Character(player_id or self.random_string(), grid or self.create_grid(), face or self.random_string(),
                         address, direction)

    def create_address(self):
        return (1, 1)

    def random_string(self):
        return str(uuid4())
