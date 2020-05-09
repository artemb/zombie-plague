from typing import Tuple
from uuid import uuid4

from game.enums import Direction, Step, Turn


class Character():
    def __init__(self, player_id: str, grid, face: str, address: Tuple, direction: Direction = Direction.DOWN):
        self.grid = grid
        self.address = address
        self.char_id = str(uuid4())
        self.player_id = player_id
        self.direction = direction
        self.face = face

        grid.add_character(self)

    def facing_cell(self, step:Step):
        col = self.address[0] + self.direction.vector[0] * step.modifier
        row = self.address[1] + self.direction.vector[1] * step.modifier

        return (col, row)

    def step(self, step: Step):
        target = self.facing_cell(step)
        if self.grid.can_step(self.address, target):
            self.address = target
            return True

        return False

    def turn(self, turn: Turn = Turn.LEFT):
        self.direction = self.direction.turn(turn)
