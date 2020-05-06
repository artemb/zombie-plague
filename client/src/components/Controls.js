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
var Board_1 = __importDefault(require("./Board"));
var Action;
(function (Action) {
    Action["FORWARD"] = "FORWARD";
    Action["BACKWARD"] = "BACKWARD";
    Action["LEFT"] = "TURN_LEFT";
    Action["RIGHT"] = "TURN_RIGHT";
})(Action || (Action = {}));
var Controls = /** @class */ (function (_super) {
    __extends(Controls, _super);
    function Controls(scene, x, y, zombie, socket) {
        var _this = _super.call(this, scene, x, y) || this;
        _this.setSize(+scene.game.config.width - Board_1.default.BOARD_WIDTH, +scene.game.config.height);
        scene.add.existing(_this);
        _this.zombie = zombie;
        _this.socket = socket;
        var left_btn = _this.create_button(50, 50, 1, function () {
            return _this.sendUpdate(Action.LEFT);
        });
        var right_btn = _this.create_button(120, 50, 4, function () {
            return _this.sendUpdate(Action.RIGHT);
        });
        var fwd_btn = _this.create_button(50, 120, 2, function () {
            return _this.sendUpdate(Action.FORWARD);
        });
        var bwd_btn = _this.create_button(120, 120, 3, function () {
            return _this.sendUpdate(Action.BACKWARD);
        });
        return _this;
    }
    Controls.prototype.sendUpdate = function (action) {
        this.socket.emit("update", { action: action });
    };
    Controls.prototype.create_button = function (x, y, frame, onPointerDown) {
        var btn = this.scene.add
            .sprite(x, y, "buttons", frame)
            .setScale(0.3)
            .setInteractive();
        btn.on("pointerdown", onPointerDown);
        this.add(btn);
        return btn;
    };
    return Controls;
}(phaser_1.default.GameObjects.Container));
exports.default = Controls;
//# sourceMappingURL=Controls.js.map