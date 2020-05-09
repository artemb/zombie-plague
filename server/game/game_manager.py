from random import randint, choice
from game.player import Player
from game.enums import Direction, Action, Step, Turn
from game.grid import Grid
from game.game import Game
from game.grid_def import OBSTACLES, WALLS
from game.turns import TurnManager


class GameManager:
    def __init__(self):
        grid = Grid(24, 20, obstacles=OBSTACLES, walls=WALLS)
        self.char_faces = ['char1', 'char2', 'char3', 'char4']
        self.game = Game(grid)
        self.players = {}
        self.chars = {}
        self.turn_manager = TurnManager(4)

    def register_player(self, id: str, name: str):
        player = Player(self.game, id, name)
        self.players[id] = player
        self.turn_manager.add_player(player)
        char = player.create_character(
            (randint(1, 24), randint(1, 20)),
            choice(list(Direction)),
            self.char_faces.pop()
        )
        self.chars[char.char_id] = char

    def is_player_registered(self, player_id):
        return player_id in self.players.keys()

    def action(self, char_id, data):
        # Checking if it is the player's turn
        char = self.chars[char_id]
        if char is None or self.turn_manager.current_player_id() != char.player_id:
            return

        if data['action'] in (Action.STEP_FORWARD.value, Action.STEP_BACKWARD.value):
            success = char.step(Step(data['action']))  # pylint: disable=no-value-for-parameter
            if not success:
                return

        if data['action'] == Action.TURN_RIGHT.value:
            char.turn(Turn.RIGHT)

        if data['action'] == Action.TURN_LEFT.value:
            char.turn(Turn.LEFT)

        self.turn_manager.spend_ap()

    def state(self):
        grid = self.game.grid.state()
        turn = self.turn_manager.state()

        return {'grid': grid, 'turn': turn}
