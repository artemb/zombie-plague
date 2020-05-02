from enum import Enum


class Turn(Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'


class Direction(Enum):
    UP = 'UP', (0, -1)
    DOWN = 'DOWN', (0, 1)
    RIGHT = 'RIGHT', (1, 0)
    LEFT = 'LEFT', (-1, 0)

    def __new__(cls, value, vector):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.vector = vector
        return obj

    def turn(self, turn: Turn):
        if self == Direction.RIGHT:
            return Direction.UP if turn == Turn.LEFT else Direction.DOWN
        elif self == Direction.UP:
            return Direction.LEFT if turn == Turn.LEFT else Direction.RIGHT
        elif self == Direction.LEFT:
            return Direction.DOWN if turn == Turn.LEFT else Direction.UP
        elif self == Direction.DOWN:
            return Direction.RIGHT if turn == Turn.LEFT else Direction.LEFT


class Action(Enum):
    STEP_FORWARD = 'FORWARD'
    STEP_BACKWARD = 'BACKWARD'
    TURN_LEFT = 'TURN_LEFT'
    TURN_RIGHT = 'TURN_RIGHT'


class Step(Enum):
    FORWARD = 'FORWARD', 1
    BACKWARD = 'BACKWARD', -1

    def __new__(cls, value, modifier):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.modifier = modifier
        return obj
