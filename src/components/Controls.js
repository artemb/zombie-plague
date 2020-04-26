import Phaser from 'phaser'
import Board from './Board.js'

export default class Controls extends Phaser.GameObjects.Container {
    constructor(scene, x, y, zombie) {
        super(scene, x, y)
        this.setSize(scene.game.config.width - Board.BOARD_WIDTH, scene.game.config.height)
        console.log(scene.game.config.width - Board.BOARD_WIDTH, scene.game.config.height)

        scene.add.existing(this);

        this.zombie = zombie

        // let gr = scene.add.graphics({ fillStyle: { color: 0x0000aa } });
        // this.add(gr)
        // gr.fillRectShape(new Phaser.Geom.Rectangle(0, 0, Math.max(50, this.width), Math.max(70, this.height)))

        function move_callback(x, y) {
            return function (pointer) {
                this.setTint(0xFF0000)
                zombie.move_forward();
            }
        }

        function btn_up(pointer) {
            this.clearTint()
        }

        let left_btn = this.create_button(50, 50, 1, () => zombie.turn_left(), btn_up)
        let right_btn = this.create_button(120, 50, 4, () => zombie.turn_right(), btn_up)
        let fwd_btn = this.create_button(50, 120, 2, () => zombie.move_forward(), btn_up)
        let bwd_btn = this.create_button(120, 120, 3, move_callback(0, 1), btn_up)
    }

    create_button(x, y, frame, onPointerDown, onPointerUp) {
        let btn = this.scene.add.sprite(x, y, 'buttons', frame).setScale(0.3).setInteractive();
        btn.on('pointerdown', onPointerDown)
        btn.on('pointerup', onPointerUp)
        btn.on('pointerout', onPointerUp)
        this.add(btn)

        return btn
    }    
}