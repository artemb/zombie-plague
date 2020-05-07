from flask import Flask, render_template, session
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from game.grid import Grid
from game.character import Character
from game.enums import Action, Step, Turn
from game.grid_def import OBSTACLES, WALLS
from game.game_manager import GameManager
from faker import Faker
from uuid import uuid4

app: Flask = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
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


@socketio.on('join')
def on_join(data):
    # Joining the room
    room = data['room']
    session['room'] = room
    join_room(room)

    # registering the player
    if not 'uid' in session:
        player_id = str(uuid4())
        player_name = Faker().name()
        session['uid'] = player_id
        mgr.register_player(player_id, player_name)
        emit('registration', {'id': player_id})
        app.logger.info(f"Registered {player_name} at {player_id}") # pylint: disable=no-member
    
    # sending the game state
    send(mgr.state())


@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)


@socketio.on('update')
def on_update(data):
    app.logger.info(  # pylint: disable=no-member
        f"State update from {session['uid']} request with {data}")

    mgr.action(session['uid'], data)

    app.logger.info(
        f"Sending state {mgr.state()}"
    )

    send(mgr.state(), room=session['room'])


if __name__ == '__main__':
    socketio.run(app, debug=True)
