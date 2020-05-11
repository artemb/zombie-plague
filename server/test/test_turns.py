import unittest

from game.character import Character
from game.game import Game
from game.grid import Grid
from game.player import Player
from game.turns import TurnManager


class TurnsTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        grid = Grid(5, 5)
        self.tm = TurnManager(4)

        self.char1 = Character('player1', grid, 'face', ())
        self.char2 = Character('player2', grid, 'face', ())

        self.tm.add_character(self.char1)
        self.tm.add_character(self.char2)

    def test_turns(self):
        self.assertEqual(self.tm.current_character_id(), self.char1.char_id)

        self.tm.end_turn()
        self.assertEqual(self.tm.current_character_id(), self.char2.char_id)

        self.tm.end_turn()
        self.assertEqual(self.tm.current_character_id(), self.char1.char_id)

    def test_remaining_ap(self):
        self.assertEqual(self.tm.current_character_id(), self.char1.char_id)
        self.assertEqual(self.tm.remaining_ap(), 4)

        self.tm.spend_ap()
        self.assertEqual(self.tm.remaining_ap(), 3)

        self.tm.spend_ap()
        self.tm.spend_ap()
        self.assertEqual(self.tm.remaining_ap(), 1)

        self.tm.spend_ap()
        self.assertEqual(self.tm.current_character_id(), self.char2.char_id)
        self.assertEqual(self.tm.remaining_ap(), 4)


if __name__ == '__main__':
    unittest.main()
