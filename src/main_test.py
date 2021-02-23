import mock
from test import *
from main import *


def test_login():
    result: tuple[int, str, str, float] = (5, 'test', 'test', 100.0)
    with mock.patch("builtins.input", return_value="test"):
        assert login() == result


class TestUser:
    def test_on_create(self):
        user = User((0, 'czak', 'test', 100))
        assert user.userid == 0
        assert user.name == 'Czak'
        assert user.amount == 100
        assert isinstance(user, User)

    def test_deposit(self):
        user = User((0, 'czak', 'test', 100))
        with mock.patch("builtins.input", return_value=100.0):
            assert user.deposit_money() == 200.0

    def test_payout(self):
        user = User((0, 'czak', 'test', 100.0))
        with mock.patch("builtins.input", return_value=50.0):
            assert user.payout_money() == 50.0
