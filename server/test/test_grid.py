import unittest
from unittest.mock import patch
from game.grid import Grid
from game.enums import Direction, Turn, Step
from game.character import Character


class TestGrid(unittest.TestCase):

    def test_size_1(self):
        grid = Grid(5, 3)
        self.assertEqual(grid.cols, 5)
        self.assertEqual(grid.rows, 3)

        grid = Grid(10, 20)
        self.assertEqual(grid.cols, 10)
        self.assertEqual(grid.rows, 20)

    def test_out_of_bounds(self):
        grid = Grid(5, 5)
        self.assertFalse(grid.is_out_of_bounds((1, 1)))
        self.assertTrue(grid.is_out_of_bounds((3, 6)))

        self.assertTrue(grid.is_out_of_bounds((6, 1)))
        self.assertTrue(grid.is_out_of_bounds((99, 99)))

        self.assertTrue(grid.is_out_of_bounds((0, 1)))
        self.assertTrue(grid.is_out_of_bounds((4, 0)))

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

    def test_grid_characters(self):
        grid = Grid(5, 5)
        self.assertEqual(len(grid.characters), 0)

        char = Character("zombie1", grid, (1, 1))
        self.assertEqual(len(grid.characters), 1)
        self.assertEqual(grid.characters[0], char)

        Character("zombie2", grid, (2, 2))
        self.assertEquals(len(grid.characters), 2)

    def test_state(self):

        grid = Grid(5, 5)
        Character("zombie1", grid, (1, 1), Direction.LEFT)
        Character("zombie2", grid, (2, 3))

        state = grid.state()

        self.assertEqual(len(state['characters']), 2)
        self.assertIn("zombie1", state['characters'].keys())
        self.assertEqual(state['characters']['zombie1']['address'], (1, 1))
        self.assertEqual(state['characters']['zombie1']['direction'], 'LEFT')
        self.assertEqual(state['characters']['zombie2']['address'], (2, 3))

    def test_can_step_oob(self):

        with patch.object(Grid, 'is_out_of_bounds', return_value=False) as mock:
            grid = Grid(5, 5)
            self.assertTrue(grid.can_step((1, 1), (2, 2)))

        mock.assert_called_once_with((2, 2))

        with patch.object(Grid, 'is_out_of_bounds', return_value=True) as mock:
            grid = Grid(5, 5)
            self.assertFalse(grid.can_step((1, 1), (2, 2)))

        mock.assert_called_once_with((2, 2))

    def test_is_obstacle(self):
        grid = Grid(5, 5, [(2, 2), (3, 3)])
        self.assertTrue(grid.is_obstacle((2, 2)))
        self.assertTrue(grid.is_obstacle((3, 3)))
        self.assertFalse(grid.is_obstacle((1, 1)))

    def test_can_step_obstacle(self):
        with patch.object(Grid, 'is_obstacle', return_value=False) as mock:
            grid = Grid(5,5)
            self.assertTrue(grid.can_step((1, 1), (1, 2)))

        mock.assert_called_once_with((1, 2))

        with patch.object(Grid, 'is_obstacle', return_value=True) as mock:
            grid = Grid(5, 5)
            self.assertFalse(grid.can_step((1, 1), (1, 2)))

        mock.assert_called_once_with((1, 2))

    def test_is_wall(self):
        grid = Grid(5, 5, walls=[((1, 1), (1, 2))])

        self.assertTrue(grid.is_wall((1,1), (1, 2)))
        self.assertTrue(grid.is_wall((1, 2), (1, 1)))
        self.assertFalse(grid.is_wall((1, 1), (2, 1)))
        self.assertFalse(grid.is_wall((1, 2), (2, 2)))

    def test_can_step_wall(self):
        with patch.object(Grid, 'is_wall', return_value=False) as mock:
            grid = Grid(5, 5)
            self.assertTrue(grid.can_step((1, 1), (1, 2)))

        mock.assert_called_once_with((1, 1), (1, 2))

        with patch.object(Grid, 'is_wall', return_value=True) as mock:
            grid = Grid(5, 5)
            self.assertFalse(grid.can_step((1, 1), (1, 2)))

        mock.assert_called_once_with((1, 1), (1, 2))


if __name__ == '__main__':
    unittest.main()
