from flask import Flask, render_template, session
from flask_socketio import SocketIO, join_room, leave_room, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

state = {"players": ['Player 1', 'Player 2']}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    room = data['room']
    session['room'] = room
    join_room(room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)

@socketio.on('update')
def on_update(data):
    global state
    send(state, room='Room 1')
    print(f"state request")

if __name__ == '__main__':
    socketio.run(app, debug=True, extra_files=['static/main.js'])