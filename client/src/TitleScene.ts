import Phaser from 'phaser';

export default class TitleScene extends Phaser.Scene {
    private errorText: Phaser.GameObjects.Text;
    constructor() {
        super('Title');
    }

    create() {
        this.createCenteredText('Zombie Plague', 150, 40);
        this.createCenteredText('Hello, stranger. Come join our game.', 300, 28);
        this.createCenteredText('What is your name', 350, 20);
        this.errorText = this.createCenteredText('C\'mon, I really need your name', 500, 16).setVisible(false);

        let field = this.add.dom(this.scale.width / 2, 450).createFromCache('name-field');

        this.createButton(this.scale.width / 2, 550, 'Start game',() => {
            // @ts-ignore
            let username = field.getChildByID('user-name').value;
            if (username == null || username == '') {
                this.errorText.setVisible(true);
                return;
            }
            this.scene.start('Board');
        });
    }

    createCenteredText(txt:string, y:number, fontSize:number) {
        return this.add.text(this.scale.width / 2, y, txt, {
            "fontSize": `${fontSize}px`,
            "color": '#FFF'
        }).setOrigin(.5, .5);
    }

    createButton(x: number, y: number, txt: string, onClick: Function) {
        const btn_img = this.add.image(x, y, 'ui-button', 'blue_button00.png');
        btn_img.setInteractive();

        const btn_label = this.add.text(0, 0, txt, {"fontSize": '18px', 'color': '#FFF', 'align': 'center'});
        Phaser.Display.Align.In.Center(btn_label, btn_img);

        btn_img.on('pointerdown', onClick);

        btn_img.on('pointerover', () => {
            btn_img.setFrame('blue_button02.png');
        });
        btn_img.on('pointerout', () => {
            btn_img.setFrame('blue_button00.png');
        })
    }
}