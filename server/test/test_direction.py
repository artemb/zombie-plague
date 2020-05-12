import unittest

from game.enums import Direction, Turn
from test.my_base import MyBaseTestCase


class TestDirection(MyBaseTestCase):
    def test_turns(self):
        d = Direction.RIGHT

        d = d.turn(Turn.LEFT)
        assert d == Direction.UP

        d = d.turn(Turn.LEFT)
        assert d == Direction.LEFT

        d = d.turn(Turn.LEFT)
        assert d == Direction.DOWN

        d = d.turn(Turn.LEFT)
        assert d == Direction.RIGHT

        d = d.turn(Turn.RIGHT)
        assert d == Direction.DOWN

        d = d.turn(Turn.RIGHT)
        assert d == Direction.LEFT

        d = d.turn(Turn.RIGHT)
        assert d == Direction.UP

        d = d.turn(Turn.RIGHT)
        assert d == Direction.RIGHT

