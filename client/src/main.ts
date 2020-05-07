import Phaser from "phaser";
import BoardScene from "./BoardScene";
import BootScene from "./BootScene";

const config = {
  type: Phaser.AUTO,
  width: 1400,
  height: 752,
  physics: {},
  scene: [BootScene, BoardScene],
  parent: 'game-container',
  dom: {
    createContainer: true
  },
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH,
  },
};

export default new Phaser.Game(config);
