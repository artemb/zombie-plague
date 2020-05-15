from random import randint, choice

from game.action import ActionType, Turn, Direction, Step
from game.character import Character
from game.game import Game, UnknownPlayerError
from game.grid import Grid
from game.grid_def import OBSTACLES, WALLS
from game.player import Player


class GameManager:
    def __init__(self):
        grid = Grid(24, 20, obstacles=OBSTACLES, walls=WALLS)
        self.char_faces = ['char1', 'char2', 'char3', 'char4']
        self.game = Game(grid)

    def register_player(self, id: str, name: str):
        player = Player(id, name)
        self.game.add_player(player)

        char = Character(self.char_faces.pop())
        self.game.add_character(char, player)

        char.spawn((randint(1, 24), randint(1, 20)), choice(list(Direction)))

    def is_player_registered(self, player_id):
        try:
            self.game.get_player(player_id)
            return True

        except UnknownPlayerError:
            return False

    def action(self, char_id, action_type, params):
        char = self.game.get_character(char_id)

        if 'step' in params:
            params['step'] = Step[params['step']]

        if 'turn' in params:
            params['turn'] = Turn[params['turn']]

        self.game.action(char, ActionType[action_type], **params)

    def state(self):
        return self.game.state()
