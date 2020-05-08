import Phaser, { Tilemaps } from "phaser";
import Board from "./components/Board";
import Character from "./components/Character";
import Controls from "./components/Controls";
import io from "socket.io-client";
import c from "./components/consts";

export default class BoardScene extends Phaser.Scene {
  board: Board;
  controls: Controls;
  socket: SocketIOClient.Socket;

  constructor() {
    super("Board");
  }

  preload() {

  }

  create() {
    this.socket = this.game.registry.get('socket')
    this.socket.on("connect", () => {
      this.socket.emit("join", { room: "Room 1" });
    });

    this.board = new Board(
      this,
      +this.game.config.width - Board.BOARD_WIDTH / 2,
      +this.game.config.height / 2
    );

    let zombie = new Character(this, this.board, "zombie", this.socket);
    zombie.position([3, 3]);

    this.controls = new Controls(this, 0, 0, zombie, this.socket);
  }
}
