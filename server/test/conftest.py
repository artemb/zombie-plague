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

    def create_player(self):
        self.player = Player(self.game or self.create_game(), Faker().pystr(), Faker().pystr())
        return self.player

    def create_grid(self, cols=5, rows=5, obstacles=(), walls=()):
        self.grid = Grid(cols, rows, list(obstacles), list(walls))
        return self.grid

    def create_character(self, player_id=None, address=(1, 1), direction=Direction.LEFT, face=None):
        if player_id is None:
            self.player or self.create_player()
            player_id = self.player.id

        self.grid or self.create_grid()

        return Character(player_id, self.grid, face or Faker().pystr(),
                         address, direction)

    def create_game(self, grid=None):
        self.game = Game(grid or self.create_grid())
        return self.game


@pytest.fixture
def game_factory():
    return GameFactory()
