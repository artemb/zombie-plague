import Phaser from 'phaser'

const GRID_WIDTH = 24
const GRID_HEIGHT = 20
const BOARD_WIDTH = 903
const BOARD_HEIGHT = 752
const CELL_WIDTH = BOARD_WIDTH / GRID_WIDTH
const CELL_HEIGHT = BOARD_HEIGHT / GRID_HEIGHT


export default class BoardScene extends Phaser.GameObjects.Container {
    static get BOARD_WIDTH() {
        return BOARD_WIDTH
    }

    positionOnGrid(object:Phaser.GameObjects.Sprite, row:integer, column:integer) {
        object.x = - this.width / 2 + column * CELL_WIDTH - CELL_WIDTH / 2;
        object.y = -this.height / 2 + row * CELL_HEIGHT - CELL_HEIGHT / 2;
        return object;
    }    

    constructor (scene:Phaser.Scene, x:integer, y:integer) {
        super(scene, x, y)

        this.setSize(BOARD_WIDTH, BOARD_HEIGHT)
        scene.add.existing(this);
        this.add(scene.add.image(0, 0, 'board'))

    }


    static preload(scene:Phaser.Scene) {
        scene.load.image('board', 'assets/board.png')
    }



}