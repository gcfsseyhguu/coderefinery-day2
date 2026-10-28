
import pytest

from typing_speed import words_per_minute, error_percentage, accuracy


@pytest.mark.parametrize("words, seconds, expected", [
    (20, 60, 20),
    (40, 60, 40),
    (10, 30, 26),
])
def test_words_per_minute(words, seconds, expected):
    assert words_per_minute(words, seconds) == pytest.approx(expected)


def test_error_percentage():
    assert error_percentage(2, 100) == pytest.approx(2)


def test_accuracy():
    assert accuracy(2, 100) == pytest.approx(98)


def test_invalid_time():
    with pytest.raises(ValueError):
        words_per_minute(20, 0)


def test_invalid_total():
    with pytest.raises(ValueError):
        error_percentage(2, 0)
