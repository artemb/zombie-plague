import Phaser from "phaser";
import Board from "./Board";
import Character from "./Character";
import StateManager from "./StateManager";

enum Action {
  FORWARD = "FORWARD",
  BACKWARD = "BACKWARD",
  LEFT = "TURN_LEFT",
  RIGHT = "TURN_RIGHT",
  STEP = "STEP",
  TURN = "TURN"
}

enum Step {
  FORWARD = "FORWARD",
  BACKWARD = "BACKWARD"
}

enum Turn {
  LEFT = "LEFT",
  RIGHT = "RIGHT"
}

export default class Controls extends Phaser.GameObjects.Container {
  character: Character;
  private stateManager: StateManager;
  private btn_group: Phaser.GameObjects.Group;
  private turnLabel: Phaser.GameObjects.Text;
  private remainingAPLabel: Phaser.GameObjects.Text;

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
    this.character = character;

    this.stateManager = stateManager;
    this.stateManager.on('gamestatechange', () => this.onGameStateUpdate());

    this.drawControls(character);
    this.drawText(character);
  }

  drawText(character) {
    this.turnLabel = this.scene.add.text(this.width / 2, 50, 'Your turn', {
      'color': '#FFF',
      'fontSize': '18px',
    }).setOrigin(0.5, 0.5);
    this.add(this.turnLabel);

    this.remainingAPLabel = this.scene.add.text(this.width / 2, 400, 'Remaining AP: 0', {
      'color': '#FFF',
      'fontSize': '16px',
    }).setOrigin(0.5, 0.5);
    this.add(this.remainingAPLabel);
  }

  drawControls(character) {
    this.btn_group = this.scene.add.group();
    let btn = this.create_button(50, 150, 1, () =>
        this.sendUpdate(character, Action.TURN, {turn: Turn.LEFT})
    );
    this.btn_group.add(btn);

    btn = this.create_button(120, 150, 4, () =>
        this.sendUpdate(character, Action.TURN, {turn: Turn.RIGHT})
    );
    this.btn_group.add(btn);

    btn = this.create_button(50, 220, 2, () =>
        this.sendUpdate(character, Action.STEP, {step: Step.FORWARD})
    );
    this.btn_group.add(btn);

    btn = this.create_button(120, 220, 3, () =>
        this.sendUpdate(character, Action.STEP, {step: Step.BACKWARD})
    );
    this.btn_group.add(btn);

  }

  sendUpdate(character: Character, action: Action, params: object = {}) {
    this.stateManager.update(character.char_id, action, params);
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
    if (this.stateManager.isCharactersTurn(this.character.char_id)) {
      this.turnLabel.setText('Your turn');
      this.btn_group.setVisible(true);
    } else {
      this.turnLabel.setText('Someone\'s turn');
    }
    this.remainingAPLabel.setText(`Remaining AP: ${this.stateManager.turn['remainingAP']}`)
  }
}
