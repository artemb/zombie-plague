import Phaser from "phaser";
import Board from "./Board";
import Character from "./Character";
import SocketIOClient from "socket.io-client";
import CNST from './consts'

enum Action {
  FORWARD = "FORWARD",
  BACKWARD = "BACKWARD",
  LEFT = "TURN_LEFT",
  RIGHT = "TURN_RIGHT",
}

export default class Controls extends Phaser.GameObjects.Container {
  zombie: Character;
  socket: SocketIOClient.Socket;
  username: string;

  static preLoad(scene:Phaser.Scene) {
    scene.load.html('nameform', CNST.WEB_PREFIX + 'assets/username.html')
  }

  constructor(scene: Phaser.Scene, x: integer, y: integer, zombie: Character, socket: SocketIOClient.Socket) {
    super(scene, x, y);
    this.setSize(
      +scene.game.config.width - Board.BOARD_WIDTH,
      +scene.game.config.height
    );

    scene.add.existing(this);

    this.zombie = zombie;
    this.socket = socket;
    this.username = null;

    const nameform = scene.add.dom(this.width / 2, 250).createFromCache('nameform');
    this.add(nameform);
    nameform.addListener('click');
    nameform.on('click', (e) => {
      if (e.target.id === 'submit-username') {
        // @ts-ignore
        this.username = document.getElementById('user-name')?.value;
        nameform.visible = false;
      }
    });

    let left_btn = this.create_button(50, 50, 1, () =>
      this.sendUpdate(Action.LEFT)
    );
    let right_btn = this.create_button(120, 50, 4, () =>
      this.sendUpdate(Action.RIGHT)
    );
    let fwd_btn = this.create_button(50, 120, 2, () =>
      this.sendUpdate(Action.FORWARD)
    );
    let bwd_btn = this.create_button(120, 120, 3, () =>
      this.sendUpdate(Action.BACKWARD)
    );
  }

  sendUpdate(action: Action) {
    this.socket.emit("update", { action: action });
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
