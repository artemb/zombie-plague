import Phaser, { Tilemaps } from 'phaser'
import Board from '../components/Board.js'
import Character from '../components/Character.js'

export default class BoardScene extends Phaser.Scene {
    constructor() {
        super('game-scene')        
    }

    preload () {
        Board.preload(this)
        this.load.image('zombie', 'assets/characters/zombies/male/idle (1).png')
        this.load.spritesheet('buttons', 'assets/ui/controls.png', {frameWidth: 200, frameHeight: 215})
    }

    create_button(x, y, frame, onPointerDown, onPointerUp) {
        let btn = this.add.sprite(x, y, 'buttons', frame).setScale(0.3).setInteractive();
        btn.on('pointerdown', onPointerDown)
        btn.on('pointerup', onPointerUp)
        btn.on('pointerout', onPointerUp)
        return btn
    }

    create () {
        this.board = new Board(this, this.game.config.width - Board.BOARD_WIDTH / 2, this.game.config.height / 2)

        let zombie = new Character(this, this.board, 'zombie')
        zombie.position(3, 3)

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

        // let left_btn = this.create_button(50, 50, 1, move_callback(-1, 0), btn_up)
        // let right_btn = this.create_button(120, 50, 4, move_callback(1, 0), btn_up)
        // let fwd_btn = this.create_button(50, 120, 2, move_callback(0, -1), btn_up)
        // let bwd_btn = this.create_button(120, 120, 3, move_callback(0, 1), btn_up)
    }
}