import unittest
from unittest.mock import patch

from game.action import Direction
from game.grid import Grid
from test.my_base import MyBaseTestCase


class TestGrid(MyBaseTestCase):

    def test_size_1(self):
        grid = self.create_grid(5, 3)
        assert grid.cols == 5
        assert grid.rows == 3

        grid = self.create_grid(10, 20)
        assert grid.cols == 10
        assert grid.rows == 20

    def test_out_of_bounds(self):
        grid = self.create_grid()
        assert not grid.is_out_of_bounds((1, 1))
        assert grid.is_out_of_bounds((3, 6))

        assert grid.is_out_of_bounds((6, 1))
        assert grid.is_out_of_bounds((99, 99))

        assert grid.is_out_of_bounds((0, 1))
        assert grid.is_out_of_bounds((4, 0))

    def test_grid_characters(self):
        grid = self.create_grid()
        assert len(grid.characters) == 0

        char = self.create_character(grid=grid)
        assert len(grid.characters) == 1
        assert grid.characters[0] == char

        char2 = self.create_character(grid=grid)

        assert len(grid.characters) == 2
        assert grid.characters[1] == char2

    def test_state(self):
        grid = self.create_grid()
        char1 = self.create_character(grid=grid, direction=Direction.LEFT, address=(1, 1))
        char2 = self.create_character(grid=grid, address=(2, 3))

        state = grid.state()

        assert len(state['characters']) == 2

        assert state['characters'][char1.char_id]['address'] == (1, 1)
        assert state['characters'][char1.char_id]['direction'] == 'LEFT'
        assert state['characters'][char2.char_id]['address'] == (2, 3)

    def test_can_step_oob(self):
        with patch.object(Grid, 'is_out_of_bounds', return_value=False) as mock:
            grid = self.create_grid()
            char = self.create_character(grid=grid)
            assert grid.can_step(char, (2, 2))

        mock.assert_called_once_with((2, 2))

        with patch.object(Grid, 'is_out_of_bounds', return_value=True) as mock:
            grid = self.create_grid()
            char = self.create_character(grid=grid)
            assert not grid.can_step(char, (2, 2))

        mock.assert_called_once_with((2, 2))

    def test_is_obstacle(self):
        grid = self.create_grid(5, 5, obstacles=[(2, 2), (3, 3)])
        assert grid.is_obstacle((2, 2))
        assert grid.is_obstacle((3, 3))
        assert not grid.is_obstacle((1, 1))

    def test_can_step_obstacle(self):
        with patch.object(Grid, 'is_obstacle', return_value=False) as mock:
            grid = self.create_grid()
            char1 = self.create_character(grid=grid)
            assert grid.can_step(char1, (1, 2))

        mock.assert_called_once_with((1, 2))

        with patch.object(Grid, 'is_obstacle', return_value=True) as mock:
            grid = self.create_grid()
            char1 = self.create_character(grid=grid)
            assert not grid.can_step(char1, (1, 2))

        mock.assert_called_once_with((1, 2))

    def test_is_wall(self):
        grid = self.create_grid(5, 5, walls=[((1, 1), (1, 2))])

        assert grid.is_wall((1, 1), (1, 2))
        assert grid.is_wall((1, 2), (1, 1))
        assert not grid.is_wall((1, 1), (2, 1))
        assert not grid.is_wall((1, 2), (2, 2))

    def test_can_step_wall(self):
        with patch.object(Grid, 'is_wall', return_value=False) as mock:
            grid = self.create_grid()
            char = self.create_character(grid=grid, address=(1, 1))
            assert grid.can_step(char, (1, 2))

        mock.assert_called_once_with((1, 1), (1, 2))

        with patch.object(Grid, 'is_wall', return_value=True) as mock:
            grid = self.create_grid()
            char = self.create_character(grid=grid, address=(1, 1))
            assert not grid.can_step(char, (1, 2))

        mock.assert_called_once_with((1, 1), (1, 2))

    def test_can_step_other_chars(self):
        grid = self.create_grid()
        char1 = self.create_character(grid=grid, address=(2, 2))
        char2 = self.create_character(grid=grid, address=(2, 3))

        assert not grid.can_step(char1, (2, 3))
        assert grid.can_step(char1, (3, 2))


if __name__ == '__main__':
    unittest.main()
