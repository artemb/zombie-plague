from enum import Enum

from game.enums import Step


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

