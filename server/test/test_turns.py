import unittest

from game.character import Character
from game.grid import Grid
from game.turns import TurnManager
from test.my_base import MyBaseTestCase


class TurnsTestCase(MyBaseTestCase):
    
    def setUp(self) -> None:
        self.tm = TurnManager(4)

        self.char1 = self.create_character()
        self.char2 = self.create_character()

        self.tm.add_character(self.char1)
        self.tm.add_character(self.char2)

    def test_turns(self):
        assert self.tm.current_character_id() ==  self.char1.char_id

        self.tm.end_turn()
        assert self.tm.current_character_id() ==  self.char2.char_id

        self.tm.end_turn()
        assert self.tm.current_character_id() ==  self.char1.char_id

    def test_remaining_ap(self):
        assert self.tm.current_character_id() ==  self.char1.char_id
        assert self.tm.remaining_ap() ==  4

        self.tm.spend_ap()
        assert self.tm.remaining_ap() ==  3

        self.tm.spend_ap()
        self.tm.spend_ap()
        assert self.tm.remaining_ap() ==  1

        self.tm.spend_ap()
        assert self.tm.current_character_id() ==  self.char2.char_id
        assert self.tm.remaining_ap() ==  4


if __name__ == '__main__':
    unittest.main()
