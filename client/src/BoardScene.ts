import Phaser from "phaser";
import Board from "./components/Board";
import Character from "./components/Character";
import Controls from "./components/Controls";

export default class BoardScene extends Phaser.Scene {
  board: Board;
  controls: Controls;
  socket: SocketIOClient.Socket;

  constructor() {
    super("Board");
  }

  create() {
    this.board = new Board(
      this,
      +this.game.config.width - Board.BOARD_WIDTH / 2,
      +this.game.config.height / 2
    );

    this.socket = this.game.registry.get('socket');

    let zombie = new Character(this, this.board, this.game.registry.get('player_id'), 'char');

    this.socket.emit('update', {action: null});

    this.controls = new Controls(this, 0, 0, zombie);
  }
}
