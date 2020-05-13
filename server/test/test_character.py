from game.action import Turn, Direction, Step
from test.my_base import MyBaseTestCase


class TestCharacter(MyBaseTestCase):

    def test_facing_cell(self):
        char = self.create_character(address=(3, 3), direction=Direction.DOWN)

        assert char.facing_cell(Step.FORWARD) == (3, 4)
        assert char.facing_cell(Step.BACKWARD) == (3, 2)

        char = self.create_character(address=(2, 2), direction=Direction.RIGHT)

        assert char.facing_cell(Step.FORWARD) == (3, 2)
        assert char.facing_cell(Step.BACKWARD) == (1, 2)

    def test_new_character(self):
        grid = self.create_grid()
        char = self.create_character(address=(3, 4), player_id="Bob", grid=grid, direction=Direction.UP, face='face1')

        assert char.address == (3, 4)
        assert char.player_id == "Bob"
        assert char.direction == Direction.UP
        assert char.grid == grid
        assert char.face == 'face1'
        assert char.char_id is not None

        grid = self.create_grid()
        char = self.create_character(grid=grid, player_id="Stacey", address=(1, 1), direction=Direction.LEFT,
                                     face='face2')

        assert char.player_id == "Stacey"
        assert char.char_id is not None
        assert char.address == (1, 1)
        assert char.direction == Direction.LEFT
        assert char.grid == grid
        assert char.face == 'face2'

    def test_character_turns(self):
        char = self.create_character(direction=Direction.DOWN)

        char.turn(Turn.LEFT)
        assert char.direction == Direction.RIGHT

        char.turn(Turn.RIGHT)
        assert char.direction == Direction.DOWN

    def test_character_steps(self):
        grid = self.create_grid(5, 5)
        char = self.create_character(grid=grid, address=(3, 3), direction=Direction.DOWN)

        char.step(Step.FORWARD)
        assert char.address == (3, 4)

        char.step(Step.BACKWARD)
        assert char.address == (3, 3)

        char = self.create_character(grid=grid, address=(2, 2), direction=Direction.RIGHT)

        char.step(Step.FORWARD)
        assert char.address == (3, 2)

        char.step(Step.BACKWARD)
        assert char.address == (2, 2)
