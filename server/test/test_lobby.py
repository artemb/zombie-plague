from unittest.mock import Mock

import pytest

from game.game import Lobby, OutOfCharactersError, UnknownPlayerError, UnknownCharacterError, Game


@pytest.fixture
def lobby():
    return Lobby()


def test_lobby_no_players(lobby):
    assert len(lobby.players) == 0
    assert len(lobby.characters) == 0


def test_lobby_create_characters(lobby, game_faker):
    player = game_faker.player()
    lobby.register_player(player)
    assert len(lobby.players) == 1
    assert lobby.players[player.id] == player


def test_lobby_create_character(lobby):
    expected_faces = ['char1', 'char2', 'char3', 'char4']
    for exp in expected_faces:
        char = lobby.create_character()
        assert char is not None
        assert char.face == exp

    with pytest.raises(OutOfCharactersError):
        lobby.create_character()


def test_assign_character(lobby, game_faker):
    player = game_faker.player()
    char = lobby.create_character()

    lobby.register_player(player)
    lobby.assign_character(player, char)

    assert char.player_id == player.id
    player_chars = lobby.get_player_characters(player)
    assert len(player_chars) == 1
    assert char in player_chars


def test_get_player_characters(lobby, game_faker):
    player1 = game_faker.player()
    player2 = game_faker.player()
    char1 = lobby.create_character()
    char2 = lobby.create_character()

    lobby.register_player(player1)
    lobby.register_player(player2)

    lobby.assign_character(player1, char1)
    lobby.assign_character(player2, char2)

    player1_chars = lobby.get_player_characters(player1)
    assert len(player1_chars) == 1
    assert char1 in player1_chars
    assert char2 not in player1_chars

    player2_chars = lobby.get_player_characters(player2)
    assert len(player2_chars) == 1
    assert char2 in player2_chars
    assert char1 not in player2_chars


def test_get_player(lobby, game_faker):
    player = game_faker.player()

    with pytest.raises(UnknownPlayerError):
        lobby.get_player(player.id)

    lobby.register_player(player)
    assert lobby.get_player(player.id) == player


def test_get_character(lobby, faker):
    with pytest.raises(UnknownCharacterError):
        lobby.get_character(faker.pystr())

    char = lobby.create_character()
    assert lobby.get_character(char.char_id) == char


def test_start_game(lobby, game_faker, mocker):
    lobby.players = Mock()
    lobby.characters = Mock()
    grid = Mock()

    mock = mocker.patch.object(Game, '__init__', return_value=None)

    game = lobby.start_game(grid)

    assert game is not None
    mock.assert_called_once_with(grid, lobby.players, lobby.characters)
