import unittest
from unittest.mock import patch

from game.enums import Direction
from game.grid import Grid
from test.my_base import MyBaseTestCase


class TestGrid(MyBaseTestCase):

    def test_size_1(self):
        grid = self.create_grid(5, 3)
        self.assertEqual(grid.cols, 5)
        self.assertEqual(grid.rows, 3)

        grid = self.create_grid(10, 20)
        self.assertEqual(grid.cols, 10)
        self.assertEqual(grid.rows, 20)

    def test_out_of_bounds(self):
        grid = self.create_grid()
        self.assertFalse(grid.is_out_of_bounds((1, 1)))
        self.assertTrue(grid.is_out_of_bounds((3, 6)))

        self.assertTrue(grid.is_out_of_bounds((6, 1)))
        self.assertTrue(grid.is_out_of_bounds((99, 99)))

        self.assertTrue(grid.is_out_of_bounds((0, 1)))
        self.assertTrue(grid.is_out_of_bounds((4, 0)))

    def test_grid_characters(self):
        grid = self.create_grid()
        self.assertEqual(len(grid.characters), 0)

        char = self.create_character(grid=grid)
        self.assertEqual(len(grid.characters), 1)
        self.assertEqual(grid.characters[0], char)

        char2 = self.create_character(grid=grid)

        self.assertEquals(len(grid.characters), 2)
        self.assertEqual(grid.characters[1], char2)

    def test_state(self):
        grid = self.create_grid()
        char1 = self.create_character(grid=grid, direction=Direction.LEFT, address=(1, 1))
        char2 = self.create_character(grid=grid, address=(2, 3))

        state = grid.state()

        self.assertEqual(len(state['characters']), 2)

        self.assertEqual(state['characters'][char1.char_id]['address'], (1, 1))
        self.assertEqual(state['characters'][char1.char_id]['direction'], 'LEFT')
        self.assertEqual(state['characters'][char2.char_id]['address'], (2, 3))

    def test_can_step_oob(self):
        with patch.object(Grid, 'is_out_of_bounds', return_value=False) as mock:
            grid = self.create_grid()
            self.assertTrue(grid.can_step((1, 1), (2, 2)))

        mock.assert_called_once_with((2, 2))

        with patch.object(Grid, 'is_out_of_bounds', return_value=True) as mock:
            grid = self.create_grid()
            self.assertFalse(grid.can_step((1, 1), (2, 2)))

        mock.assert_called_once_with((2, 2))

    def test_is_obstacle(self):
        grid = self.create_grid(5, 5, obstacles=[(2, 2), (3, 3)])
        self.assertTrue(grid.is_obstacle((2, 2)))
        self.assertTrue(grid.is_obstacle((3, 3)))
        self.assertFalse(grid.is_obstacle((1, 1)))

    def test_can_step_obstacle(self):
        with patch.object(Grid, 'is_obstacle', return_value=False) as mock:
            grid = self.create_grid()
            self.assertTrue(grid.can_step((1, 1), (1, 2)))

        mock.assert_called_once_with((1, 2))

        with patch.object(Grid, 'is_obstacle', return_value=True) as mock:
            grid = self.create_grid()
            self.assertFalse(grid.can_step((1, 1), (1, 2)))

        mock.assert_called_once_with((1, 2))

    def test_is_wall(self):
        grid = self.create_grid(5, 5, walls=[((1, 1), (1, 2))])

        self.assertTrue(grid.is_wall((1, 1), (1, 2)))
        self.assertTrue(grid.is_wall((1, 2), (1, 1)))
        self.assertFalse(grid.is_wall((1, 1), (2, 1)))
        self.assertFalse(grid.is_wall((1, 2), (2, 2)))

    def test_can_step_wall(self):
        with patch.object(Grid, 'is_wall', return_value=False) as mock:
            grid = self.create_grid()
            self.assertTrue(grid.can_step((1, 1), (1, 2)))

        mock.assert_called_once_with((1, 1), (1, 2))

        with patch.object(Grid, 'is_wall', return_value=True) as mock:
            grid = self.create_grid()
            self.assertFalse(grid.can_step((1, 1), (1, 2)))

        mock.assert_called_once_with((1, 1), (1, 2))


if __name__ == '__main__':
    unittest.main()
