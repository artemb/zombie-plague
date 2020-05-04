class Game:
    def __init__(self, grid):
        self.grid = grid
        self.characters = set()
        self.players = {}

    def add_player(self, player):
        self.players[player.id] = player

    def add_character(self, character):
        self.characters.add(character)