import unittest
from game.grid import Grid
from game.enums import Direction, Turn, Step
from game.character import Character
from game.grid_def import OBSTACLES, WALLS, rect_obstacle


class TestGridDef(unittest.TestCase):

    def test_def(self):
        grid = Grid(24, 20, obstacles=OBSTACLES, walls=WALLS)
        self.assertFalse(grid.can_step((4, 3), (5, 3)))

    def test_rect_obstacle(self):
        obst = rect_obstacle((2, 2), 3, 2)
        self.assertEqual(len(obst), 3*2)
        self.assertIn((2, 2), obst)
        self.assertIn((3, 3), obst)
        self.assertNotIn((4, 4), obst)