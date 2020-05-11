import unittest

from game.game import Game, GameStatus, NoPlayersError
from game.grid import Grid
from test.my_base import MyBaseTestCase


class GameTestCase(MyBaseTestCase):
    def setUp(self) -> None:
        self.game = Game(Grid(5, 5))

    def test_state(self):
        self.assertEqual(self.game.state()['status'], GameStatus.LOBBY)

    def test_game_start(self):
        self.game.add_player(self.create_player())
        self.game.start()

        self.assertEqual(self.game.status, GameStatus.STARTED)

    def test_game_start_no_players(self):
        self.assertEqual(len(self.game.players), 0)

        with self.assertRaises(NoPlayersError):
            self.game.start()


if __name__ == '__main__':
    unittest.main()
