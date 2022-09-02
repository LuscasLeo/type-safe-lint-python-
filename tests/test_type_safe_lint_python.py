from type_safe_lint_python import __version__
from type_safe_lint_python import sum_two_numbers


def test_version():
    assert __version__ == "0.1.0"


def test_sum():
    # Mypy does NOT act on runtime.
    # So you still can infer values with different
    # types into functions with typed arguments
    assert sum_two_numbers(1, "123") == "1"
