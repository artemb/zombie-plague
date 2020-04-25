import Phaser from 'phaser'

export default class BoardScene extends Phaser.Scene {
    constructor() {
        super('game-scene')
    }

    preload () {
        this.load.image('board', 'assets/board.png')
    }

    create () {
        this.add.image(700, 376, 'board')
    }
}