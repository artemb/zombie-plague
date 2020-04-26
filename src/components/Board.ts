import Phaser from 'phaser'

const GRID_WIDTH = 24
const GRID_HEIGHT = 20
const BOARD_WIDTH = 903
const BOARD_HEIGHT = 752
const CELL_WIDTH = BOARD_WIDTH / GRID_WIDTH
const CELL_HEIGHT = BOARD_HEIGHT / GRID_HEIGHT

const obstacles = [
    [3, 5],
    [4, 5],
    [5, 5],
    [3, 6],
    [4, 6],
    [5, 6],
    [3, 7],
    [4, 7],
    [5, 7],
    [3, 8],
    [4, 8],
    [5, 8],
    [3, 9],
    [4, 9],
    [5, 9]
]

const walls = [
    [1, 15, 2, 15],
    [1, 16, 2, 16],
    [2, 14, 2, 15]
]


export default class BoardScene extends Phaser.GameObjects.Container {
    static get BOARD_WIDTH() {
        return BOARD_WIDTH
    }

    getPositionOnGrid(row:integer, column:integer):Phaser.Math.Vector2 {
        let x:number = - this.width / 2 + column * CELL_WIDTH - CELL_WIDTH / 2;
        let y:number = -this.height / 2 + row * CELL_HEIGHT - CELL_HEIGHT / 2;
        return new Phaser.Math.Vector2(x, y)
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

    is_blocked(from:Phaser.Math.Vector2, to:Phaser.Math.Vector2) {
        // check world boundaries
        if (to.x < 1 || to.x > GRID_HEIGHT || to.y < 1 || to.y > GRID_WIDTH) {
            return true;
        }

        // check for static obstacles
        if (obstacles.some((val) => val[0] == to.x && val[1] == to.y)) {
            return true;
        }

        // check for walls
        return walls.some((wall) => {
            if (wall[0] == from.x && wall[1] == from.y && wall[2] == to.x && wall[3] == to.y) {
                return true;
            }
            if (wall[0] == to.x && wall[1] == to.y && wall[2] == from.x && wall[3] == from.y) {
                return true;
            }
            return false;
        })

        
    }

}