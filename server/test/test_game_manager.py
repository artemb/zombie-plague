from unittest.mock import patch

import pytest
from faker import Faker

from game.game import Game
from game.game_manager import GameManager
from test.my_base import MyBaseTestCase


@pytest.fixture
def mgr():
    return GameManager()


def test_game_init(mgr):
    assert mgr.game is not None


def test_register_player(mgr, mocker):
    id = Faker().pystr()
    name = Faker().pystr()

    mocker.patch.object(Game, 'add_player')

    mgr.register_player(id, name)

    Game.add_player.assert_called_once()


def test_state(game_factory):
    mgr = GameManager()

    expected = Faker().pydict()
    with patch.object(Game, 'state', return_value=expected):
        state = mgr.state()

    assert state == expected
