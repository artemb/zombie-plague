from typing import Tuple
from game.enums import Direction
from game.character import Character

class Player:
    def __init__(self, game, id, name):
        self.game = game
        self.id = id
        self.name = name
        self.characters = set()

        game.add_player(self)

    def create_character(self, address: Tuple, direction: Direction, face: str):
        char = Character(self.id, self.game.grid, face, address, direction)
        self.characters.add(char)