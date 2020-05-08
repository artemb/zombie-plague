from random import randint, choice
from game.player import Player
from game.enums import Direction, Action, Step, Turn
from game.grid import Grid
from game.game import Game
from game.grid_def import OBSTACLES, WALLS


class GameManager:
    def __init__(self):
        grid = Grid(24, 20, obstacles=OBSTACLES, walls=WALLS)
        self.char_faces = ['char1', 'char2', 'char3', 'char4']
        self.game = Game(grid)
        self.players = {}

    def register_player(self, id: str, name: str):
        player = Player(self.game, id, name)
        self.players[id] = player
        player.create_character(
            (randint(1, 24), randint(1, 20)),
            choice(list(Direction)),
            self.char_faces.pop()
        )

    def is_player_registered(self, player_id):
        return player_id in self.players.keys()

    def action(self, player_id, data):
        player = self.players[player_id]
        char = player.characters.copy().pop()

        if data['action'] in (Action.STEP_FORWARD.value, Action.STEP_BACKWARD.value):
            char.step(Step(data['action']))  # pylint: disable=no-value-for-parameter

        if data['action'] == Action.TURN_RIGHT.value:
            char.turn(Turn.RIGHT)

        if data['action'] == Action.TURN_LEFT.value:
            char.turn(Turn.LEFT)

    def state(self):
        return self.game.grid.state()
