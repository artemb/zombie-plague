import Phaser from "phaser";
import Board from "./components/Board";
import Character from "./components/Character";
import Controls from "./components/Controls";
import StateManager from "./components/StateManager";

export default class BoardScene extends Phaser.Scene {
  private board: Board;
  private controls: Controls;
  private stateManager: StateManager;

  constructor() {
    super("Board");
  }

  create() {
    this.board = new Board(
      this,
      +this.game.config.width - Board.BOARD_WIDTH / 2,
      +this.game.config.height / 2
    );

    this.stateManager = this.game.registry.get('stateManager');

    let zombie = new Character(this, this.board, this.stateManager.playerId, 'char', this.stateManager);
    this.controls = new Controls(this, 0, 0, zombie, this.stateManager);

    this.stateManager.update();
  }
}
