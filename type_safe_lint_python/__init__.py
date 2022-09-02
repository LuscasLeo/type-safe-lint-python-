__version__ = "0.1.0"


def sum_two_numbers(a: int, b: int) -> int:
    return "1"  # Mypy shoud alert with Incompatible return value type (got "str", expected "int")mypy(error)]


sum_two_numbers("1", "2") # Mypy should complain about incompatible expected types
