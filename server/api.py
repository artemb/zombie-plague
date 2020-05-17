import logging
from uuid import uuid4

from flask_socketio import Namespace


class GameServerAPI(Namespace):
    def __init__(self, mgr, session, emit, send, logger=logging.getLogger(__name__)):
        super().__init__()
        self.mgr = mgr
        self.session = session
        self.logger = logger
        self.emit = emit
        self.send = send

    def on_register(self, data):
        player_id = str(uuid4())
        player_name = data['username']
        self.session['player_id'] = player_id
        self.mgr.register_player(player_id, player_name)
        self.logger.info(f"Registered {player_name} at {player_id}")
        self.emit('joined', {'player_id': player_id})

    def on_check_registration(self, data):
        player_id = data['player_id']
        is_registered = self.mgr.is_player_registered(player_id)
        if is_registered:
            self.session['player_id'] = player_id

        self.logger.info(f"Registration check for {player_id} returned {is_registered}")
        self.emit('registration_check', {'registered': is_registered})

    def on_update(self, data):
        self.logger.info(  # pylint: disable=no-member
            f"State update from {self.session['player_id']} request with {data}")

        if data['action'] is not None:
            params = {}
            if 'params' in data:
                params = data['params']

            self.mgr.action(data['character'], data['action'], params)

        self.logger.info(
            f"Sending state {self.mgr.state()}"
        )

        self.send(self.mgr.state(), broadcast=True)

