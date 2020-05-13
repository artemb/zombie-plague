import unittest
from unittest.mock import patch

import pytest

from game.action import ActionType, StepAction, Direction
from game.game import GameStatus, NoPlayersError
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

    def test_game_adds_characters_to_turn_manager(self):
        character = self.create_character()

        with patch.object(TurnManager, 'add_character') as mock:
            self.game.add_character(character)

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
        player = self.create_player(game=self.game)

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

    def test_action(self, mocker):
        char = self.create_character(grid=self.game.grid, address=(2, 2), direction=Direction.DOWN)
        self.game.add_character(char)
        mocker.patch.object(StepAction, 'run')
        self.game.action(char, ActionType.STEP, mock_param='mock_value')
        ActionType.STEP.action.run.assert_called_once_with(char, mock_param='mock_value')


if __name__ == '__main__':
    unittest.main()
