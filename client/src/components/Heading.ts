export class Heading {
    frameSuffix: string;
    flipX: boolean;

    constructor(frameSuffix: string, flipX: boolean) {
        this.frameSuffix = frameSuffix;
        this.flipX = flipX;
    }
}

export const Headings = {
    RIGHT: new Heading('-right', false),
    DOWN: new Heading('-down', false),
    LEFT: new Heading('-right', true),
    UP: new Heading('-up', false),
}