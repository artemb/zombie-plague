from unittest.mock import patch

from game.game import Game
from game.game_manager import GameManager
from test.my_base import MyBaseTestCase


class TestGameManager(MyBaseTestCase):

    def test_state(self):
        mgr = GameManager()

        expected = self.random_object()
        with patch.object(Game, 'state', return_value=expected):
            state = mgr.state()

        assert state == expected
