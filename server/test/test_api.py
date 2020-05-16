from unittest.mock import MagicMock, Mock

import pytest

from api import GameServerAPI
from game.game_manager import GameManager


@pytest.fixture
def mock_emit():
    def emit(event_name, data):
        print(f"Got data on {event_name}: {data}")

    return emit


def test_register(mock_emit):
    mgr = Mock()
    session = {}
    api = GameServerAPI(mgr, session, mock_emit)

    api.register({'username': 'Artem B'})

    mgr.register_player.assert_called_once()
    player_id = mgr.register_player.call_args[0][0]
    assert session['player_id'] == player_id
