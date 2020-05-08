import Phaser from 'phaser';
import SocketIOClient from 'socket.io-client'

export default class StateManager extends Phaser.Events. EventEmitter {
    private socket: SocketIOClient.Socket;
    playerId: string;
    characters: object;

    constructor(socket) {
        super();

        this.socket = socket;
        this.socket.on('message', (data) => this.onServerUpdate(data));
    }

    checkRegistration(player_id: string) {
        return new Promise<boolean> ((resolve, reject) => {
            this.socket.on('registration_check', (data) => {
                if (data['registered']) {
                    this.playerId = player_id;
                    return resolve(true);
                }
                return resolve(false);
            });

            this.socket.emit('check_registration', { player_id });
        });

    }

    registerPlayer(username: string) {
        return new Promise<void>((resolve, reject) => {
            this.socket.on('joined', (data) => {
                localStorage.setItem('player_id', data['player_id'])
                localStorage.setItem('player_name', username);

                this.playerId = data['player_id']
                resolve();
            });

            this.socket.emit("register", { username: username});
        });
    }

    update(character: string = null, action: string = null) {
        this.socket.emit('update', { character, action });
    }

    private onServerUpdate(data) {
        this.characters = data['characters'];
        this.emit('gamestatechange', this);
    }
}