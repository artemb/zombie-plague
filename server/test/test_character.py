import pytest

from game.action import Turn, Direction, Step
from game.character import Character


@pytest.fixture
def char(faker):
    return Character(faker.pystr())


@pytest.fixture
def grid(game_factory):
    return game_factory.create_grid()


def test_facing_cell_1(grid, char):
    char.spawn(grid, (3, 3), Direction.DOWN)

    assert char.facing_cell(Step.FORWARD) == (3, 4)
    assert char.facing_cell(Step.BACKWARD) == (3, 2)


def test_facing_cell_2(grid, char):
    char.spawn(grid, (2, 2), Direction.RIGHT)

    assert char.facing_cell(Step.FORWARD) == (3, 2)
    assert char.facing_cell(Step.BACKWARD) == (1, 2)


def test_new_character(game_factory, game_faker):
    char = Character('face1')
    assert char.face == 'face1'
    assert char.char_id is not None

    char2 = Character('face2')
    assert char2.face == 'face2'
    assert char2.char_id is not None
    assert char2.char_id != char.char_id


def test_attach_to_player(char, faker):
    player_id = faker.pystr()
    char.attach_to_player(player_id)

    assert char.player_id == player_id


def test_spawn_1(char, grid):
    char.spawn(grid, (3, 4), Direction.UP)

    assert char.address == (3, 4)
    assert char.direction == Direction.UP
    assert char.grid == grid


def test_spawn_2(grid, char):
    char.spawn(grid, (1, 1), Direction.LEFT)

    assert char.address == (1, 1)
    assert char.direction == Direction.LEFT
    assert char.grid == grid


def test_character_turns(char):
    char.direction = Direction.DOWN

    char.turn(Turn.LEFT)
    assert char.direction == Direction.RIGHT

    char.turn(Turn.RIGHT)
    assert char.direction == Direction.DOWN


def test_character_steps_1(grid, char):
    char.spawn(grid, (3, 3), Direction.DOWN)

    char.step(Step.FORWARD)
    assert char.address == (3, 4)

    char.step(Step.BACKWARD)
    assert char.address == (3, 3)


def test_character_steps_2(grid, char):
    char.spawn(grid, (2, 2), Direction.RIGHT)

    char.step(Step.FORWARD)
    assert char.address == (3, 2)

    char.step(Step.BACKWARD)
    assert char.address == (2, 2)
