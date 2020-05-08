import Board from "./components/Board";
import Controls from "./components/Controls";
import Character from "./components/Character";
import c from "./components/consts";

export default class BootScene extends Phaser.Scene {
    constructor() {
        super("Boot");
    }

    preload() {
        Board.preload(this);
        Controls.preLoad(this);
        Character.preload(this);

        this.load.image("zombie", c.WEB_PREFIX + "assets/zombie.png");
        this.load.spritesheet("buttons", c.WEB_PREFIX + "assets/controls.png", {
            frameWidth: 200,
            frameHeight: 215,
        });
        this.load.atlasXML('ui-button', c.WEB_PREFIX + "assets/ui/blue_sheet.png",
            c.WEB_PREFIX + "assets/ui/blue_sheet.xml")

        this.load.html('name-field', c.WEB_PREFIX + 'assets/username.html');
    }

    create() {
        this.scene.run('Title');
    }
}
