import Phaser from 'phaser'
import Grid from './Grid'

const GRID_WIDTH = 24
const GRID_HEIGHT = 20
const BOARD_WIDTH = 903
const BOARD_HEIGHT = 752
const CELL_WIDTH = BOARD_WIDTH / GRID_WIDTH
const CELL_HEIGHT = BOARD_HEIGHT / GRID_HEIGHT

const obstacles = [
    [5, 3],
    [5, 4],
    [5, 5],
    [6, 3],
    [6, 4],
    [6, 5],
    [7, 3],
    [7, 4],
    [7, 5],
    [8, 3],
    [8, 4],
    [8, 5],
    [9, 3],
    [9, 4],
    [9, 5]
]

const walls = [
    [[15, 1], [15, 2]],
    [[16, 1], [16, 2]],
    [[14, 2], [15, 2]]
]


export default class BoardScene extends Phaser.GameObjects.Container {
    grid: Grid

    static get BOARD_WIDTH() {
        return BOARD_WIDTH
    }

    getPositionOnGrid(address:integer[]):Phaser.Math.Vector2 {
        let x:number = - this.width / 2 + address[0] * CELL_WIDTH - CELL_WIDTH / 2;
        let y:number = -this.height / 2 + address[1] * CELL_HEIGHT - CELL_HEIGHT / 2;

        return new Phaser.Math.Vector2(x, y)
    }

    constructor (scene:Phaser.Scene, x:integer, y:integer) {
        super(scene, x, y)

        this.grid = new Grid(24, 20);
        this.setSize(BOARD_WIDTH, BOARD_HEIGHT)
        scene.add.existing(this);
        this.add(scene.add.image(0, 0, 'board'))

    }


    static preload(scene:Phaser.Scene) {
        scene.load.image('board', '/dist/assets/board.png')
    }

    is_blocked(from:integer[], to:integer[]) {
        // check boundaries
        if (this.grid.isOutOfBounds(to)) {
            return true;
        }

        // check for static obstacles
        if (this.grid.addressInList(to, obstacles)) {
            return true;
        }

        // check for walls
        if (this.grid.hitsWall(from, to, walls)) {
            return true;
        }
    }
}