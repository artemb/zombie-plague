import Phaser from 'phaser'
import Board from './Board'

const IMAGE_SCALE = 0.08;

export default class Character extends Phaser.GameObjects.Sprite {
    board: Board;
    _heading: number;
    address: number[];

    constructor(scene:Phaser.Scene, board:Board, texture:string) {
        super(scene, 0, 0, texture);
        this.setScale(IMAGE_SCALE);
        scene.add.existing(this);

        this.board = board;
        board.add(this);

        this.address = [1, 1]

        this._heading = 0;
    }

    // the angle is 0 for right, 90 for down, 180 for left, 270 for up
    set heading(angle) {
        if (angle < 0) {
            angle += 360;
        } else if (angle >= 360) {
            angle -= 360;
        }

        switch (angle) {
            case 0: {
                this.angle = 0;
                this.scaleX = IMAGE_SCALE;
                break;
            }
            case 90: {
                this.angle = 90;
                this.scaleX = IMAGE_SCALE;
                break;
            }
            case 180: {
                this.angle = 0;
                this.scaleX = -IMAGE_SCALE;
                break;
            }
            case 270: {
                this.angle = -90;
                this.scaleX = IMAGE_SCALE;
            }
        }

        this._heading = angle;
    }

    get heading() {
        return this._heading;
    }

    turn_left() {
        this.heading -= 90;
    }

    turn_right() {
        this.heading += 90;
    }

    position(address:integer[], animate = false) {
        this.address = address;
        let v:Phaser.Math.Vector2 = this.board.getPositionOnGrid(address)

        if (animate) {
            this.scene.tweens.add({
                targets: this,
                x: v.x,
                y: v.y,
                ease: Phaser.Math.Easing.Quartic,
                duration: 500,
                yoyo: false
            });
        } else {
            this.x = v.x;
            this.y = v.y;
        }
    }

    move(forward=true) {
        let row_step = 0;
        let col_step = 0;

        const facing_cell = this.board.grid.facingAddress(this.address, this.heading, forward)

        if (this.board.is_blocked(this.address, facing_cell)) {
            return;
        }

        let direction_factor = forward ? 1 : -1;

        this.position(facing_cell, true);
    }

}