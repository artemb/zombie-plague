from enum import Enum


class GameStatus(Enum):
    LOBBY = "LOBBY",
    STARTED = "STARTED",
    FINISHED = "FINISHED",
    ABSENT = "ABSENT"


class NoPlayersError(Exception):
    pass


class Game:
    def __init__(self, grid):
        self.grid = grid
        self.characters = set()
        self.players = {}
        self.status = GameStatus.LOBBY

    def add_player(self, player):
        self.players[player.id] = player

    def add_character(self, character):
        self.characters.add(character)

    def state(self):
        return {'status': self.status}

    def start(self):
        if len(self.players) < 1:
            raise NoPlayersError()

        self.status = GameStatus.STARTED
