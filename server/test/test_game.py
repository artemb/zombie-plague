import unittest
from unittest.mock import patch

import pytest

from game.action import ActionType, StepAction, Direction, Step
from game.character import Character, ActionNotAllowedError
from game.game import GameStatus, NoPlayersError, NotCharactersTurnError, NotEnoughAPError
from game.grid import Grid
from game.player import Player
from game.turns import TurnManager
from test.my_base import MyBaseTestCase


class TestGame(MyBaseTestCase):
    def setup_method(self) -> None:
        self.game = self.create_game()

    def test_status(self):
        assert self.game.state()['status'] == 'LOBBY'

    def test_game_start(self):
        self.game.add_player(self.create_player())
        self.game.start()

        assert self.game.status == GameStatus.STARTED

    def test_game_start_no_players(self):
        assert len(self.game.players) == 0

        with pytest.raises(NoPlayersError):
            self.game.start()

    def test_game_has_turns(self):
        assert self.game.turn_manager is not None

    def test_game_adds_characters_to_turn_manager(self, game_factory):
        player = game_factory.create_player()
        character = game_factory.create_character()

        with patch.object(TurnManager, 'add_character') as mock:
            self.game.add_character(character, player)

        mock.assert_called_once_with(character)

    def test_state_status(self):
        state = self.game.state()
        assert 'status' in state
        assert state['status'] == 'LOBBY'

        self.game.add_player(self.create_player())
        self.game.start()
        state = self.game.state()

        assert 'status' in state
        assert state['status'] == 'STARTED'

    def test_state_players(self):
        player = self.create_player()

        self.game.add_player(player)

        expected = self.random_object()
        with patch.object(Player, 'state', return_value=expected) as mock:
            state = self.game.state()

        assert 'players' in state
        assert len(state['players']) == 1
        assert player.id in state['players']
        mock.assert_called_once()
        assert state['players'][player.id] == expected

    def test_state_grid(self):
        expected = self.random_object()
        with patch.object(Grid, 'state', return_value=expected) as mock:
            state = self.game.state()

        assert 'grid' in state
        assert state['grid'] == expected

    def test_state_turns(self):
        expected = self.random_object()
        with patch.object(TurnManager, 'state', return_value=expected):
            state = self.game.state()

        assert 'turn' in state
        assert state['turn'] == expected

    def test_action(self, game_factory, mocker):
        game = game_factory.create_game()
        char = game_factory.create_character(address=(2, 2), direction=Direction.DOWN)
        mocker.patch.object(StepAction, 'run')

        game.action(char, ActionType.STEP, mock_param='mock_value')

        ActionType.STEP.action.run.assert_called_once_with(char, mock_param='mock_value')

    def test_action_controls_turns(self, game_factory, mocker):
        game = game_factory.create_game()
        char1 = game_factory.create_character()
        char2 = game_factory.create_character()

        st = mocker.patch.object(Character, 'step')

        # Testing character who's turn it is
        game.action(char1, ActionType.STEP, step=Step.FORWARD)
        st.assert_called_once()
        st.reset_mock()

        # Testing character who's turn it's not
        with pytest.raises(NotCharactersTurnError):
            game.action(char2, ActionType.STEP, step=Step.FORWARD)

        st.assert_not_called()

    def test_action_deducts_ap(self, game_factory, monkeypatch):
        game = game_factory.create_game()
        char = game_factory.create_character()

        monkeypatch.setattr(ActionType.STEP.action, 'ap', 3)

        assert game.turn_manager.remaining_ap() == 4

        game.action(char, ActionType.STEP, step=Step.FORWARD)
        assert game.turn_manager.remaining_ap() == 1

    def test_action_checks_remaining_ap(self, game_factory, monkeypatch):
        game = game_factory.create_game()
        char = game_factory.create_character()

        monkeypatch.setattr(ActionType.STEP.action, 'ap', 5)

        assert game.turn_manager.remaining_ap() == 4

        with pytest.raises(NotEnoughAPError):
            game.action(char, ActionType.STEP, step=Step.FORWARD)

    def test_action_checks_possibility(self, game_factory, mocker):
        game_factory.create_grid(10, 10, obstacles=((1, 2),))
        game = game_factory.create_game()
        char = game_factory.create_character(address=(1, 1))

        with pytest.raises(ActionNotAllowedError):
            game.action(char, ActionType.STEP, step=Step.FORWARD)

    def test_game_add_character(self, game_factory):
        game = game_factory.create_game()
        player = game_factory.create_player()
        char = Character('face')

        game.add_character(char, player)

        assert len(game.characters) == 1
        assert char.char_id in game.characters
        assert game.characters[char.char_id] == char



if __name__ == '__main__':
    unittest.main()
