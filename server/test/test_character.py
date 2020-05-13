from game.action import Turn, Direction, Step
from test.my_base import MyBaseTestCase


class TestCharacter(MyBaseTestCase):

    def test_facing_cell(self, game_factory):
        char = game_factory.create_character(address=(3, 3), direction=Direction.DOWN)

        assert char.facing_cell(Step.FORWARD) == (3, 4)
        assert char.facing_cell(Step.BACKWARD) == (3, 2)

        char = game_factory.create_character(address=(2, 2), direction=Direction.RIGHT)

        assert char.facing_cell(Step.FORWARD) == (3, 2)
        assert char.facing_cell(Step.BACKWARD) == (1, 2)

    def test_new_character(self, game_factory):
        game = game_factory.create_game()
        player = game_factory.create_player(id="Bob")
        char = game_factory.create_character(address=(3, 4), player=player, direction=Direction.UP, face='face1')

        assert game == game_factory.game
        assert game.grid == game_factory.grid

        assert char.address == (3, 4)
        assert char.player_id == "Bob"
        assert char.direction == Direction.UP
        assert char.grid == game.grid
        assert char.face == 'face1'
        assert char.char_id is not None

        player = game_factory.create_player(id="Stacey")
        char = game_factory.create_character(player=player, address=(1, 1), direction=Direction.LEFT,
                                     face='face2')

        assert char.player_id == "Stacey"
        assert char.char_id is not None
        assert char.address == (1, 1)
        assert char.direction == Direction.LEFT
        assert char.grid == game.grid
        assert char.face == 'face2'

    def test_character_turns(self, game_factory):
        char = game_factory.create_character(direction=Direction.DOWN)

        char.turn(Turn.LEFT)
        assert char.direction == Direction.RIGHT

        char.turn(Turn.RIGHT)
        assert char.direction == Direction.DOWN

    def test_character_steps(self, game_factory):
        grid = game_factory.create_grid(5, 5)
        char = game_factory.create_character(address=(3, 3), direction=Direction.DOWN)

        char.step(Step.FORWARD)
        assert char.address == (3, 4)

        char.step(Step.BACKWARD)
        assert char.address == (3, 3)

        char = game_factory.create_character(address=(2, 2), direction=Direction.RIGHT)

        char.step(Step.FORWARD)
        assert char.address == (3, 2)

        char.step(Step.BACKWARD)
        assert char.address == (2, 2)
