import Phaser from 'phaser';

export default class TitleScene extends Phaser.Scene {
    constructor() {
        super('Title');
    }

    preload() {

    }

    create() {
        this.add.text(+this.scale.width / 2, +this.scale.height / 2 - 100, 'Hello, stranger. Come join our game', {
            "font-size": '20px',
            "fill": '#FFF',
            "align": 'center'
        }).setOrigin(.5, .5);

        const btn_img = this.add.image(+this.game.config.width / 2, +this.game.config.height / 2, 'ui-button', 'blue_button00.png');
        btn_img.setInteractive();

        const btn_label = this.add.text(0, 0, 'Start game', {"font-size": '18px', 'fill': '#FFF', 'align': 'center'});
        Phaser.Display.Align.In.Center(btn_label, btn_img);

        btn_img.on('pointerdown', () => {
            console.log('Start button pressed!');
            this.scene.start('Board');
        })
    }
}