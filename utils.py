def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    """Multiply two numbers together."""
    if not a or not b:
        raise ValueError("multiply_numbers does not accept empty input")
    return a * b
