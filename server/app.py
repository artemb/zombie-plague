from flask import Flask, render_template, session
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from game.grid import Grid
from game.character import Character
from game.enums import Action, Step, Turn

app: Flask = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

grid = Grid(24, 20)
zombie1 = Character("zombie1", grid, (2, 2))
zombie_index = 1


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('join')
def on_join(data):
    room = data['room']
    session['room'] = room
    join_room(room)
    send(grid.state())


@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)


@socketio.on('update')
def on_update(data):
    global grid, zombie1
    app.logger.info(  # pylint: disable=no-member
        f"State update request with {data}")

    if (data['action'] in (Action.STEP_FORWARD.value, Action.STEP_BACKWARD.value)):
        zombie1.step(Step(data['action']))  # pylint: disable=no-value-for-parameter

    if (data['action'] == Action.TURN_RIGHT.value):
        zombie1.turn(Turn.RIGHT)

    if (data['action'] == Action.TURN_LEFT.value):
        zombie1.turn(Turn.LEFT)

    send(grid.state(), room='Room 1')


if __name__ == '__main__':
    socketio.run(app, debug=True)
