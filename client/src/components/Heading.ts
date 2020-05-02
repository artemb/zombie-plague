
export class Heading {
    angle: number;
    flip: integer;

    constructor(angle:integer, flip = 1) {
        this.angle = angle;
        this.flip = flip;
    }

    get col_step():integer {
        return -1 * (this.angle - 90) / 90 % 2;
    }

    get row_step():integer {
        return this.angle / 90 % 2;
    }

    static from_angle(angle:integer):Heading {
        while (angle > 180) {
            angle -= 360;
        }
        while (angle < -90) {
            angle += 360;
        }
        switch (angle) {
            case 0: {
                return Headings.RIGHT;
            }
            case 90: {
                return Headings.DOWN;
            }
            case 180: {
                return Headings.LEFT;
            }
            case -90: {
                return Headings.UP;
            }
        }

        throw new Error(`Unknown heading angle ${angle}`)
    }

    turn_left() {
        return Heading.from_angle(this.angle - 90)
    }

    turn_right() {
        return Heading.from_angle(this.angle + 90)
    }
}

export const Headings = {
    RIGHT: new Heading(0),
    DOWN: new Heading(90),
    LEFT: new Heading(180, -1),
    UP: new Heading(-90)
}