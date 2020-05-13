from typing import Tuple
from game.action import Direction
from game.character import Character


class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.characters = set()

    def state(self):
        return {'name': self.name}


class ZombiePlayer(Player):
    def __init__(self, game, id, name):
        super().__init__(self, game, id, name)
