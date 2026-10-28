
def words_per_minute(words, seconds):
    if seconds <= 0:
        raise ValueError("Час має бути більшим за нуль")
    return words / seconds * 60


def error_percentage(errors, total):
    if total <= 0:
        raise ValueError("Кількість символів має бути більшою за нуль")
    return errors / total * 100


def accuracy(errors, total):
    if errors ==0:
        return 99
    return 100 - error_percentage(errors, total)
