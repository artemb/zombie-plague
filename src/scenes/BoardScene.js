import Phaser from 'phaser'

const GRID_WIDTH = 24
const GRID_HEIGHT = 24
const SCREEN_WIDTH = 1400
const SCREEN_HEIGHT = 752
const BOARD_WIDTH = 903
const BOARD_HEIGHT = SCREEN_HEIGHT
const CELL_WIDTH = BOARD_WIDTH / GRID_WIDTH
const CELL_HEIGHT = BOARD_HEIGHT / GRID_HEIGHT

function place_on_grid(grid_x, grid_y, axis) {
    const BOARD_X_OFFSET = (SCREEN_WIDTH - BOARD_WIDTH) / 2
    if (axis == 'x') {
        return BOARD_X_OFFSET + CELL_WIDTH * grid_x - CELL_WIDTH / 2
    } else {
        return CELL_HEIGHT * grid_y - CELL_HEIGHT / 2
    }
}

export default class BoardScene extends Phaser.Scene {
    constructor() {
        super('game-scene')
    }

    preload () {
        this.load.image('board', 'assets/board.png')
        this.load.image('zombie', 'assets/characters/zombies/male/idle (1).png')
        this.load.spritesheet('buttons', 'assets/ui/controls.png', {frameWidth: 200, frameHeight: 215})
    }

    create () {
        this.add.image(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 'board')
        this.add.image(place_on_grid(1, 1, 'x'), place_on_grid(1, 1, 'y'), 'zombie').setScale(0.08)
        this.add.sprite(50, 50, 'buttons', 1).setScale(0.3)
        this.add.sprite(50, 120, 'buttons', 2).setScale(0.3)
        this.add.sprite(50, 190, 'buttons', 3).setScale(0.3)
        this.add.sprite(50, 260, 'buttons', 4).setScale(0.3)
    }
}