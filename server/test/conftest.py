import pytest
from faker import Faker

from game.character import Character
from game.action import Direction
from game.game import Game
from game.grid import Grid
from game.player import Player


class GameFactory:
    def __init__(self):
        self.grid = None
        self.game = None
        self.player = None

    def create_player(self, name=None, id=None):
        self.player = Player(
            id or Faker().pystr(),
            name or Faker().pystr()
        )

        self.game or self.create_game()
        self.game.add_player(self.player)

        return self.player

    def create_grid(self, cols=5, rows=5, obstacles=(), walls=()):
        self.grid = Grid(cols, rows, list(obstacles), list(walls))
        return self.grid

    def create_character(self, player=None, address=(3, 3), direction=Direction.LEFT, face=None):
        if player is None:
            self.player or self.create_player()
            player = self.player

        self.game or self.create_game()

        char = Character(face or Faker().pystr())
        self.game.add_character(char, player)
        char.spawn(address, direction)

        return char

    def create_game(self, grid=None):
        grid or self.grid or self.create_grid()
        self.game = Game(grid or self.grid)
        return self.game


@pytest.fixture
def game_factory():
    return GameFactory()
