import unittest
from game.grid import Grid
from game.enums import Direction, Turn, Step
from game.character import Character


class TestCharacter(unittest.TestCase):

    def test_facing_cell(self):
        grid = Grid(5, 5)
        char = Character("test", grid, 'char1', (3, 3), Direction.DOWN)

        self.assertEqual(char.facing_cell(Step.FORWARD), (3, 4))
        self.assertEqual(char.facing_cell(Step.BACKWARD), (3, 2))

        char = Character("test2", grid, 'char1', (2, 2), Direction.RIGHT)

        self.assertEqual(char.facing_cell(Step.FORWARD), (3, 2))
        self.assertEqual(char.facing_cell(Step.BACKWARD), (1, 2))


    def test_new_character(self):
        grid = Grid(5, 5)
        char = Character("Bob", grid, 'char1', (3, 3), Direction.DOWN)

        self.assertEqual(char.address, (3, 3))
        self.assertEqual(char.player_id, "Bob")
        self.assertIsNotNone(char.char_id)
        self.assertEqual(char.direction, Direction.DOWN)
        self.assertEqual(char.grid, grid)

        grid = Grid(1, 1)
        char = Character("Stacey", grid, 'char1', (1, 1), Direction.UP)

        self.assertEqual(char.player_id, "Stacey")
        self.assertIsNotNone(char.char_id)
        self.assertEqual(char.address, (1, 1))
        self.assertEquals(char.direction, Direction.UP)
        self.assertEquals(char.grid, grid)

    def test_character_turns(self):
        grid = Grid(5, 5)
        char = Character("zombie", grid, 'char1', (3, 3), Direction.DOWN)

        char.turn(Turn.LEFT)

        self.assertEquals(char.direction, Direction.RIGHT)

        char.turn(Turn.RIGHT)

        self.assertEquals(char.direction, Direction.DOWN)

    def test_character_steps(self):
        grid = Grid(5, 5)
        char = Character("zombie", grid, 'char1', (3, 3), Direction.DOWN)

        char.step(Step.FORWARD)
        self.assertEqual(char.address, (3, 4))

        char.step(Step.BACKWARD)
        self.assertEqual(char.address, (3, 3))

        char = Character("human", grid, 'char1', (2, 2), Direction.RIGHT)

        char.step(Step.FORWARD)
        self.assertEqual(char.address, (3, 2))

        char.step(Step.BACKWARD)
        self.assertEqual(char.address, (2, 2))        
