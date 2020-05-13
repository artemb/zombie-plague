from enum import Enum


class Action:
    def __init__(self, ap):
        self.ap = ap


class StepAction(Action):
    def __init__(self):
        super().__init__(1)

    def run(self, char, step):
        char.step(step)


class TurnAction(Action):
    def __init__(self):
        super().__init__(1)

    def run(self, char, turn):
        char.turn(turn)


class ActionType(Enum):
    STEP = 'STEP', StepAction()
    TURN = 'TURN', TurnAction()

    def __new__(cls, value, action=None):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.action = action
        return obj


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


class Step(Enum):
    FORWARD = 'FORWARD', 1
    BACKWARD = 'BACKWARD', -1

    def __new__(cls, value, modifier):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.modifier = modifier
        return obj