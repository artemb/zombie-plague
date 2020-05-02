from typing import Tuple
from game.enums import Direction, Step, Turn


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
