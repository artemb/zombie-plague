import unittest

from game.enums import Direction, Turn
from test.my_base import MyBaseTestCase


class DirectionsTestCase(MyBaseTestCase):
    def test_turns(self):
        d = Direction.RIGHT

        d = d.turn(Turn.LEFT)
        self.assertEqual(d, Direction.UP)

        d = d.turn(Turn.LEFT)
        self.assertEqual(d, Direction.LEFT)

        d = d.turn(Turn.LEFT)
        self.assertEqual(d, Direction.DOWN)

        d = d.turn(Turn.LEFT)
        self.assertEqual(d, Direction.RIGHT)

        d = d.turn(Turn.RIGHT)
        self.assertEqual(d, Direction.DOWN)

        d = d.turn(Turn.RIGHT)
        self.assertEqual(d, Direction.LEFT)

        d = d.turn(Turn.RIGHT)
        self.assertEqual(d, Direction.UP)

        d = d.turn(Turn.RIGHT)
        self.assertEqual(d, Direction.RIGHT)



if __name__ == '__main__':
    unittest.main()
