import pytest

from src.sphere.encrypt import encrypt


@pytest.fixture
def dummy_codebook():
    return {"a": 1, "b": 2, "c": 3, " ": 0}


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("abc", "1 2 3"),
        ("a b c", "1 0 2 0 3"),
        ("ABC", "1 2 3"),
        ("x", "*"),
        ("aXbYcZ", "1 * 2 * 3 *"),
        ("", ""),
    ],
)
def test_encrypt_basic(dummy_codebook, input_text, expected_output):
    assert encrypt(dummy_codebook, input_text) == expected_output


def test_encrypt_mixed_characters(dummy_codebook):
    assert encrypt(dummy_codebook, "aXbYcZ") == "1 * 2 * 3 *"


def test_encrypt_empty_string(dummy_codebook):
    assert encrypt(dummy_codebook, "") == ""
