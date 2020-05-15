from game.grid_def import OBSTACLES, WALLS, rect_obstacle, hwall, vwall


def test_def(game_factory):
    grid = game_factory.create_grid(24, 20, obstacles=OBSTACLES, walls=WALLS)
    assert not grid.can_step((4, 3), (5, 3))

def test_rect_obstacle():
    obst = rect_obstacle((2, 2), 3, 2)

    assert len(obst) == 3 * 2
    assert (2, 2) in obst
    assert (3, 3) in obst
    assert (4, 4) not in obst

def test_hwall():
    wall = hwall((2, 2), 3)
    assert ((2, 1), (2, 2)) in wall
    assert ((4, 1), (4, 2)) in wall
    assert ((5, 1), (5, 2)) not in wall
    assert ((2, 2), (3, 2)) not in wall

def test_hwall():
    wall = vwall((2, 2), 3)
    assert ((1, 2), (2, 2)) in wall
    assert ((1, 4), (2, 4)) in wall
    assert ((1, 5), (2, 5)) not in wall
    assert ((2, 2), (2, 3)) not in wall
