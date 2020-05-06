"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
var phaser_1 = __importDefault(require("phaser"));
var Grid_1 = __importDefault(require("./Grid"));
var consts_1 = __importDefault(require("./consts"));
var GRID_WIDTH = 24;
var GRID_HEIGHT = 20;
var BOARD_WIDTH = 903;
var BOARD_HEIGHT = 752;
var CELL_WIDTH = BOARD_WIDTH / GRID_WIDTH;
var CELL_HEIGHT = BOARD_HEIGHT / GRID_HEIGHT;
var obstacles = [
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
    [9, 5],
];
var walls = [
    [
        [15, 1],
        [15, 2],
    ],
    [
        [16, 1],
        [16, 2],
    ],
    [
        [14, 2],
        [15, 2],
    ],
];
var BoardScene = /** @class */ (function (_super) {
    __extends(BoardScene, _super);
    function BoardScene(scene, x, y) {
        var _this = _super.call(this, scene, x, y) || this;
        _this.grid = new Grid_1.default(24, 20);
        _this.setSize(BOARD_WIDTH, BOARD_HEIGHT);
        scene.add.existing(_this);
        _this.add(scene.add.image(0, 0, "board"));
        return _this;
    }
    Object.defineProperty(BoardScene, "BOARD_WIDTH", {
        get: function () {
            return BOARD_WIDTH;
        },
        enumerable: true,
        configurable: true
    });
    BoardScene.prototype.getPositionOnGrid = function (address) {
        var x = -this.width / 2 + address[0] * CELL_WIDTH - CELL_WIDTH / 2;
        var y = -this.height / 2 + address[1] * CELL_HEIGHT - CELL_HEIGHT / 2;
        return new phaser_1.default.Math.Vector2(x, y);
    };
    BoardScene.preload = function (scene) {
        scene.load.image("board", consts_1.default.WEB_PREFIX + "assets/board.png");
    };
    BoardScene.prototype.is_blocked = function (from, to) {
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
    };
    return BoardScene;
}(phaser_1.default.GameObjects.Container));
exports.default = BoardScene;
//# sourceMappingURL=Board.js.map