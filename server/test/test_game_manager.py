from unittest.mock import patch, Mock

import pytest

from game.action import Step, ActionType
from game.character import ActionNotAllowedError
from game.game import Game, Lobby, GameStartedError, UnknownPlayerError
from game.game_manager import GameManager


@pytest.fixture
def mgr():
    return GameManager()


def test_lobby_init(mgr):
    assert mgr.game is None
    assert mgr.lobby is not None


# def test_game_init(mgr):
#     assert mgr.game is not None


def test_register_player_lobby(mgr, mocker, faker):
    id = faker.pystr()
    name = faker.pystr()

    mocker.patch.object(Lobby, 'register_player')

    mgr.register_player(id, name)

    Lobby.register_player.assert_called_once()


def test_register_player_started(mgr, mocker, faker):
    id, name = faker.pystr(), faker.pystr()
    mgr.game = Mock()  # as if the game is already started

    with pytest.raises(GameStartedError):
        mgr.register_player(id, name)


def test_is_registered_lobby(mgr, monkeypatch, faker):
    player_id = faker.pystr()
    assert not mgr.is_player_registered(player_id)

    mgr.lobby.players = {player_id: Mock()}

    assert mgr.is_player_registered(player_id)


def test_is_registered_game(mgr, faker):
    mgr.game = Mock()
    mgr.game.get_player.side_effect = UnknownPlayerError()

    assert not mgr.is_player_registered(faker.pystr())

    mgr.game.get_player.reset_mock(side_effect=True)
    mgr.game.get_player.return_value = Mock()

    assert mgr.is_player_registered(faker.pystr())


def test_action(mgr, faker):
    char = Mock()

    mgr.game = Mock()
    mgr.game.get_character.return_value = char

    mgr.action(faker.pystr(), 'STEP', {'step': 'FORWARD'})
    mgr.game.action.assert_called_once_with(char, ActionType.STEP, step=Step.FORWARD)


def test_action_not_allowed(mgr, faker):
    mgr.game = Mock()
    mgr.game.action.side_effect = ActionNotAllowedError()

    mgr.action(faker.pystr(), 'STEP', {'step': 'FORWARD'})
    # Will pass if no exception was raised


def test_state(mgr):
    expected = Mock()
    mgr.game = Mock()
    mgr.game.state.return_value = expected

    assert mgr.state() == expected
