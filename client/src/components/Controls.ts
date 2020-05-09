import Phaser from "phaser";
import Board from "./Board";
import Character from "./Character";
import StateManager from "./StateManager";

enum Action {
  FORWARD = "FORWARD",
  BACKWARD = "BACKWARD",
  LEFT = "TURN_LEFT",
  RIGHT = "TURN_RIGHT",
}

export default class Controls extends Phaser.GameObjects.Container {
  zombie: Character;
  private stateManager: StateManager;
  private btn_group: Phaser.GameObjects.Group;

  static preload(scene:Phaser.Scene, prefix: string) {
    scene.load.html('nameform', prefix + 'assets/username.html')
  }

  constructor(scene: Phaser.Scene, x: integer, y: integer, character: Character, stateManager: StateManager) {
    // Initialize the controls container
    super(scene, x, y);
    this.setSize(
      +scene.game.config.width - Board.BOARD_WIDTH,
      +scene.game.config.height
    );
    scene.add.existing(this);

    this.stateManager = stateManager;
    this.stateManager.on('gamestatechange', () => this.onGameStateUpdate());

    this.drawControls(character)
  }

  drawControls(character) {
    this.btn_group = this.scene.add.group();
    let btn = this.create_button(50, 50, 1, () =>
        this.sendUpdate(character, Action.LEFT)
    );
    this.btn_group.add(btn);

    btn = this.create_button(120, 50, 4, () =>
        this.sendUpdate(character, Action.RIGHT)
    );
    this.btn_group.add(btn);

    btn = this.create_button(50, 120, 2, () =>
        this.sendUpdate(character, Action.FORWARD)
    );
    this.btn_group.add(btn);

    btn = this.create_button(120, 120, 3, () =>
        this.sendUpdate(character, Action.BACKWARD)
    );
    this.btn_group.add(btn);
  }

  sendUpdate(character: Character, action: Action) {
    this.stateManager.update(character.char_id, action);
  }

  create_button(x: integer, y: integer, frame: integer, onPointerDown: Function) {
    let btn = this.scene.add
      .sprite(x, y, "buttons", frame)
      .setScale(0.3)
      .setInteractive();
    btn.on("pointerdown", onPointerDown);
    this.add(btn);

    return btn;
  }

  onGameStateUpdate() {
    this.btn_group.setVisible(false);
    if (this.stateManager.turn['activePlayer'] == this.stateManager.playerId) {
      this.btn_group.setVisible(true);
    }
  }
}
