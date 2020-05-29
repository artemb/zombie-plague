from enum import Enum

from game.character import Character
from game.turns import TurnManager


class NotCharactersTurnError(Exception):
    pass


class NotEnoughAPError(Exception):
    pass


class UnknownPlayerError(Exception):
    pass


class UnknownCharacterError(Exception):
    pass


class OutOfCharactersError(Exception):
    pass


class GameStartedError(Exception):
    pass


class Lobby:
    def __init__(self):
        self.players = {}
        self.characters = {}
        self.available_faces = ['char1', 'char2', 'char3', 'char4']

    def register_player(self, player):
        self.players[player.id] = player

    def create_character(self):
        if len(self.available_faces) < 1:
            raise OutOfCharactersError()

        face = self.available_faces.pop(0)
        char = Character(face)
        self.characters[char.char_id] = char
        return char

    def get_player(self, player_id):
        if player_id not in self.players:
            raise UnknownPlayerError()

        return self.players[player_id]

    def get_character(self, char_id):
        if char_id not in self.characters:
            raise UnknownCharacterError()

        return self.characters[char_id]

    def assign_character(self, player, character):
        character.attach_to_player(player.id)

    def get_player_characters(self, player):
        return [char for char in self.characters.values() if char.player_id == player.id]

    def start_game(self, grid):
        return Game(grid, self.players, self.characters)


class Game:
    def __init__(self, grid, players, characters):
        self.grid = grid
        self.characters = characters
        self.players = players
        self.turn_manager = TurnManager(4, list(characters.values()))

    # def add_player(self, player):
    #     self.players[player.id] = player

    def get_player(self, player_id):
        if player_id not in self.players:
            raise UnknownPlayerError()

        return self.players[player_id]

    # def add_character(self, character, player):
    #     self.characters[character.char_id] = character
    #     character.attach_to_player(player.id, self.grid)
    #     self.turn_manager.add_character(character)

    def get_character(self, char_id):
        if char_id not in self.characters:
            raise UnknownCharacterError

        return self.characters[char_id]

    def action(self, char, action_type, **params):
        if self.turn_manager.current_character() != char:
            raise NotCharactersTurnError()

        if self.turn_manager.remaining_ap() < action_type.action.ap:
            raise NotEnoughAPError()

        action_type.action.run(char, **params)
        self.turn_manager.spend_ap(action_type.action.ap)

    def state(self):
        state = {
            'players': {},
            'grid': self.grid.state(),
            'turn': self.turn_manager.state()
        }

        for player_id, player in self.players.items():
            state['players'][player_id] = player.state()

        return state
