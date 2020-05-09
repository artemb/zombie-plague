import unittest

from game.game import Game
from game.player import Player
from game.turns import TurnManager


class TurnsTestCase(unittest.TestCase):
    def test_turns(self):
        game = Game(None)
        tm = TurnManager(4)

        tm.add_player(Player(game, 1, 'hi'))
        tm.add_player(Player(game, 2, 'hi'))

        self.assertEqual(tm.current_player_id(), 1)

        tm.end_turn()
        self.assertEqual(tm.current_player_id(), 2)

        tm.end_turn()
        self.assertEqual(tm.current_player_id(), 1)

    def test_remaining_ap(self):
        game = Game(None)
        tm = TurnManager(4)

        tm.add_player(Player(game, 1, 'hi'))
        tm.add_player(Player(game, 2, 'hi'))

        self.assertEqual(tm.current_player_id(), 1)
        self.assertEqual(tm.remaining_ap(), 4)

        tm.spend_ap()
        self.assertEqual(tm.remaining_ap(), 3)

        tm.spend_ap()
        tm.spend_ap()
        self.assertEqual(tm.remaining_ap(), 1)

        tm.spend_ap()
        self.assertEqual(tm.current_player_id(), 2)
        self.assertEqual(tm.remaining_ap(), 4)


if __name__ == '__main__':
    unittest.main()
