import Phaser from 'phaser';

export default class UIButton extends Phaser.GameObjects.Image {
    constructor(scene: Phaser.Scene, x: number, y: number, txt: string, onClick: Function) {
        super(scene, x, y, 'ui-button', 'blue_button00.png');
        this.setInteractive();
        scene.add.existing(this);

        const btn_label = scene.add.text(0, 0, txt, {"fontSize": '18px', 'color': '#FFF', 'align': 'center'});
        Phaser.Display.Align.In.Center(btn_label, this);

        this.on('pointerdown', onClick);

        this.on('pointerover', () => {
            this.setFrame('blue_button02.png');
        });
        this.on('pointerout', () => {
            this.setFrame('blue_button00.png');
        })

    }
}