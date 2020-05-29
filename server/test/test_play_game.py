import pytest
from faker import Faker

from game.action import Direction, ActionType, Step, Turn
from game.character import ActionNotAllowedError, Character
from game.game import Game, Lobby
from game.grid import Grid
from game.player import Player


def test_play(game_factory, faker):
    lobby = Lobby()


    player1 = Player(faker.pystr(), faker.name())
    player2 = Player(faker.pystr(), faker.name())

    lobby.register_player(player1)
    lobby.register_player(player2)

    char1 = lobby.create_character()
    char2 = lobby.create_character()

    lobby.assign_character(player1, char1)
    lobby.assign_character(player2, char2)

    game = lobby.start_game(Grid(20, 20))

    char1.spawn(game.grid, (1, 1), Direction.DOWN)
    char2.spawn(game.grid, (1, 2), Direction.UP)

    with pytest.raises(ActionNotAllowedError):
        game.action(char1, ActionType.STEP, step=Step.FORWARD)

    game.action(char1, ActionType.TURN, turn=Turn.LEFT)
    game.action(char1, ActionType.STEP, step=Step.FORWARD)
    game.action(char1, ActionType.STEP, step=Step.FORWARD)
    game.action(char1, ActionType.TURN, turn=Turn.LEFT)

    assert game.turn_manager.current_character() == char2
    assert game.characters[char1.char_id].address == (3, 1)
    assert game.characters[char1.char_id].direction == Direction.UP
