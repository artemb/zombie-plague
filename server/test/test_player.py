def test_player_state(game_factory):
    player = game_factory.create_player()
    state = player.state()
    assert 'name' in state
    assert state['name'] == player.name