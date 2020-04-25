import Phaser from 'phaser'

export default class Character extends Phaser.GameObjects.Sprite {

    constructor(scene, texture) {
        super(scene, 0, 0, texture);
        this.setScale(0.08)
        scene.add.existing(this);
    }

}