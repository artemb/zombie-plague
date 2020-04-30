import Phaser from 'phaser'
import Board from './Board'
import Character from './Character'

export default class Controls extends Phaser.GameObjects.Container {
    zombie: Character

    constructor(scene:Phaser.Scene, x:integer, y:integer, zombie:Character) {
        super(scene, x, y)
        this.setSize(+scene.game.config.width - Board.BOARD_WIDTH, +scene.game.config.height)
        console.log(+scene.game.config.width - Board.BOARD_WIDTH, scene.game.config.height)

        scene.add.existing(this);

        this.zombie = zombie

        let left_btn = this.create_button(50, 50, 1, () => zombie.turn_left())
        let right_btn = this.create_button(120, 50, 4, () => zombie.turn_right())
        let fwd_btn = this.create_button(50, 120, 2, () => zombie.move(true))
        let bwd_btn = this.create_button(120, 120, 3, () => zombie.move(false))
    }

    create_button(x:integer, y:integer, frame:integer, onPointerDown:Function) {
        let btn = this.scene.add.sprite(x, y, 'buttons', frame).setScale(0.3).setInteractive();
        btn.on('pointerdown', onPointerDown)
        this.add(btn)

        return btn
    }    
}