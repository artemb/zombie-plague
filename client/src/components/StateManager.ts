import Phaser from 'phaser';
import SocketIOClient from 'socket.io-client'

export default class StateManager extends Phaser.Events. EventEmitter {
    private socket: SocketIOClient.Socket;
    playerId: string;
    characters: object;
    turn: object;

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

    // isOurTurn() {
    //     return this.isPlayersTurn(this.playerId);
    // }

    // isPlayersTurn(playerId) {
    //     return this.turn['activePlayer'] == playerId;
    // }

    isCharactersTurn(characterId) {
        return this.turn['activeCharacter'] == characterId;
    }

    private onServerUpdate(data) {
        this.characters = data['grid']['characters'];
        this.turn = data['turn'];
        this.emit('gamestatechange', this);
    }
}