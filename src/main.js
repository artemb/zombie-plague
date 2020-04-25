import Phaser from 'phaser'

import HelloWorldScene from './scenes/HelloWorldScene'
import BoardScene from './scenes/BoardScene'

const config = {
	type: Phaser.AUTO,
	width: 800,
	height: 600,
	physics: {
		default: 'arcade',
		arcade: {
			gravity: { y: 300 }
		}
	},
	scene: [BoardScene]
}

export default new Phaser.Game(config)
