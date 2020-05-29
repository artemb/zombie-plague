class TurnManager:
    def __init__(self, max_ap, characters):
        self.characters = characters
        self.max_ap = max_ap
        self.active_character_index = 0
        self.current_turn_ap = max_ap

    def add_character(self, character):
        self.characters += [character]

    def current_character(self):
        return self.characters[self.active_character_index]

    def current_character_id(self):
        return self.current_character().char_id

    def end_turn(self):
        self.active_character_index += 1
        self.active_character_index %= len(self.characters)
        self.current_turn_ap = self.max_ap

    def remaining_ap(self):
        return self.current_turn_ap

    def spend_ap(self, ap=1):
        self.current_turn_ap -= ap
        if self.current_turn_ap <= 0:
            self.end_turn()

    def state(self):
        if len(self.characters) < 1:
            return {}

        return {
            'activeCharacter': self.current_character_id(),
            'remainingAP': self.remaining_ap()
        }
