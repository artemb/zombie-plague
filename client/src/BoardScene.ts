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
    this.stateManager.on('gamestatechange', () => this.onStateUpdate());


    this.stateManager.update();
  }

  onStateUpdate() {
    for (let char_id in this.stateManager.characters) {
      if (!this.stateManager.characters.hasOwnProperty(char_id)) {
        continue;
      }

      if (!this.board.getByName(char_id)) {
        let char_data = this.stateManager.characters[char_id];
        let character = new Character(this, this.board, char_data['player_id'], char_id, char_data['face'], this.stateManager);
        character.updateState(true);
        if (char_data['player_id'] == this.stateManager.playerId && !this.controls) {
          this.controls = new Controls(this, 0, 0, character, this.stateManager);
          this.controls.onGameStateUpdate();
        }
      }
    }
  }
}
