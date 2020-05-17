from unittest.mock import Mock

import pytest

from api import GameServerAPI


@pytest.fixture
def api():
    return GameServerAPI(Mock(), {}, Mock(), Mock())


def test_register(api):
    api.on_register({'username': 'Artem B'})

    api.mgr.register_player.assert_called_once()
    player_id = api.mgr.register_player.call_args[0][0]
    assert api.session['player_id'] == player_id
    api.emit.assert_called_once()
    assert api.emit.call_args[0][0] == 'joined'
    assert 'player_id' in api.emit.call_args[0][1]
    assert api.emit.call_args[0][1]['player_id'] == player_id


def test_on_check_registration_true(api, faker):
    player_id = faker.pystr()
    api.mgr.is_player_registered.return_value = True

    api.on_check_registration({'player_id': player_id})

    assert api.session['player_id'] == player_id
    api.emit.assert_called_once()
    assert api.emit.call_args[0][0] == 'registration_check'
    assert api.emit.call_args[0][1]['registered'] == True


def test_on_check_registration_false(api, faker):
    player_id = faker.pystr()
    api.mgr.is_player_registered.return_value = False

    api.on_check_registration({'player_id': player_id})

    assert 'player_id' not in api.session
    api.emit.assert_called_once()
    assert api.emit.call_args[0][0] == 'registration_check'
    assert api.emit.call_args[0][1]['registered'] == False


def test_on_update_no_action(api, faker):
    state = faker.pydict()
    api.mgr.state.return_value = state
    api.session['player_id'] = faker.pystr()

    api.on_update({'action': None})

    api.mgr.state.assert_called()
    api.send.assert_called_once_with(state)


def test_on_update_action(api, faker):
    state = faker.pydict()
    api.mgr.state.return_value = state
    api.session['player_id'] = faker.pystr()

    action = faker.pystr()
    character = faker.pystr()
    data = {'action': action, 'character': character, 'foo': 'bar'}
    api.on_update(data)

    api.mgr.action.assert_called_once_with(character, action, data)
    api.send.assert_called_once_with(state)
