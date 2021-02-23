import mock
from main import *


def test_login():
    result: tuple[int, str, str, float] = (5, 'test', 'test', 0.0)
    with mock.patch("builtins.input", return_value="test"):
        assert login() == result


class TestUser:
    def test_on_create(self):
        user = User((0, 'czak', 'test', 100))
        assert user.userid == 0
        assert user.name == 'czak'
        assert user.amount == 100
        assert isinstance(user, User)