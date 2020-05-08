import Phaser from "phaser";
import Board from "./Board";
import {Heading, Headings} from "./Heading";

export default class Character extends Phaser.GameObjects.Sprite {
    board: Board;
    address: number[] = [1, 1];
    _heading: Heading = Headings.RIGHT;
    socket: SocketIOClient.Socket;
    char_id: string;
    frameName: string = 'char';

    static preload(scene: Phaser.Scene, prefix: string) {
        scene.load.image('char-down', prefix + 'assets/chars/2.1idle.gif')
        scene.load.image('char-right', prefix + 'assets/chars/2.2idle.gif')
        scene.load.image('char-up', prefix + 'assets/chars/2.3idle.gif')
    }

    constructor(scene: Phaser.Scene, board: Board, char_id: string, frameName: string) {
        super(scene, 0, 0, frameName + '-down');
        this.board = board;
        this.frameName = frameName;
        this.char_id = char_id;

        scene.add.existing(this);
        board.add(this);

        this.setUpSocketEvents();
    }

    private setUpSocketEvents() {
        this.socket = this.scene.game.registry.get('socket');

        this.socket.on("message", (data: object) => {
            this.position(data["characters"][this.char_id]["address"], true);
            let direction = data["characters"][this.char_id]["direction"];
            this.heading = Headings[direction];
        });
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
