from game.grid import Grid
from game.enums import Direction, Turn, Step
from game.character import Character
from test.my_base import MyBaseTestCase


class CharacterTestCase(MyBaseTestCase):

    def test_facing_cell(self):
        char = self.create_character(address=(3, 3), direction=Direction.DOWN)

        self.assertEqual(char.facing_cell(Step.FORWARD), (3, 4))
        self.assertEqual(char.facing_cell(Step.BACKWARD), (3, 2))

        char = self.create_character(address=(2, 2), direction=Direction.RIGHT)

        self.assertEqual(char.facing_cell(Step.FORWARD), (3, 2))
        self.assertEqual(char.facing_cell(Step.BACKWARD), (1, 2))


    def test_new_character(self):
        grid = self.create_grid()
        char = self.create_character(address=(3, 4), player_id="Bob", grid=grid, direction=Direction.UP, face='face1')

        self.assertEqual(char.address, (3, 4))
        self.assertEqual(char.player_id, "Bob")
        self.assertEqual(char.direction, Direction.UP)
        self.assertEqual(char.grid, grid)
        self.assertEqual(char.face, 'face1')
        self.assertIsNotNone(char.char_id)

        grid = self.create_grid()
        char = self.create_character(grid=grid, player_id="Stacey", address=(1, 1), direction=Direction.LEFT, face='face2')

        self.assertEqual(char.player_id, "Stacey")
        self.assertIsNotNone(char.char_id)
        self.assertEqual(char.address, (1, 1))
        self.assertEquals(char.direction, Direction.LEFT)
        self.assertEquals(char.grid, grid)
        self.assertEqual(char.face, 'face2')


    def test_character_turns(self):
        char = self.create_character(direction=Direction.DOWN)

        char.turn(Turn.LEFT)
        self.assertEquals(char.direction, Direction.RIGHT)

        char.turn(Turn.RIGHT)
        self.assertEquals(char.direction, Direction.DOWN)

    def test_character_steps(self):
        grid = self.create_grid(5, 5)
        char = self.create_character(grid=grid, address=(3, 3), direction=Direction.DOWN)

        char.step(Step.FORWARD)
        self.assertEqual(char.address, (3, 4))

        char.step(Step.BACKWARD)
        self.assertEqual(char.address, (3, 3))

        char = self.create_character(grid=grid, address=(2, 2), direction=Direction.RIGHT)

        char.step(Step.FORWARD)
        self.assertEqual(char.address, (3, 2))

        char.step(Step.BACKWARD)
        self.assertEqual(char.address, (2, 2))        
