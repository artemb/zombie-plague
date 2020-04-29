import Phaser, { Tilemaps } from 'phaser'
import Board from '../components/Board'
import Character from '../components/Character'
import Controls from '../components/Controls'

export default class BoardScene extends Phaser.Scene {
    board: Board
    controls: Controls
    
    constructor() {
        super('game-scene')        
    }

    preload () {
        Board.preload(this)
        this.load.image('zombie', 'static/assets/characters/zombies/male/idle (1).png')
        this.load.spritesheet('buttons', 'static/assets/ui/controls.png', {frameWidth: 200, frameHeight: 215})
    }



    create () {
        this.board = new Board(this, +this.game.config.width - Board.BOARD_WIDTH / 2, +this.game.config.height / 2)

        let zombie = new Character(this, this.board, 'zombie')
        zombie.position([3, 3])

        this.controls = new Controls(this, 0, 0, zombie)

    }
}