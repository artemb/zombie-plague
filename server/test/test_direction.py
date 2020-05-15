from game.action import Turn, Direction


def test_turns():
    d = Direction.RIGHT

    d = d.turn(Turn.LEFT)
    assert d == Direction.UP

    d = d.turn(Turn.LEFT)
    assert d == Direction.LEFT

    d = d.turn(Turn.LEFT)
    assert d == Direction.DOWN

    d = d.turn(Turn.LEFT)
    assert d == Direction.RIGHT

    d = d.turn(Turn.RIGHT)
    assert d == Direction.DOWN

    d = d.turn(Turn.RIGHT)
    assert d == Direction.LEFT

    d = d.turn(Turn.RIGHT)
    assert d == Direction.UP

    d = d.turn(Turn.RIGHT)
    assert d == Direction.RIGHT

