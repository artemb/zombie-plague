from typing import Tuple
from uuid import uuid4

from game.action import Turn, Direction, Step


class ActionNotAllowedError(Exception):
    pass


class Character():
    def __init__(self, face: str):
        self.grid = None
        self.address = None
        self.char_id = str(uuid4())
        self.player_id = None
        self.direction = None
        self.face = face

    def attach_to_player(self, player_id, grid):
        self.grid = grid
        self.grid.add_character(self)
        self.player_id = player_id

    def spawn(self, address, direction):
        self.address = address
        self.direction = direction

    def facing_cell(self, step: Step):
        col = self.address[0] + self.direction.vector[0] * step.modifier
        row = self.address[1] + self.direction.vector[1] * step.modifier

        return (col, row)

    def step(self, step: Step):
        target = self.facing_cell(step)
        if not self.grid.can_step(self, target):
            raise ActionNotAllowedError()

        self.address = target
        return True

    def turn(self, turn: Turn = Turn.LEFT):
        self.direction = self.direction.turn(turn)
