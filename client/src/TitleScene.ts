import Phaser from 'phaser';
import StateManager from "./components/StateManager";
import UIButton from "./components/UIButton";

export default class TitleScene extends Phaser.Scene {
    private errorText: Phaser.GameObjects.Text;
    private usernameField: Phaser.GameObjects.DOMElement;
    private stateManager: StateManager;
    constructor() {
        super('Title');
    }

    create() {
        this.stateManager = this.game.registry.get('stateManager');
        this.checkIfRegistered();

        this.createCenteredText('Zombie Plague', 150, 40);
        this.createCenteredText('Hello, stranger. Come join our game.', 300, 28);
        this.createCenteredText('What is your name', 350, 20);
        this.errorText = this.createCenteredText('C\'mon, I really need your name', 500, 16).setVisible(false);
        this.usernameField = this.createUsernameField(this.scale.width / 2, 450);
        new UIButton(this, this.scale.width / 2, 550, 'Start game', () => this.onStartClick());
    }

    checkIfRegistered() {
        const player_id = localStorage.getItem('player_id');

        this.stateManager.checkRegistration(player_id).then((is_registered) => {
            if (is_registered) {
                this.scene.start('Board');
            }
        });

    }

    onStartClick() {
        // @ts-ignore
        let username = this.usernameField.getChildByID('user-name').value;
        if (username == null || username == '') {
            this.errorText.setVisible(true);
            return;
        }
        this.stateManager.registerPlayer(username).then(() => {
            this.scene.start('Lobby');
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
}