class TurnManager:
    def __init__(self, max_ap):
        self.players = []
        self.max_ap = max_ap
        self.active_player_index = 0
        self.current_turn_ap = max_ap

    def add_player(self, player):
        self.players += [player]

    def current_player(self):
        return self.players[self.active_player_index]

    def current_player_id(self):
        return self.current_player().id

    def end_turn(self):
        self.active_player_index += 1
        self.active_player_index %= len(self.players)
        self.current_turn_ap = self.max_ap

    def remaining_ap(self):
        return self.current_turn_ap

    def spend_ap(self):
        self.current_turn_ap -= 1
        if self.current_turn_ap <= 0:
            self.end_turn()

    def state(self):
        return {
            'activePlayer': self.current_player_id(),
            'remainingAP': self.remaining_ap()
        }
