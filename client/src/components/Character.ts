import Phaser from "phaser";
import Board from "./Board";
import {Heading, Headings} from "./Heading";
import StateManager from "./StateManager";

export default class Character extends Phaser.GameObjects.Sprite {
    board: Board;
    address: number[] = [1, 1];
    _heading: Heading = Headings.RIGHT;
    char_id: string;
    frameName: string = 'char';
    private stateManager: StateManager;

    static preload(scene: Phaser.Scene, prefix: string) {
        scene.load.image('char1-down', prefix + 'assets/chars/2.1idle.gif')
        scene.load.image('char1-right', prefix + 'assets/chars/2.2idle.gif')
        scene.load.image('char1-up', prefix + 'assets/chars/2.3idle.gif')

        scene.load.image('char2-down', prefix + 'assets/chars/1.1idle.gif')
        scene.load.image('char2-right', prefix + 'assets/chars/1.2idle.gif')
        scene.load.image('char2-up', prefix + 'assets/chars/1.3idle.gif')

        scene.load.image('char3-down', prefix + 'assets/chars/3.1idle.gif')
        scene.load.image('char3-right', prefix + 'assets/chars/3.2idle.gif')
        scene.load.image('char3-up', prefix + 'assets/chars/3.4idle.gif')

        scene.load.image('char4-down', prefix + 'assets/chars/4.1idle.gif')
        scene.load.image('char4-right', prefix + 'assets/chars/4.2idle.gif')
        scene.load.image('char4-up', prefix + 'assets/chars/4.3idle.gif')

    }

    constructor(scene: Phaser.Scene, board: Board, char_id: string, frameName: string, stateManager: StateManager) {
        super(scene, 0, 0, frameName + '-down');
        this.board = board;
        this.frameName = frameName;
        this.char_id = char_id;
        this.name = char_id;
        this.stateManager = stateManager;

        scene.add.existing(this);
        board.add(this);

        this.setupEvents();
    }

    private setupEvents() {
        this.stateManager.on('gamestatechange', () => this.updateState());
    }

    updateState(initial=false) {
        this.position(this.stateManager.characters[this.char_id]["address"], !initial);
        let direction = this.stateManager.characters[this.char_id]["direction"];
        this.heading = Headings[direction];
    }

    set heading(heading: Heading) {
        this._heading = heading;

        this.setTexture(this.frameName + heading.frameSuffix);
        this.flipX = heading.flipX;
    }

    get heading() {
        return this._heading;
    }

    position(address: integer[], animate = false) {
        this.address = address;
        let v: Phaser.Math.Vector2 = this.board.getPositionOnGrid(address);

        if (animate) {
            this.scene.tweens.add({
                targets: this,
                x: v.x,
                y: v.y,
                ease: Phaser.Math.Easing.Quartic,
                duration: 500,
                yoyo: false,
            });
        } else {
            this.x = v.x;
            this.y = v.y;
        }
    }
}
