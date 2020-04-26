import Phaser from 'phaser'
import Board from './Board'

const IMAGE_SCALE = 0.08;

export default class Character extends Phaser.GameObjects.Sprite {
    board: Board;
    row: number;
    column: number;
    _heading: number;

    constructor(scene:Phaser.Scene, board:Board, texture:string) {
        super(scene, 0, 0, texture);
        this.setScale(IMAGE_SCALE);
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

    move(forward=true) {
        let row_step = 0;
        let col_step = 0;

        const facing_cell = this.facing_cell(forward);
        const current_cell = new Phaser.Math.Vector2(this.row, this.column);

        if (this.board.is_blocked(current_cell, facing_cell)) {
            return;
        }

        let direction_factor = forward ? 1 : -1;

        if (this.heading == 0) {
            col_step = 1 * direction_factor;
        } else if (this.heading == 90) {
            row_step = 1 * direction_factor;
        } else if (this.heading == 180) {
            col_step = -1 * direction_factor;
        } else if (this.heading == 270) {
            row_step = -1 * direction_factor;
        } else {
            console.error(`Unknown heading: ${this.heading}`);
        }

        
        this.position(facing_cell.x, facing_cell.y, true);
    }

    facing_cell(forward=true):Phaser.Math.Vector2 {
        const direction_step = forward ? 1 : -1;
        
        switch (this.heading) {
            case 0: {
                return new Phaser.Math.Vector2(this.row, this.column + direction_step);
            }
            case 90: {
                return new Phaser.Math.Vector2(this.row + direction_step, this.column);
            }
            case 180: {
                return new Phaser.Math.Vector2(this.row, this.column - direction_step);
            }
            case 270: {
                return new Phaser.Math.Vector2(this.row - direction_step, this.column)
            }

            throw new Error("Unexpected direction");
        }
        
    }

}