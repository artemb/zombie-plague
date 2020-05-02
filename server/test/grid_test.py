import unittest
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

    def test_facing_cell(self):
        grid = Grid(5, 5)

        self.assertEqual(grid.facing_cell((3, 5), Direction.DOWN), (3, 6))
        self.assertEqual(grid.facing_cell((1, 1), Direction.DOWN), (1, 2))

        self.assertEqual(grid.facing_cell((3, 3), Direction.RIGHT), (4, 3))
        self.assertEquals(grid.facing_cell((2, 2), Direction.LEFT), (1, 2))
        self.assertEquals(grid.facing_cell((4, 4), Direction.UP), (4, 3))

    def test_new_character(self):
        grid = Grid(5, 5)
        char = Character("Bob", grid, (3, 3), Direction.DOWN)

        self.assertEqual(char.address, (3, 3))
        self.assertEqual(char.name, "Bob")
        self.assertEqual(char.direction, Direction.DOWN)
        self.assertEqual(char.grid, grid)

        grid = Grid(1, 1)
        char = Character("Stacey", grid, (1, 1), Direction.UP)

        self.assertEqual(char.name, "Stacey")
        self.assertEqual(char.address, (1, 1))
        self.assertEquals(char.direction, Direction.UP)
        self.assertEquals(char.grid, grid)

    def test_character_turns(self):
        grid = Grid(5, 5)
        char = Character("zombie", grid, (3, 3), Direction.DOWN)

        char.turn(Turn.LEFT)

        self.assertEquals(char.direction, Direction.RIGHT)

        char.turn(Turn.RIGHT)

        self.assertEquals(char.direction, Direction.DOWN)

    def test_character_steps(self):
        grid = Grid(5, 5)
        char = Character("zombie", grid, (3, 3), Direction.DOWN)

        char.step(Step.FORWARD)
        self.assertEqual(char.address, (3, 4))

        char.step(Step.BACKWARD)
        self.assertEqual(char.address, (3, 3))

        char = Character("human", grid, (2, 2), Direction.RIGHT)

        char.step(Step.FORWARD)
        self.assertEqual(char.address, (3, 2))

        char.step(Step.BACKWARD)
        self.assertEqual(char.address, (2, 2))

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


if __name__ == '__main__':
    unittest.main()
