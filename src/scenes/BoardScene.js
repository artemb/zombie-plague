import Phaser from 'phaser'

const GRID_WIDTH = 24
const GRID_HEIGHT = 24
const BOARD_WIDTH = 903
const BOARD_HEIGHT = 752
const CELL_WIDTH = BOARD_WIDTH / GRID_WIDTH
const CELL_HEIGHT = BOARD_HEIGHT / GRID_HEIGHT

export default class BoardScene extends Phaser.Scene {
    constructor() {
        super('game-scene')
        
    }

    preload () {
        this.load.image('board', 'assets/board.png')
        this.load.image('zombie', 'assets/characters/zombies/male/idle (1).png')
        this.load.spritesheet('buttons', 'assets/ui/controls.png', {frameWidth: 200, frameHeight: 215})
        console.log(this.game)
    }

    create_button(x, y, frame, onPointerDown, onPointerUp) {
        let btn = this.add.sprite(x, y, 'buttons', frame).setScale(0.3).setInteractive();
        btn.on('pointerdown', onPointerDown)
        btn.on('pointerup', onPointerUp)
        btn.on('pointerout', onPointerUp)
        return btn
    }

    create () {
        this.add.image(this.game.config.width / 2, this.game.config.height / 2, 'board')
        let zombie = this.add.image(this.place_on_grid(1, 1, 'x'), 
            this.place_on_grid(1, 1, 'y'), 'zombie').setScale(0.08)

        function move_callback(x, y) {
            return function (pointer) {
                this.setTint(0xFF0000)
                zombie.x += x * CELL_WIDTH;
                zombie.y += y * CELL_WIDTH;
            }
        }

        function btn_up(pointer) {
            this.clearTint()
        }

        let left_btn = this.create_button(50, 50, 1, move_callback(-1, 0), btn_up)
        let right_btn = this.create_button(120, 50, 4, move_callback(1, 0), btn_up)
        let fwd_btn = this.create_button(50, 120, 2, move_callback(0, -1), btn_up)
        let bwd_btn = this.create_button(120, 120, 3, move_callback(0, 1), btn_up)
    }

    place_on_grid(grid_x, grid_y, axis) {
        const BOARD_X_OFFSET = (this.game.config.width - BOARD_WIDTH) / 2
        if (axis == 'x') {
            return BOARD_X_OFFSET + CELL_WIDTH * grid_x - CELL_WIDTH / 2
        } else {
            return CELL_HEIGHT * grid_y - CELL_HEIGHT / 2
        }
    }
}