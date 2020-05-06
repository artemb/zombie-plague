var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
System.register("components/Heading", [], function (exports_1, context_1) {
    "use strict";
    var Heading, Headings;
    var __moduleName = context_1 && context_1.id;
    return {
        setters: [],
        execute: function () {
            Heading = /** @class */ (function () {
                function Heading(angle, flip) {
                    if (flip === void 0) { flip = 1; }
                    this.angle = angle;
                    this.flip = flip;
                }
                Object.defineProperty(Heading.prototype, "col_step", {
                    get: function () {
                        return -1 * (this.angle - 90) / 90 % 2;
                    },
                    enumerable: true,
                    configurable: true
                });
                Object.defineProperty(Heading.prototype, "row_step", {
                    get: function () {
                        return this.angle / 90 % 2;
                    },
                    enumerable: true,
                    configurable: true
                });
                Heading.from_angle = function (angle) {
                    while (angle > 180) {
                        angle -= 360;
                    }
                    while (angle < -90) {
                        angle += 360;
                    }
                    switch (angle) {
                        case 0: {
                            return Headings.RIGHT;
                        }
                        case 90: {
                            return Headings.DOWN;
                        }
                        case 180: {
                            return Headings.LEFT;
                        }
                        case -90: {
                            return Headings.UP;
                        }
                    }
                    throw new Error("Unknown heading angle " + angle);
                };
                Heading.prototype.turn_left = function () {
                    return Heading.from_angle(this.angle - 90);
                };
                Heading.prototype.turn_right = function () {
                    return Heading.from_angle(this.angle + 90);
                };
                return Heading;
            }());
            exports_1("Heading", Heading);
            exports_1("Headings", Headings = {
                RIGHT: new Heading(0),
                DOWN: new Heading(90),
                LEFT: new Heading(180, -1),
                UP: new Heading(-90)
            });
        }
    };
});
// A component to make handling grid addressing easier
System.register("components/Grid", [], function (exports_2, context_2) {
    "use strict";
    var Grid;
    var __moduleName = context_2 && context_2.id;
    return {
        setters: [],
        execute: function () {// A component to make handling grid addressing easier
            Grid = /** @class */ (function () {
                function Grid(cols, rows) {
                    this.cols = cols;
                    this.rows = rows;
                }
                Grid.prototype.facingAddress = function (from, heading, forward) {
                    if (forward === void 0) { forward = true; }
                    var direction_step = forward ? 1 : -1;
                    return [from[0] + heading.col_step * direction_step, from[1] + heading.row_step * direction_step];
                };
                Grid.prototype.sameAddress = function (one, two) {
                    return one[0] == two[0] && one[1] == two[1];
                };
                Grid.prototype.isOutOfBounds = function (address) {
                    return address[0] < 1 || address[0] > this.cols || address[1] < 1 || address[1] > this.rows;
                };
                Grid.prototype.addressInList = function (address, list) {
                    return list.some(function (item) { return address[0] == item[0] && address[1] == item[1]; });
                };
                Grid.prototype.hitsWall = function (from, to, walls) {
                    var _this = this;
                    return walls.some(function (wall) {
                        if (_this.sameAddress(from, wall[0]) && _this.sameAddress(to, wall[1])) {
                            return true;
                        }
                        if (_this.sameAddress(from, wall[1]) && _this.sameAddress(to, wall[0])) {
                            return true;
                        }
                        return false;
                    });
                };
                return Grid;
            }());
            exports_2("default", Grid);
        }
    };
});
System.register("components/consts", [], function (exports_3, context_3) {
    "use strict";
    var constants;
    var __moduleName = context_3 && context_3.id;
    return {
        setters: [],
        execute: function () {
            constants = {
                WEB_PREFIX: "",
            };
            if (process.env.NODE_ENV == "internal") {
                constants.WEB_PREFIX = "static/";
            }
            console.log("Running in " + process.env.NODE_ENV + ", setting web prefix to " + constants.WEB_PREFIX);
            exports_3("default", constants);
        }
    };
});
System.register("components/Board", ["phaser", "components/Grid", "components/consts"], function (exports_4, context_4) {
    "use strict";
    var phaser_1, Grid_1, consts_1, GRID_WIDTH, GRID_HEIGHT, BOARD_WIDTH, BOARD_HEIGHT, CELL_WIDTH, CELL_HEIGHT, obstacles, walls, BoardScene;
    var __moduleName = context_4 && context_4.id;
    return {
        setters: [
            function (phaser_1_1) {
                phaser_1 = phaser_1_1;
            },
            function (Grid_1_1) {
                Grid_1 = Grid_1_1;
            },
            function (consts_1_1) {
                consts_1 = consts_1_1;
            }
        ],
        execute: function () {
            GRID_WIDTH = 24;
            GRID_HEIGHT = 20;
            BOARD_WIDTH = 903;
            BOARD_HEIGHT = 752;
            CELL_WIDTH = BOARD_WIDTH / GRID_WIDTH;
            CELL_HEIGHT = BOARD_HEIGHT / GRID_HEIGHT;
            obstacles = [
                [5, 3],
                [5, 4],
                [5, 5],
                [6, 3],
                [6, 4],
                [6, 5],
                [7, 3],
                [7, 4],
                [7, 5],
                [8, 3],
                [8, 4],
                [8, 5],
                [9, 3],
                [9, 4],
                [9, 5],
            ];
            walls = [
                [
                    [15, 1],
                    [15, 2],
                ],
                [
                    [16, 1],
                    [16, 2],
                ],
                [
                    [14, 2],
                    [15, 2],
                ],
            ];
            BoardScene = /** @class */ (function (_super) {
                __extends(BoardScene, _super);
                function BoardScene(scene, x, y) {
                    var _this = _super.call(this, scene, x, y) || this;
                    _this.grid = new Grid_1.default(24, 20);
                    _this.setSize(BOARD_WIDTH, BOARD_HEIGHT);
                    scene.add.existing(_this);
                    _this.add(scene.add.image(0, 0, "board"));
                    return _this;
                }
                Object.defineProperty(BoardScene, "BOARD_WIDTH", {
                    get: function () {
                        return BOARD_WIDTH;
                    },
                    enumerable: true,
                    configurable: true
                });
                BoardScene.prototype.getPositionOnGrid = function (address) {
                    var x = -this.width / 2 + address[0] * CELL_WIDTH - CELL_WIDTH / 2;
                    var y = -this.height / 2 + address[1] * CELL_HEIGHT - CELL_HEIGHT / 2;
                    return new phaser_1.default.Math.Vector2(x, y);
                };
                BoardScene.preload = function (scene) {
                    scene.load.image("board", consts_1.default.WEB_PREFIX + "assets/board.png");
                };
                BoardScene.prototype.is_blocked = function (from, to) {
                    // check boundaries
                    if (this.grid.isOutOfBounds(to)) {
                        return true;
                    }
                    // check for static obstacles
                    if (this.grid.addressInList(to, obstacles)) {
                        return true;
                    }
                    // check for walls
                    if (this.grid.hitsWall(from, to, walls)) {
                        return true;
                    }
                };
                return BoardScene;
            }(phaser_1.default.GameObjects.Container));
            exports_4("default", BoardScene);
        }
    };
});
System.register("components/Character", ["phaser", "components/Heading"], function (exports_5, context_5) {
    "use strict";
    var phaser_2, Heading_1, IMAGE_SCALE, Character;
    var __moduleName = context_5 && context_5.id;
    return {
        setters: [
            function (phaser_2_1) {
                phaser_2 = phaser_2_1;
            },
            function (Heading_1_1) {
                Heading_1 = Heading_1_1;
            }
        ],
        execute: function () {
            IMAGE_SCALE = 0.08;
            Character = /** @class */ (function (_super) {
                __extends(Character, _super);
                function Character(scene, board, texture, socket) {
                    var _this = _super.call(this, scene, 0, 0, texture) || this;
                    _this.setScale(IMAGE_SCALE);
                    scene.add.existing(_this);
                    _this.board = board;
                    board.add(_this);
                    _this.address = [1, 1];
                    _this._heading = Heading_1.Headings.RIGHT;
                    _this.char_id = null;
                    _this.socket = socket;
                    socket.on('registration', function (data) {
                        _this.char_id = data['id'];
                    });
                    socket.on("message", function (data) {
                        _this.position(data["characters"][_this.char_id]["address"], true);
                        if (data["characters"][_this.char_id]["direction"] == "UP") {
                            _this.heading = Heading_1.Headings.UP;
                        }
                        if (data["characters"][_this.char_id]["direction"] == "DOWN") {
                            _this.heading = Heading_1.Headings.DOWN;
                        }
                        if (data["characters"][_this.char_id]["direction"] == "LEFT") {
                            _this.heading = Heading_1.Headings.LEFT;
                        }
                        if (data["characters"][_this.char_id]["direction"] == "RIGHT") {
                            _this.heading = Heading_1.Headings.RIGHT;
                        }
                    });
                    return _this;
                }
                Object.defineProperty(Character.prototype, "heading", {
                    /*
                  
                      // the angle is 0 for right, 90 for down, 180 for left, 270 for up
                      set heading(heading) {
                          if (heading < 0) {
                              heading += 360;
                          } else if (heading >= 360) {
                              heading -= 360;
                          }
                  
                          switch (heading) {
                              case HEADING.RIGHT: {
                                  this.angle = 0;
                                  this.scaleX = IMAGE_SCALE;
                                  break;
                              }
                              case HEADING.DOWN: {
                                  this.angle = 90;
                                  this.scaleX = IMAGE_SCALE;
                                  break;
                              }
                              case HEADING.LEFT: {
                                  this.angle = 0;
                                  this.scaleX = -IMAGE_SCALE;
                                  break;
                              }
                              case HEADING.UP: {
                                  this.angle = -90;
                                  this.scaleX = IMAGE_SCALE;
                              }
                          }
                  
                          this._heading = heading;
                      }
                      */
                    get: function () {
                        return this._heading;
                    },
                    set: function (heading) {
                        this._heading = heading;
                        this.angle = this._heading.angle;
                        this.scaleX = this._heading.flip * IMAGE_SCALE;
                        if (this._heading.flip == -1) {
                            this.angle -= 180;
                        }
                    },
                    enumerable: true,
                    configurable: true
                });
                Character.prototype.turn_left = function () {
                    this.heading = this.heading.turn_left();
                };
                Character.prototype.turn_right = function () {
                    this.heading = this.heading.turn_right();
                };
                Character.prototype.position = function (address, animate) {
                    if (animate === void 0) { animate = false; }
                    this.address = address;
                    var v = this.board.getPositionOnGrid(address);
                    if (animate) {
                        this.scene.tweens.add({
                            targets: this,
                            x: v.x,
                            y: v.y,
                            ease: phaser_2.default.Math.Easing.Quartic,
                            duration: 500,
                            yoyo: false,
                        });
                    }
                    else {
                        this.x = v.x;
                        this.y = v.y;
                    }
                };
                Character.prototype.move = function (forward) {
                    if (forward === void 0) { forward = true; }
                    var facing_cell = this.board.grid.facingAddress(this.address, this.heading, forward);
                    if (this.board.is_blocked(this.address, facing_cell)) {
                        return;
                    }
                    this.position(facing_cell, true);
                };
                return Character;
            }(phaser_2.default.GameObjects.Sprite));
            exports_5("default", Character);
        }
    };
});
System.register("components/Controls", ["phaser", "components/Board"], function (exports_6, context_6) {
    "use strict";
    var phaser_3, Board_1, Action, Controls;
    var __moduleName = context_6 && context_6.id;
    return {
        setters: [
            function (phaser_3_1) {
                phaser_3 = phaser_3_1;
            },
            function (Board_1_1) {
                Board_1 = Board_1_1;
            }
        ],
        execute: function () {
            (function (Action) {
                Action["FORWARD"] = "FORWARD";
                Action["BACKWARD"] = "BACKWARD";
                Action["LEFT"] = "TURN_LEFT";
                Action["RIGHT"] = "TURN_RIGHT";
            })(Action || (Action = {}));
            Controls = /** @class */ (function (_super) {
                __extends(Controls, _super);
                function Controls(scene, x, y, zombie, socket) {
                    var _this = _super.call(this, scene, x, y) || this;
                    _this.setSize(+scene.game.config.width - Board_1.default.BOARD_WIDTH, +scene.game.config.height);
                    scene.add.existing(_this);
                    _this.zombie = zombie;
                    _this.socket = socket;
                    var left_btn = _this.create_button(50, 50, 1, function () {
                        return _this.sendUpdate(Action.LEFT);
                    });
                    var right_btn = _this.create_button(120, 50, 4, function () {
                        return _this.sendUpdate(Action.RIGHT);
                    });
                    var fwd_btn = _this.create_button(50, 120, 2, function () {
                        return _this.sendUpdate(Action.FORWARD);
                    });
                    var bwd_btn = _this.create_button(120, 120, 3, function () {
                        return _this.sendUpdate(Action.BACKWARD);
                    });
                    return _this;
                }
                Controls.prototype.sendUpdate = function (action) {
                    this.socket.emit("update", { action: action });
                };
                Controls.prototype.create_button = function (x, y, frame, onPointerDown) {
                    var btn = this.scene.add
                        .sprite(x, y, "buttons", frame)
                        .setScale(0.3)
                        .setInteractive();
                    btn.on("pointerdown", onPointerDown);
                    this.add(btn);
                    return btn;
                };
                return Controls;
            }(phaser_3.default.GameObjects.Container));
            exports_6("default", Controls);
        }
    };
});
System.register("BoardScene", ["phaser", "components/Board", "components/Character", "components/Controls", "socket.io-client", "components/consts"], function (exports_7, context_7) {
    "use strict";
    var phaser_4, Board_2, Character_1, Controls_1, socket_io_client_1, consts_2, BoardScene;
    var __moduleName = context_7 && context_7.id;
    return {
        setters: [
            function (phaser_4_1) {
                phaser_4 = phaser_4_1;
            },
            function (Board_2_1) {
                Board_2 = Board_2_1;
            },
            function (Character_1_1) {
                Character_1 = Character_1_1;
            },
            function (Controls_1_1) {
                Controls_1 = Controls_1_1;
            },
            function (socket_io_client_1_1) {
                socket_io_client_1 = socket_io_client_1_1;
            },
            function (consts_2_1) {
                consts_2 = consts_2_1;
            }
        ],
        execute: function () {
            BoardScene = /** @class */ (function (_super) {
                __extends(BoardScene, _super);
                function BoardScene() {
                    return _super.call(this, "game-scene") || this;
                }
                BoardScene.prototype.preload = function () {
                    Board_2.default.preload(this);
                    this.load.image("zombie", consts_2.default.WEB_PREFIX + "assets/zombie.png");
                    this.load.spritesheet("buttons", consts_2.default.WEB_PREFIX + "assets/controls.png", {
                        frameWidth: 200,
                        frameHeight: 215,
                    });
                    var socket = socket_io_client_1.default("localhost:5000");
                    this.socket = socket;
                    socket.on("connect", function () {
                        socket.emit("join", { room: "Room 1" });
                    });
                };
                BoardScene.prototype.create = function () {
                    this.board = new Board_2.default(this, +this.game.config.width - Board_2.default.BOARD_WIDTH / 2, +this.game.config.height / 2);
                    var zombie = new Character_1.default(this, this.board, "zombie", this.socket);
                    zombie.position([3, 3]);
                    this.controls = new Controls_1.default(this, 0, 0, zombie, this.socket);
                };
                return BoardScene;
            }(phaser_4.default.Scene));
            exports_7("default", BoardScene);
        }
    };
});
System.register("main", ["phaser", "BoardScene"], function (exports_8, context_8) {
    "use strict";
    var phaser_5, BoardScene_1, config;
    var __moduleName = context_8 && context_8.id;
    return {
        setters: [
            function (phaser_5_1) {
                phaser_5 = phaser_5_1;
            },
            function (BoardScene_1_1) {
                BoardScene_1 = BoardScene_1_1;
            }
        ],
        execute: function () {
            config = {
                type: phaser_5.default.AUTO,
                width: 1400,
                height: 752,
                physics: {},
                scene: [BoardScene_1.default],
                scale: {
                    mode: phaser_5.default.Scale.FIT,
                    autoCenter: phaser_5.default.Scale.CENTER_BOTH,
                },
            };
            exports_8("default", new phaser_5.default.Game(config));
        }
    };
});
//# sourceMappingURL=main.js.map