from game.grid_def import OBSTACLES, WALLS
from game.enums import Direction
from game.character import Character


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
