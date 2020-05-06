"use strict";
// A component to make handling grid addressing easier
Object.defineProperty(exports, "__esModule", { value: true });
var Grid = /** @class */ (function () {
    function Grid(cols, rows) {
        this.cols = cols;
        this.rows = rows;
    }
    Grid.prototype.facingAddress = function (from, heading, forward) {
        if (forward === void 0) { forward = true; }
        var direction_step = forward ? 1 : -1;
        return [from[0] + heading.col_step * direction_step, from[1] + heading.row_step * direction_step];
    };
    Grid.prototype.sameAddress = function (one, two) {
        return one[0] == two[0] && one[1] == two[1];
    };
    Grid.prototype.isOutOfBounds = function (address) {
        return address[0] < 1 || address[0] > this.cols || address[1] < 1 || address[1] > this.rows;
    };
    Grid.prototype.addressInList = function (address, list) {
        return list.some(function (item) { return address[0] == item[0] && address[1] == item[1]; });
    };
    Grid.prototype.hitsWall = function (from, to, walls) {
        var _this = this;
        return walls.some(function (wall) {
            if (_this.sameAddress(from, wall[0]) && _this.sameAddress(to, wall[1])) {
                return true;
            }
            if (_this.sameAddress(from, wall[1]) && _this.sameAddress(to, wall[0])) {
                return true;
            }
            return false;
        });
    };
    return Grid;
}());
exports.default = Grid;
//# sourceMappingURL=Grid.js.map