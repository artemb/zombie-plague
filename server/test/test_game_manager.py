from unittest.mock import patch

import pytest

from game.action import Step, ActionType
from game.game import Game
from game.game_manager import GameManager


@pytest.fixture
def mgr():
    return GameManager()


def test_game_init(mgr):
    assert mgr.game is not None


def test_register_player(mgr, mocker, faker):
    id = faker.pystr()
    name = faker.pystr()

    mocker.patch.object(Game, 'add_player')

    mgr.register_player(id, name)

    Game.add_player.assert_called_once()


def test_is_registered(mgr, monkeypatch, faker):
    player_id = faker.pystr()
    assert not mgr.is_player_registered(player_id)

    monkeypatch.setattr(mgr.game, 'players', {player_id: faker.pydict()})

    assert mgr.is_player_registered(player_id)


def test_action(mgr, mocker, monkeypatch, faker):
    char_id = faker.pystr()
    char = faker.pydict()
    monkeypatch.setattr(mgr.game, 'characters', {char_id: char})
    mocker.patch.object(Game, 'action')
    mgr.action(char_id, 'STEP', {'step': 'FORWARD'})
    Game.action.assert_called_once_with(char, ActionType.STEP, step=Step.FORWARD)


def test_state(game_factory, faker):
    mgr = GameManager()

    expected = faker.pydict()
    with patch.object(Game, 'state', return_value=expected):
        state = mgr.state()

    assert state == expected
