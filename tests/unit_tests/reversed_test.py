from crackme_zed_frequency.main import generate_key
from crackme_zed_frequency.main import make_key_look_legit
from crackme_zed_frequency.reversed import zed_frequency


def test_wrong_key() -> None:
    assert not zed_frequency("abcdefghjkabcdefghjkabcdef")


def test_valid_key() -> None:
    valid_key: str = generate_key()
    assert zed_frequency(valid_key)


def test_shuffle() -> None:
    valid_key: str = generate_key()
    scrambled_key = make_key_look_legit(valid_key)
    assert zed_frequency(scrambled_key)
