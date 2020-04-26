import Phaser from 'phaser'
import Board from './Board'

export default class Character extends Phaser.GameObjects.Sprite {
    board: Board;
    row: number;
    column: number;
    _heading: number;

    constructor(scene:Phaser.Scene, board:Board, texture:string) {
        super(scene, 0, 0, texture);
        this.setScale(0.08);
        scene.add.existing(this);

        this.board = board;
        board.add(this);

        this.row = 1;
        this.column = 1;
        this._heading = 0;
    }

    // the angle is 0 for right, 90 for down, 180 for left, 270 for up
    set heading(angle) {
        if (angle < 0) {
            angle += 360;
        } else if (angle >= 360) {
            angle -= 360;
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

    position(row:integer, column:integer, animate = false) {
        this.row = row;
        this.column = column;
        let v:Phaser.Math.Vector2 = this.board.getPositionOnGrid(row, column)

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

    move_forward() {
        let row_step = 0;
        let col_step = 0;

        if (this.heading == 0) {
            col_step = 1;
        } else if (this.heading == 90) {
            row_step = 1;
        } else if (this.heading == 180) {
            col_step = -1
        } else if (this.heading == 270) {
            row_step = -1
        } else {
            console.error(`Unknown heading: ${this.heading}`);
        }

        
        this.position(this.row + row_step, this.column + col_step, true);
    }

}