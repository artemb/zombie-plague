from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

state = {"players": ['Player 1', 'Player 2']}

@app.route('/')
def hello_world():
    return render_template('index.html')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('Game started', {room: 'Room 1'}, json=True, room=room)
    print(f"{username} joined {room}")

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    print(f"{username} left {room}")

@socketio.on('update')
def on_update(data):
    global state
    send(state, room='Room 1')
    print(f"state request")

@socketio.on('connect')
def on_connect(*args, **kwargs):
    print("Client connected")

@socketio.on('disconnect')
def on_disconnect(*args, **kwargs):
    print("client disconnected")

if __name__ == '__main__':
    socketio.run(app)