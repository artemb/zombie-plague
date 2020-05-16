import Phaser from 'phaser';
import StateManager, {GameStatus} from "./components/StateManager";
import UIButton from "./components/UIButton";

export default class LobbyScene extends Phaser.Scene {
    private state: StateManager;
    constructor() {
        super('Lobby');
    }

    create() {
        this.state = this.game.registry.get('stateManager');
        new UIButton(this, this.scale.width / 2, 550, 'Start game', () => this.onStartClick())

        this.state.on('gamestatechange', () => this.onGameStateChange());
        this.onGameStateChange();

    }

    private onGameStateChange() {
        if (this.state.game['status'] == GameStatus.STARTED) {
            this.scene.start('Board');
            return;
        }

        let playerPosition = 1
        Object.values(this.state.players).forEach((player) => {
            this.createPlayerLabel(player, playerPosition++);
        });
    }

    private createPlayerLabel(player: object, position: number) {
        this.add.text(100, 100 + 100 * position, `${player["name"]}`);
    }

    private onStartClick() {
        this.scene.start('Board');
    }
}