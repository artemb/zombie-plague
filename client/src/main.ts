import Phaser from "phaser";
import BoardScene from "./BoardScene";
import BootScene from "./BootScene";
import TitleScene from "./TitleScene";
import io from 'socket.io-client'

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
  private socket: SocketIOClient.Socket;
  constructor(config) {
    super(config);
    const socket = io('http://localhost:5000');
    this.registry.set('socket', socket);
  }
}

export default new Game(config);
