from enum import Enum

from game.turns import TurnManager


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
        self.turn_manager = TurnManager(4)

    def add_player(self, player):
        self.players[player.id] = player

    def add_character(self, character):
        self.characters.add(character)
        self.turn_manager.add_character(character)

    def state(self):
        state = {
            'status': self.status.name,
            'players': {},
            'grid': self.grid.state(),
            'turn': self.turn_manager.state()
        }

        for player_id, player in self.players.items():
            state['players'][player_id] = player.state()

        return state

    def start(self):
        if len(self.players) < 1:
            raise NoPlayersError()

        self.status = GameStatus.STARTED
