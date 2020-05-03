import unittest
from game.grid import Grid
from game.enums import Direction, Turn, Step
from game.character import Character
from game.grid_def import OBSTACLES, WALLS, rect_obstacle, hwall, vwall


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

    def test_hwall(self):
        wall = hwall((2, 2), 3)
        self.assertIn(((2, 1), (2, 2)), wall)
        self.assertIn(((4, 1), (4, 2)), wall)
        self.assertNotIn(((5, 1), (5, 2)), wall)
        self.assertNotIn(((2, 2), (3, 2)), wall)
    
    def test_hwall(self):
        wall = vwall((2, 2), 3)
        self.assertIn(((1, 2), (2, 2)), wall)
        self.assertIn(((1, 4), (2, 4)), wall)
        self.assertNotIn(((1, 5), (2, 5)), wall)
        self.assertNotIn(((2, 2), (2, 3)), wall)
