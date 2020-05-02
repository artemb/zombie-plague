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

  constructor(
    scene: Phaser.Scene,
    board: Board,
    texture: string,
    socket: SocketIOClient.Socket
  ) {
    super(scene, 0, 0, texture);
    this.setScale(IMAGE_SCALE);
    scene.add.existing(this);

    this.board = board;
    board.add(this);

    this.address = [1, 1];
    this._heading = Headings.RIGHT;
    this.socket = socket;

    socket.on("message", (data: object) => {
      this.position(data["characters"]["zombie1"]["address"], true);
      if (data["characters"]["zombie1"]["direction"] == "UP") {
        this.heading = Headings.UP;
      }

      if (data["characters"]["zombie1"]["direction"] == "DOWN") {
        this.heading = Headings.DOWN;
      }

      if (data["characters"]["zombie1"]["direction"] == "LEFT") {
        this.heading = Headings.LEFT;
      }

      if (data["characters"]["zombie1"]["direction"] == "RIGHT") {
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

  /*

    // the angle is 0 for right, 90 for down, 180 for left, 270 for up
    set heading(heading) {
        if (heading < 0) {
            heading += 360;
        } else if (heading >= 360) {
            heading -= 360;
        }

        switch (heading) {
            case HEADING.RIGHT: {
                this.angle = 0;
                this.scaleX = IMAGE_SCALE;
                break;
            }
            case HEADING.DOWN: {
                this.angle = 90;
                this.scaleX = IMAGE_SCALE;
                break;
            }
            case HEADING.LEFT: {
                this.angle = 0;
                this.scaleX = -IMAGE_SCALE;
                break;
            }
            case HEADING.UP: {
                this.angle = -90;
                this.scaleX = IMAGE_SCALE;
            }
        }

        this._heading = heading;
    }
    */

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
