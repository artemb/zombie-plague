import logging
from uuid import uuid4


class GameServerAPI:
    def __init__(self, mgr, session, emit, logger=logging.getLogger(__name__)):
        self.mgr = mgr
        self.session = session
        self.logger = logger
        self.emit = emit

    def register(self, data):
        player_id = str(uuid4())
        player_name = data['username']
        self.session['player_id'] = player_id
        self.mgr.register_player(player_id, player_name)
        self.logger.info(f"Registered {player_name} at {player_id}")
        self.emit('joined', {'player_id': player_id})
