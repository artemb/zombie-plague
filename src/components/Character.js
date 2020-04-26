import Phaser from 'phaser'

export default class Character extends Phaser.GameObjects.Sprite {

    constructor(scene, board, texture) {
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

    position(row, column) {
        this.row = row;
        this.column = column;
        this.board.positionOnGrid(this, row, column);
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
        this.position(this.row + row_step, this.column + col_step);
    }

}