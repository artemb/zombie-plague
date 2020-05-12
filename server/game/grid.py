from game.enums import Direction
from game.character import Character


class Grid:
    def __init__(self, cols, rows, obstacles = [], walls=[]):
        self.cols = cols
        self.rows = rows
        self.characters = []
        self.obstacles = obstacles
        self.walls = walls

    def add_character(self, character: Character):
        self.characters.append(character)

    def can_step(self, char, addr_to):
        if self.is_out_of_bounds(addr_to):
            return False

        if self.is_obstacle(addr_to):
            return False

        if self.is_wall(char.address, addr_to):
            return False

        for other in self.characters:
            if char.char_id == other.char_id:
                continue

            if other.address == addr_to:
                return False

        return True

    def is_out_of_bounds(self, address):
        if address[1] > self.rows or address[1] < 1:
            return True

        if address[0] > self.cols or address[0] < 1:
            return True

        return False

    def is_obstacle(self, address):
        if address in self.obstacles:
            return True

        return False

    def is_wall(self, addr_from, addr_to):
        if (addr_from, addr_to) in self.walls:
            return True

        if (addr_to, addr_from) in self.walls:
            return True

        return False

    def state(self):
        state = {'characters': {}}
        for char in self.characters:
            state['characters'][char.char_id] = {
                "player_id": char.player_id,
                "address": char.address,
                "direction": char.direction.value,
                "face": char.face
            }

        return state
