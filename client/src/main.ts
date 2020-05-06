import Phaser from "phaser";
import BoardScene from "./BoardScene";

const config = {
  type: Phaser.AUTO,
  width: 1400,
  height: 752,
  physics: {},
  scene: [BoardScene],
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
