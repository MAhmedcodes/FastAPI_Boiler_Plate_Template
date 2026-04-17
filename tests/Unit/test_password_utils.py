import pytest
from shared.utils import utils


class TestPasswordHashing:

    def test_hash_password_returns_string(self):
        password = "secure123"
        hashed = utils.hashing(password)
        assert isinstance(hashed, str)
        assert hashed != password

    def test_verify_correct_password(self):
        password = "secure123"
        hashed = utils.hashing(password)
        assert utils.verify(password, hashed) is True

    def test_verify_wrong_password(self):
        password = "secure123"
        wrong = "wrongpass"
        hashed = utils.hashing(password)
        assert utils.verify(wrong, hashed) is False

    def test_long_password_handling(self):
        long_password = "a" * 100
        hashed = utils.hashing(long_password)
        assert utils.verify(long_password, hashed) is True
