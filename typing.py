
def words_per_minute(typed_text: str, seconds: float) -> float:
    if seconds <= 0:
        raise ValueError("Час має бути більшим за нуль.")

    words = len(typed_text.split())
    return words / seconds * 60


def error_percentage(original: str, typed: str) -> float:
    """Calculate the percentage of character errors."""
    if not original and not typed:
        return 0.0

    total_chars = max(len(original), len(typed))
    errors = sum(
        1
        for i in range(total_chars)
        if i >= len(original)
        or i >= len(typed)
        or original[i] != typed[i]
    )

    return errors / total_chars * 100


def accuracy(original: str, typed: str) -> float:
    """Calculate typing accuracy as a percentage."""
    return 100.0 - error_percentage(original, typed)


def typing_report(
    original: str, typed: str, seconds: float
) -> dict:
    """Return a complete typing performance report."""
    return {
        "words_per_minute": words_per_minute(typed, seconds),
        "error_percentage": error_percentage(original, typed),
        "accuracy": accuracy(original, typed),
    }
