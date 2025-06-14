from unittest.mock import patch

import pytest

from src.sphere.encrypt import encrypt


@pytest.fixture
def dummy_mapping():
    # a, b, c, space のみ対応
    return {"a": 1, "b": 2, "c": 3, " ": 0}


@patch("src.sphere.encrypt.load_mapping")
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
def test_encrypt_basic(mock_load_mapping, dummy_mapping, input_text, expected_output):
    mock_load_mapping.return_value = dummy_mapping
    assert encrypt(input_text) == expected_output


@patch("src.sphere.encrypt.load_mapping")
def test_encrypt_mixed_characters(mock_load_mapping, dummy_mapping):
    mock_load_mapping.return_value = dummy_mapping
    assert encrypt("aXbYcZ") == "1 * 2 * 3 *"


@patch("src.sphere.encrypt.load_mapping")
def test_encrypt_empty_string(mock_load_mapping, dummy_mapping):
    mock_load_mapping.return_value = dummy_mapping
    assert encrypt("") == ""
