from pprint import pprint
from unittest.mock import patch

import app
from app import register, zombie_app, socketio


def test_register(faker, monkeypatch, mocker):
    emit = mocker.patch('app.emit')

    with zombie_app.test_request_context():
        assert len(app.session) == 0
        register({'username': faker.pystr()})
        assert len(app.session) > 0


    emit.assert_called_once()
