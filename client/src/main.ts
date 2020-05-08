import Phaser from "phaser";
import BoardScene from "./BoardScene";
import BootScene from "./BootScene";
import TitleScene from "./TitleScene";
import io from 'socket.io-client'
import StateManager from "./components/StateManager";

const config = {
  type: Phaser.AUTO,
  width: 1400,
  height: 752,
  physics: {},
  scene: [BootScene, TitleScene, BoardScene],
  parent: 'game-container',
  dom: {
    createContainer: true
  },
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH,
  },
  roundPixels: true,
};

class Game extends Phaser.Game {
  constructor(config) {
    super(config);
    const socket:SocketIOClient.Socket = io(location.hostname + ':5000');
    const stateManager = new StateManager(socket);
    this.registry.set('stateManager', stateManager);
    this.registry.set('socket', socket);
  }
}

export default new Game(config);
