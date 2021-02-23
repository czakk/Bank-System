import mock
from main import *


def test_login():
    result = (5, 'test', 'test', 0.0)
    with mock.patch("builtins.input", return_value="test"):
        assert login() == result


