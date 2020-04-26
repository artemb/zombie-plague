// A component to make handling grid addressing easier

export default class Grid {
    cols: number;
    rows: number;

    constructor(cols:integer, rows:integer) {
        this.cols = cols;
        this.rows = rows;
    }

    facingAddress(from:integer[], heading:integer, forward=true) {
        const direction_step = forward ? 1 : -1;
        
        switch (heading) {
            case 0: {
                return [from[0] + direction_step,  from[1]]
            }
            case 90: {
                return [from[0], from[1] + direction_step]
            }
            case 180: {
                return [from[0] - direction_step, from[1]]
            }
            case 270: {
                return [from[0], from[1] - direction_step]
            }
        }

        throw new Error(`Unknown heading ${heading}`)
    }

    sameAddress(one:integer[], two:integer[]) {
        return one[0] == two[0] && one[1] == two[1]
    }

    isOutOfBounds(address:integer[]) {
        return address[0] < 1 || address[0] > this.cols || address[1] < 1 || address[1] > this.rows;
    }

    addressInList(address:integer[], list:integer[][]) {
        return list.some((item) => address[0] == item[0] && address[1] == item[1]);
    }

    hitsWall(from:integer[], to:integer[], walls:integer[][][]) {
        return walls.some((wall) => {
            if (this.sameAddress(from, wall[0]) && this.sameAddress(to, wall[1])) {
                return true;
            }
            if (this.sameAddress(from, wall[1]) && this.sameAddress(to, wall[0])) {
                return true;
            }
            return false;
        });
    }

}