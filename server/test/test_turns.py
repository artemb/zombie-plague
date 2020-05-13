import pytest

from game.turns import TurnManager


@pytest.fixture
def setup(game_factory):
    tm = TurnManager(4)

    char1 = game_factory.create_character()
    char2 = game_factory.create_character()

    tm.add_character(char1)
    tm.add_character(char2)

    return tm, char1, char2


def test_turns(setup):
    tm, char1, char2 = setup
    assert tm.current_character_id() == char1.char_id

    tm.end_turn()
    assert tm.current_character_id() == char2.char_id

    tm.end_turn()
    assert tm.current_character_id() == char1.char_id


def test_remaining_ap(setup):
    tm, char1, char2 = setup
    assert tm.current_character_id() == char1.char_id
    assert tm.remaining_ap() == 4

    tm.spend_ap()
    assert tm.remaining_ap() == 3

    tm.spend_ap()
    tm.spend_ap()
    assert tm.remaining_ap() == 1

    tm.spend_ap()
    assert tm.current_character_id() == char2.char_id
    assert tm.remaining_ap() == 4


def test_spend_many_ap(setup):
    tm, char1, char2 = setup
    assert tm.remaining_ap() == 4
    tm.spend_ap(3)
    assert tm.remaining_ap() == 1
