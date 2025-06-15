import pytest

from src.sphere.decrypt import decrypt


@pytest.fixture
def dummy_mapping():
    return {"a": 1, "b": 2, "c": 3, " ": 0}


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("1 2 3", "abc"),
        ("1 0 2 0 3", "a b c"),
        ("*", "*"),
        ("1 * 2", "a*b"),
        ("", ""),
    ],
)
def test_decrypt_basic(dummy_mapping, input_text, expected_output):
    assert decrypt(dummy_mapping, input_text) == expected_output
