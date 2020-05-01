from game.grid_def import OBSTACLES, WALLS

from enum import Enum
from typing import Tuple

class Turn(Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'

    def turn(self, turn: Turn):
        if self == Direction.RIGHT:
            return Direction.UP if turn == Turn.LEFT else Direction.DOWN
        elif self == Direction.UP:
            return Direction.LEFT if turn == Turn.LEFT else Direction.RIGHT
        elif self == Direction.LEFT:
            return Direction.DOWN if turn == Turn.LEFT else Direction.UP
        elif self == Direction.DOWN:
            return Direction.RIGHT if turn == Turn.LEFT else Direction.LEFT

class Character():
    def __init__(self, name:str, grid, address:Tuple, direction:Direction):
        self.grid = grid
        self.address = address
        self.name = name
        self.direction = direction

    def step(self, forward=True):
        pass

    def can_step(self, forward=True):
        pass

    def turn(self, turn:Turn = Turn.LEFT):
        pass

class Grid():
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

    def add_character(self, character:Character):
        pass

    def facing_cell(self, address, direction:Direction):
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

