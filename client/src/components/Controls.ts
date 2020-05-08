import Phaser from "phaser";
import Board from "./Board";
import Character from "./Character";
import SocketIOClient from "socket.io-client";

enum Action {
  FORWARD = "FORWARD",
  BACKWARD = "BACKWARD",
  LEFT = "TURN_LEFT",
  RIGHT = "TURN_RIGHT",
}

export default class Controls extends Phaser.GameObjects.Container {
  zombie: Character;
  socket: SocketIOClient.Socket;

  static preload(scene:Phaser.Scene, prefix: string) {
    scene.load.html('nameform', prefix + 'assets/username.html')
  }

  constructor(scene: Phaser.Scene, x: integer, y: integer, character: Character) {
    // Initialize the controls container
    super(scene, x, y);
    this.setSize(
      +scene.game.config.width - Board.BOARD_WIDTH,
      +scene.game.config.height
    );
    scene.add.existing(this);

    this.socket = scene.game.registry.get('socket');

    this.drawControls(character)
  }

  drawControls(character) {
    this.create_button(50, 50, 1, () =>
        this.sendUpdate(character, Action.LEFT)
    );
    this.create_button(120, 50, 4, () =>
        this.sendUpdate(character, Action.RIGHT)
    );
    this.create_button(50, 120, 2, () =>
        this.sendUpdate(character, Action.FORWARD)
    );
    this.create_button(120, 120, 3, () =>
        this.sendUpdate(character, Action.BACKWARD)
    );
  }

  sendUpdate(character: Character, action: Action) {
    this.socket.emit("update", { character: character.char_id, action: action });
  }

  create_button(x: integer, y: integer, frame: integer, onPointerDown: Function) {
    let btn = this.scene.add
      .sprite(x, y, "buttons", frame)
      .setScale(0.3)
      .setInteractive();
    btn.on("pointerdown", onPointerDown);
    this.add(btn);

    return btn;
  }
}
