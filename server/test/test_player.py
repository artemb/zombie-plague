from test.my_base import MyBaseTestCase


class TestPlayer(MyBaseTestCase):

    def test_player_state(self):
        player = self.create_player()
        state = player.state()
        assert 'name' in state
        assert state['name'] == player.name