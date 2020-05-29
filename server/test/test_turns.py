import pytest

from game.turns import TurnManager


@pytest.fixture
def tm():
    return TurnManager(4, [])


@pytest.fixture
def char1(tm, game_factory):
    char = game_factory.create_character()
    tm.add_character(char)
    return char


@pytest.fixture
def char2(tm, game_factory):
    char = game_factory.create_character()
    tm.add_character(char)
    return char


def test_init(faker):
    chars = faker.pylist()
    tm = TurnManager(5, chars)
    assert tm.max_ap == 5
    assert tm.characters == chars
    assert tm.active_character_index == 0


def test_turns(tm, char1, char2):
    assert tm.current_character_id() == char1.char_id

    tm.end_turn()
    assert tm.current_character_id() == char2.char_id

    tm.end_turn()
    assert tm.current_character_id() == char1.char_id


def test_remaining_ap(tm, char1, char2):
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


def test_spend_many_ap(tm, char1, char2):
    assert tm.remaining_ap() == 4
    tm.spend_ap(3)
    assert tm.remaining_ap() == 1
