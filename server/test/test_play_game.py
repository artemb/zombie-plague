import pytest
from faker import Faker

from game.action import Direction, ActionType, Step, Turn
from game.character import ActionNotAllowedError, Character
from game.game import Game
from game.grid import Grid
from game.player import Player


def test_play(game_factory, faker):
    game = Game(Grid(20, 20))

    player1 = Player(faker.pystr(), faker.name())
    player2 = Player(faker.pystr(), faker.name())

    game.add_player(player1)
    game.add_player(player2)

    char1 = Character(faker.pystr())
    char2 = Character(faker.pystr())

    game.add_character(char1, player1)
    game.add_character(char2, player2)

    char1.spawn((1, 1), Direction.DOWN)
    char2.spawn((1, 2), Direction.UP)

    with pytest.raises(ActionNotAllowedError):
        game.action(char1, ActionType.STEP, step=Step.FORWARD)

    game.action(char1, ActionType.TURN, turn=Turn.LEFT)
    game.action(char1, ActionType.STEP, step=Step.FORWARD)
    game.action(char1, ActionType.STEP, step=Step.FORWARD)
    game.action(char1, ActionType.TURN, turn=Turn.LEFT)

    assert game.turn_manager.current_character() == char2
    assert game.characters[char1.char_id].address == (3, 1)
    assert game.characters[char1.char_id].direction == Direction.UP
