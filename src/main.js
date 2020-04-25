import Phaser from 'phaser'


import HelloWorldScene from './scenes/HelloWorldScene'
import BoardScene from './scenes/BoardScene'

const config = {
	type: Phaser.AUTO,
	width: 1400,
	height: 752,
	physics: {},
	scene: [BoardScene],
	scale: {
        mode: Phaser.Scale.FIT,
        autoCenter: Phaser.Scale.CENTER_BOTH
    },
}

export default new Phaser.Game(config)
