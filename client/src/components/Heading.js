"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Heading = /** @class */ (function () {
    function Heading(angle, flip) {
        if (flip === void 0) { flip = 1; }
        this.angle = angle;
        this.flip = flip;
    }
    Object.defineProperty(Heading.prototype, "col_step", {
        get: function () {
            return -1 * (this.angle - 90) / 90 % 2;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Heading.prototype, "row_step", {
        get: function () {
            return this.angle / 90 % 2;
        },
        enumerable: true,
        configurable: true
    });
    Heading.from_angle = function (angle) {
        while (angle > 180) {
            angle -= 360;
        }
        while (angle < -90) {
            angle += 360;
        }
        switch (angle) {
            case 0: {
                return exports.Headings.RIGHT;
            }
            case 90: {
                return exports.Headings.DOWN;
            }
            case 180: {
                return exports.Headings.LEFT;
            }
            case -90: {
                return exports.Headings.UP;
            }
        }
        throw new Error("Unknown heading angle " + angle);
    };
    Heading.prototype.turn_left = function () {
        return Heading.from_angle(this.angle - 90);
    };
    Heading.prototype.turn_right = function () {
        return Heading.from_angle(this.angle + 90);
    };
    return Heading;
}());
exports.Heading = Heading;
exports.Headings = {
    RIGHT: new Heading(0),
    DOWN: new Heading(90),
    LEFT: new Heading(180, -1),
    UP: new Heading(-90)
};
//# sourceMappingURL=Heading.js.map