import Phaser from 'phaser';
import SocketIOClient from 'socket.io-client'

export default class TitleScene extends Phaser.Scene {
    private errorText: Phaser.GameObjects.Text;
    private usernameField: Phaser.GameObjects.DOMElement;
    private socket: SocketIOClient.Socket;
    constructor() {
        super('Title');
    }

    create() {
        this.socket = this.game.registry.get('socket')

        this.createCenteredText('Zombie Plague', 150, 40);
        this.createCenteredText('Hello, stranger. Come join our game.', 300, 28);
        this.createCenteredText('What is your name', 350, 20);
        this.errorText = this.createCenteredText('C\'mon, I really need your name', 500, 16).setVisible(false);
        this.usernameField = this.createUsernameField(this.scale.width / 2, 450);
        this.createButton(this.scale.width / 2, 550, 'Start game',() => {this.onStartClick()});
    }

    onStartClick() {
        // @ts-ignore
        let username = this.usernameField.getChildByID('user-name').value;
        if (username == null || username == '') {
            this.errorText.setVisible(true);
            return;
        }
        this.socket.emit("join", { username: username, room: "Room 1" });
        this.socket.on('joined', (data) => {
            this.game.registry.set('player_id', data['player_id']);
            this.scene.start('Board');
        });
    }

    createUsernameField(x, y) {
        let field = this.add.dom(x, y).createFromCache('name-field');
        field.addListener('keyup')
        field.on('keyup', (event) => {
            if (event.keyCode === 13) {
                this.onStartClick();
            }
        })
        return field;
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