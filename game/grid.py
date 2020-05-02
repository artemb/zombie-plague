from game.grid_def import OBSTACLES, WALLS

from enum import Enum
from typing import Tuple


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


class Character():
    def __init__(self, name: str, grid, address: Tuple, direction: Direction = Direction.DOWN):
        self.grid = grid
        self.address = address
        self.name = name
        self.direction = direction

        grid.add_character(self)

    def step(self, step: Step):
        col = self.address[0] + self.direction.vector[0] * step.modifier
        row = self.address[1] + self.direction.vector[1] * step.modifier
        self.address = (col, row)

    def can_step(self, step: Step):
        pass

    def turn(self, turn: Turn = Turn.LEFT):
        self.direction = self.direction.turn(turn)


class Grid():
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.characters = []

    def add_character(self, character: Character):
        self.characters.append(character)

    def facing_cell(self, address, direction: Direction):
        if direction == Direction.DOWN:
            return (address[0], address[1] + 1)

        if direction == Direction.RIGHT:
            return (address[0] + 1, address[1])

        if direction == Direction.LEFT:
            return (address[0] - 1, address[1])

        if direction == Direction.UP:
            return (address[0], address[1] - 1)

    def is_out_of_bounds(self, address):
        if address[1] > self.rows:
            return True

        if address[0] > self.cols:
            return True

        return False

    def state(self):
        state = {'characters': {}}
        for char in self.characters:
            state['characters'][char.name] = {
                "address": char.address,
                "direction": char.direction.value
            }

        return state
