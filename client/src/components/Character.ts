import Phaser from "phaser";
import Board from "./Board";
import { Heading, Headings } from "./Heading";

const IMAGE_SCALE = 0.08;

export default class Character extends Phaser.GameObjects.Sprite {
  board: Board;
  // _heading: number;
  address: number[];
  _heading: Heading;
  socket: SocketIOClient.Socket;
  char_id: string;

  constructor(scene: Phaser.Scene,  board: Board, texture: string, socket: SocketIOClient.Socket ) {
    super(scene, 0, 0, texture);
    this.setScale(IMAGE_SCALE);
    scene.add.existing(this);

    this.board = board;
    board.add(this);

    this.address = [1, 1];
    this._heading = Headings.RIGHT;
    this.char_id = null
    this.socket = socket;

    socket.on('registration', (data:object) => {
      this.char_id = data['id']
    });

    socket.on("message", (data: object) => {
      this.position(data["characters"][this.char_id]["address"], true);
      if (data["characters"][this.char_id]["direction"] == "UP") {
        this.heading = Headings.UP;
      }

      if (data["characters"][this.char_id]["direction"] == "DOWN") {
        this.heading = Headings.DOWN;
      }

      if (data["characters"][this.char_id]["direction"] == "LEFT") {
        this.heading = Headings.LEFT;
      }

      if (data["characters"][this.char_id]["direction"] == "RIGHT") {
        this.heading = Headings.RIGHT;
      }
    });
  }

  set heading(heading: Heading) {
    this._heading = heading;
    this.angle = this._heading.angle;
    this.scaleX = this._heading.flip * IMAGE_SCALE;
    if (this._heading.flip == -1) {
      this.angle -= 180;
    }
  }

  get heading() {
    return this._heading;
  }

  turn_left() {
    this.heading = this.heading.turn_left();
  }

  turn_right() {
    this.heading = this.heading.turn_right();
  }

  position(address: integer[], animate = false) {
    this.address = address;
    let v: Phaser.Math.Vector2 = this.board.getPositionOnGrid(address);

    if (animate) {
      this.scene.tweens.add({
        targets: this,
        x: v.x,
        y: v.y,
        ease: Phaser.Math.Easing.Quartic,
        duration: 500,
        yoyo: false,
      });
    } else {
      this.x = v.x;
      this.y = v.y;
    }
  }

  move(forward = true) {
    const facing_cell = this.board.grid.facingAddress(
      this.address,
      this.heading,
      forward
    );

    if (this.board.is_blocked(this.address, facing_cell)) {
      return;
    }

    this.position(facing_cell, true);
  }
}
