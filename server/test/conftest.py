from unittest.mock import Mock

import pytest
from faker import Faker

from game.character import Character
from game.action import Direction
from game.game import Game
from game.grid import Grid
from game.player import Player


class GameFactory:
    def __init__(self, faker):
        self.grid = None
        self.game = None
        self.player = None
        self.faker = faker

    def create_player(self, name=None, id=None):
        self.player = Player(
            id or self.faker.pystr(),
            name or self.faker.pystr()
        )

        self.game or self.create_game()
        self.game.players[self.player.id] = self.player

        return self.player

    def create_grid(self, cols=5, rows=5, obstacles=(), walls=()):
        self.grid = Grid(cols, rows, list(obstacles), list(walls))
        return self.grid

    def create_character(self, player=None, address=(3, 3), direction=Direction.LEFT, face=None):
        if player is None:
            self.player or self.create_player()
            player = self.player

        self.game or self.create_game()

        char = Character(face or self.faker.pystr())
        char.attach_to_player(player)
        self.game.characters[char.char_id] = char
        self.game.turn_manager.characters.append(char)
        char.spawn(self.grid, address, direction)

        return char

    def create_game(self, grid=None):
        grid or self.grid or self.create_grid()
        self.game = Game(grid or self.grid, {}, {})
        return self.game


@pytest.fixture
def game_factory(faker):
    return GameFactory(faker)


class GameFaker:
    def __init__(self, monkeypatch, faker):
        self.monkeypatch = monkeypatch
        self.faker = faker

    def grid(self):
        return Mock()

    def player(self, game=None):
        player = Mock(id=self.faker.pystr())
        if game is not None:
            game.players[player.id] = player
        return player

    def character(self, game=None):
        char = Mock(char_id=self.faker.pystr())
        if game is not None:
            game.characters[char.id] = char
            game.turn_manager.characters.append(char)
        return char

    def turn_manager(self, char=None, remaining_ap=4):
        tm = Mock()
        tm.current_character.return_value = char
        tm.remaining_ap.return_value = remaining_ap
        return tm


@pytest.fixture(scope="session")
def faker():
    return Faker()


@pytest.fixture
def game_faker(monkeypatch, faker):
    return GameFaker(monkeypatch, faker)
