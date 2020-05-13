from enum import Enum

from game.turns import TurnManager


class GameStatus(Enum):
    LOBBY = "LOBBY",
    STARTED = "STARTED",
    FINISHED = "FINISHED",
    ABSENT = "ABSENT"


class NoPlayersError(Exception):
    pass


class NotCharactersTurnError(Exception):
    pass


class NotEnoughAPError(Exception):
    pass


class Game:
    def __init__(self, grid):
        self.grid = grid
        self.characters = {}
        self.players = {}
        self.status = GameStatus.LOBBY
        self.turn_manager = TurnManager(4)

    def add_player(self, player):
        self.players[player.id] = player

    def add_character(self, character, player):
        self.characters[character.char_id] = character
        character.attach_to_player(player.id, self.grid)
        self.turn_manager.add_character(character)

    def action(self, char, action_type, **params):
        if self.turn_manager.current_character() != char:
            raise NotCharactersTurnError()

        if self.turn_manager.remaining_ap() < action_type.action.ap:
            raise NotEnoughAPError()

        action_type.action.run(char, **params)
        self.turn_manager.spend_ap(action_type.action.ap)

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
