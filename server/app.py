from uuid import uuid4

from flask import Flask, render_template, session
from flask_socketio import SocketIO, send, emit

from api import GameServerAPI
from game.game_manager import GameManager

zombie_app: Flask = Flask(__name__)
zombie_app.config['SECRET_KEY'] = 'Ajdjeu234Jfjsd!lsd@#@33jA'
socketio = SocketIO(zombie_app, cors_allowed_origins='*')

api = GameServerAPI(GameManager(), session, emit, zombie_app.logger)

socketio.on_namespace(api)


@zombie_app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(zombie_app, debug=True, host='0.0.0.0')
