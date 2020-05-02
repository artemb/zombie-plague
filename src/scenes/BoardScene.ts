import Phaser, { Tilemaps } from "phaser";
import Board from "../components/Board";
import Character from "../components/Character";
import Controls from "../components/Controls";
import io from "socket.io-client";
import c from "../components/consts";

export default class BoardScene extends Phaser.Scene {
  board: Board;
  controls: Controls;
  socket: SocketIOClient.Socket;

  constructor() {
    super("game-scene");
  }

  preload() {
    Board.preload(this);
    this.load.image(
      "zombie",
      c.WEB_PREFIX + "assets/characters/zombies/male/idle.png"
    );
    this.load.spritesheet("buttons", c.WEB_PREFIX + "assets/ui/controls.png", {
      frameWidth: 200,
      frameHeight: 215,
    });
    let socket = io("localhost:5000");
    this.socket = socket;

    socket.on("connect", () => {
      socket.emit("join", { room: "Room 1" });
    });
  }

  create() {
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
