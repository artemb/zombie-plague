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
    }

    position(row, column) {
        this.row = row;
        this.column = column;
        this.board.positionOnGrid(this, row, column);
    }

    move_forward() {
        this.position(this.row + 1, this.column);
    }

}