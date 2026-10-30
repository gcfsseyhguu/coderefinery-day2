def add(left, right):
    """Return the sum of the left and right values.

    Args:
        left: The first value to add.
        right: The second value to add.

    Returns:
        The sum of left and right.

    Example:
        add(3, 4) -> 7
    """
    return left + right


def subtract(left, right):
    """Subtract the second value from the first.

    Args:
        left: The value to subtract from.
        right: The value to subtract.

    Returns:
        The difference between left and right.
    """
    return left - right


def test_add():
    assert add(3, 4) == 7



def test_subtract():
    assert subtract(3, 4) == -1


def test_subtract_positive_result():
    assert subtract(4, 3) == 1
