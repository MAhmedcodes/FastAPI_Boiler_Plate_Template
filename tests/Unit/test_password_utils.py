from shared.utils import utils


class TestPasswordHashing:

    def test_hash_password(self):
        hashed = utils.hashing("secure123")
        assert isinstance(hashed, str)
        assert hashed != "secure123"

    def test_verify_correct(self):
        hashed = utils.hashing("secure123")
        assert utils.verify("secure123", hashed) is True

    def test_verify_wrong(self):
        hashed = utils.hashing("secure123")
        assert utils.verify("wrong", hashed) is False

    def test_long_password(self):
        pw = "a" * 200
        hashed = utils.hashing(pw)
        assert utils.verify(pw, hashed) is True
