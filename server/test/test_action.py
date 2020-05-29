import pytest

from game.action import ActionType, Turn, Direction, Step
from game.character import Character


@pytest.fixture
def char(game_factory, mocker):
    mocker.patch.object(Character, 'step')
    mocker.patch.object(Character, 'turn')
    return game_factory.create_character(address=(1, 1), direction=Direction.DOWN)


@pytest.mark.parametrize(('step'), ((Step.FORWARD), (Step.BACKWARD)))
def test_step(char, step):
    ActionType.STEP.action.run(char, step=step)
    Character.step.assert_called_once_with(step)


@pytest.mark.parametrize(('turn'), ((Turn.LEFT), (Turn.RIGHT)))
def test_turn_left(char, turn):
    ActionType.TURN.action.run(char, turn=turn)
    Character.turn.assert_called_once_with(turn)
