from unittest.mock import patch, Mock

import pytest

from game.action import ActionType, StepAction, Direction, Step
from game.character import Character, ActionNotAllowedError
from game.game import NotCharactersTurnError, NotEnoughAPError, UnknownPlayerError, \
    UnknownCharacterError, Game
from game.grid import Grid
from game.player import Player
from game.turns import TurnManager


@pytest.fixture
def game(game_factory):
    return game_factory.create_game()


def test_game_has_turns(game):
    assert game.turn_manager is not None


def test_game_adds_characters_to_turn_manager(game_faker, game_factory):
    char = game_faker.character()
    char2 = game_faker.character()

    with patch.object(TurnManager, '__init__', return_value=None) as mock:
        Game(game_factory.create_grid(), {}, {char.id: char, char2.id: char2})

    mock.assert_called_once_with(4, [char, char2])


def test_state_players(game, game_factory, faker, game_faker):
    player1 = game_faker.player(game)
    player2 = game_faker.player(game)

    expected = faker.pydict()
    player1.state.return_value = expected
    player2.state.return_value = expected

    state = game.state()

    assert 'players' in state
    assert len(state['players']) == 2
    assert player1.id in state['players']
    assert player2.id in state['players']

    player1.state.assert_called_once()
    player2.state.assert_called_once()
    assert state['players'][player1.id] == expected
    assert state['players'][player2.id] == expected


def test_state_grid(game, faker):
    expected = faker.pydict()
    with patch.object(Grid, 'state', return_value=expected) as mock:
        state = game.state()

    assert 'grid' in state
    assert state['grid'] == expected


def test_state_turns(game, faker):
    expected = faker.pydict()
    with patch.object(TurnManager, 'state', return_value=expected):
        state = game.state()

    assert 'turn' in state
    assert state['turn'] == expected


def test_action(game, game_faker, mocker):
    char = game_faker.character(game)
    mocker.patch.object(StepAction, 'run')

    game.action(char, ActionType.STEP, mock_param='mock_value')

    ActionType.STEP.action.run.assert_called_once_with(char, mock_param='mock_value')


def test_action_controls_turns(game, mocker, game_faker):
    char1 = game_faker.character(game)
    char2 = game_faker.character(game)

    st = mocker.patch.object(StepAction, 'run')

    # Testing character who's turn it is
    game.action(char1, ActionType.STEP, step=Step.FORWARD)
    st.assert_called_once()
    st.reset_mock()

    # Testing character who's turn it's not
    with pytest.raises(NotCharactersTurnError):
        game.action(char2, ActionType.STEP, step=Step.FORWARD)

    st.assert_not_called()


def test_action_deducts_ap(game, game_faker, monkeypatch):
    char = game_faker.character(game)

    monkeypatch.setattr(ActionType.STEP.action, 'ap', 3)

    assert game.turn_manager.remaining_ap() == 4

    game.action(char, ActionType.STEP, step=Step.FORWARD)
    assert game.turn_manager.remaining_ap() == 1


def test_action_checks_remaining_ap(game, game_faker, monkeypatch):
    char = game_faker.character(game)

    monkeypatch.setattr(ActionType.STEP.action, 'ap', 5)

    assert game.turn_manager.remaining_ap() == 4

    with pytest.raises(NotEnoughAPError):
        game.action(char, ActionType.STEP, step=Step.FORWARD)


def test_action_checks_possibility(game, game_faker):
    char = game_faker.character(game)
    char.step.side_effect = ActionNotAllowedError()

    with pytest.raises(ActionNotAllowedError):
        game.action(char, ActionType.STEP, step=Step.FORWARD)


def test_get_char(game, game_faker, faker):
    char = game_faker.character(game)

    assert game.get_character(char.id) == char

    with pytest.raises(UnknownCharacterError):
        game.get_character(faker.pystr())


def test_get_player(game, game_faker, faker):
    player = game_faker.player(game)

    assert game.get_player(player.id) == player

    with pytest.raises(UnknownPlayerError):
        game.get_player(faker.pystr())
