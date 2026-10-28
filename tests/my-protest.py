
import pytest

from typing_spee import (
    words_per_minute,
    error_percentage,
    accuracy,
    typing_report,
)


@pytest.mark.parametrize(
    "text, seconds, expected",
    [
        ("hello world", 60, 2.0),
        ("one two three", 30, 6.0),
        ("", 60, 0.0),
        ("hello", 15, 4.0),
    ],
)
def test_words_per_minute(text, seconds, expected):
    assert words_per_minute(text, seconds) == pytest.approx(expected)


@pytest.mark.parametrize(
    "original, typed, expected",
    [
        ("hello", "hello", 0.0),
        ("hello", "hallo", 20.0),
        ("abc", "ab", 33.3333333333),
        ("", "", 0.0),
    ],
)
def test_error_percentage(original, typed, expected):
    assert error_percentage(original, typed) == pytest.approx(expected)


@pytest.mark.parametrize(
    "original, typed, expected",
    [
        ("hello", "hello", 100.0),
        ("hello", "hallo", 80.0),
        ("", "", 100.0),
    ],
)
def test_accuracy(original, typed, expected):
    assert accuracy(original, typed) == pytest.approx(expected)


def test_typing_report():
    report = typing_report("hello world", "hello word", 30)

    assert report["words_per_minute"] == pytest.approx(4.0)
    assert report["error_percentage"] == pytest.approx(9.09090909)
    assert report["accuracy"] == pytest.approx(90.90909091)


@pytest.mark.parametrize("seconds", [0, -1, -10])
def test_invalid_time(seconds):
    with pytest.raises(ValueError):
        words_per_minute("hello world", seconds)
