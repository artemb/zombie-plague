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
var Heading_1 = require("./Heading");
var IMAGE_SCALE = 0.08;
var Character = /** @class */ (function (_super) {
    __extends(Character, _super);
    function Character(scene, board, texture, socket) {
        var _this = _super.call(this, scene, 0, 0, texture) || this;
        _this.setScale(IMAGE_SCALE);
        scene.add.existing(_this);
        _this.board = board;
        board.add(_this);
        _this.address = [1, 1];
        _this._heading = Heading_1.Headings.RIGHT;
        _this.char_id = null;
        _this.socket = socket;
        socket.on('registration', function (data) {
            _this.char_id = data['id'];
        });
        socket.on("message", function (data) {
            _this.position(data["characters"][_this.char_id]["address"], true);
            if (data["characters"][_this.char_id]["direction"] == "UP") {
                _this.heading = Heading_1.Headings.UP;
            }
            if (data["characters"][_this.char_id]["direction"] == "DOWN") {
                _this.heading = Heading_1.Headings.DOWN;
            }
            if (data["characters"][_this.char_id]["direction"] == "LEFT") {
                _this.heading = Heading_1.Headings.LEFT;
            }
            if (data["characters"][_this.char_id]["direction"] == "RIGHT") {
                _this.heading = Heading_1.Headings.RIGHT;
            }
        });
        return _this;
    }
    Object.defineProperty(Character.prototype, "heading", {
        /*
      
          // the angle is 0 for right, 90 for down, 180 for left, 270 for up
          set heading(heading) {
              if (heading < 0) {
                  heading += 360;
              } else if (heading >= 360) {
                  heading -= 360;
              }
      
              switch (heading) {
                  case HEADING.RIGHT: {
                      this.angle = 0;
                      this.scaleX = IMAGE_SCALE;
                      break;
                  }
                  case HEADING.DOWN: {
                      this.angle = 90;
                      this.scaleX = IMAGE_SCALE;
                      break;
                  }
                  case HEADING.LEFT: {
                      this.angle = 0;
                      this.scaleX = -IMAGE_SCALE;
                      break;
                  }
                  case HEADING.UP: {
                      this.angle = -90;
                      this.scaleX = IMAGE_SCALE;
                  }
              }
      
              this._heading = heading;
          }
          */
        get: function () {
            return this._heading;
        },
        set: function (heading) {
            this._heading = heading;
            this.angle = this._heading.angle;
            this.scaleX = this._heading.flip * IMAGE_SCALE;
            if (this._heading.flip == -1) {
                this.angle -= 180;
            }
        },
        enumerable: true,
        configurable: true
    });
    Character.prototype.turn_left = function () {
        this.heading = this.heading.turn_left();
    };
    Character.prototype.turn_right = function () {
        this.heading = this.heading.turn_right();
    };
    Character.prototype.position = function (address, animate) {
        if (animate === void 0) { animate = false; }
        this.address = address;
        var v = this.board.getPositionOnGrid(address);
        if (animate) {
            this.scene.tweens.add({
                targets: this,
                x: v.x,
                y: v.y,
                ease: phaser_1.default.Math.Easing.Quartic,
                duration: 500,
                yoyo: false,
            });
        }
        else {
            this.x = v.x;
            this.y = v.y;
        }
    };
    Character.prototype.move = function (forward) {
        if (forward === void 0) { forward = true; }
        var facing_cell = this.board.grid.facingAddress(this.address, this.heading, forward);
        if (this.board.is_blocked(this.address, facing_cell)) {
            return;
        }
        this.position(facing_cell, true);
    };
    return Character;
}(phaser_1.default.GameObjects.Sprite));
exports.default = Character;
//# sourceMappingURL=Character.js.map