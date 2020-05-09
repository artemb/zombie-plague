from uuid import uuid4

from flask import Flask, render_template, session
from flask_socketio import SocketIO, send, emit

from game.game_manager import GameManager

app: Flask = Flask(__name__)
app.config['SECRET_KEY'] = 'Ajdjeu234Jfjsd!lsd@#@33jA'
socketio = SocketIO(app, cors_allowed_origins='*')

mgr = GameManager()


# grid = Grid(24, 20, obstacles=OBSTACLES, walls=WALLS)
# zombie1 = Character("zombie1", grid, (2, 2))
# zombie_index = 1

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('check_registration')
def check_registration(data):
    player_id = data['player_id']
    is_registered = mgr.is_player_registered(player_id)
    if is_registered:
        session['player_id'] = player_id

    app.logger.info(f"Registration check for {player_id} returned {is_registered}")
    emit('registration_check', {'registered': is_registered})


@socketio.on('register')
def register(data):
    player_id = str(uuid4())
    player_name = data['username']
    session['player_id'] = player_id
    mgr.register_player(player_id, player_name)
    app.logger.info(f"Registered {player_name} at {player_id}")  # pylint: disable=no-member

    emit('joined', {'player_id': player_id})


@socketio.on('update')
def on_update(data):
    app.logger.info(  # pylint: disable=no-member
        f"State update from {session['player_id']} request with {data}")

    if data['action'] is not None:
        mgr.action(data['character'], data)

    app.logger.info(
        f"Sending state {mgr.state()}"
    )

    socketio.send(mgr.state())


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
