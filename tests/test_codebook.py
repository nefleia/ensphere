import json

import pytest

from src.ensphere import codebook
from src.ensphere.codebook import get_codebook


def setup_codebook_env(monkeypatch, tmp_path, data):
    codebook_file = tmp_path / "codebook.json"
    codebook_file.write_text(json.dumps(data))

    dummy_src = tmp_path / "src" / "ensphere"
    dummy_src.mkdir(parents=True)
    dummy_file = dummy_src / "dummy.py"
    dummy_file.write_text("# dummy")

    monkeypatch.setattr(codebook, "__file__", str(dummy_file))


def test_get_codebook(monkeypatch, tmp_path):
    setup_codebook_env(monkeypatch, tmp_path, {"a": 1, "b": 2})

    result = get_codebook()
    assert result == {"a": 1, "b": 2}


def test_invalid_codebook(monkeypatch, tmp_path):
    setup_codebook_env(monkeypatch, tmp_path, {"a": 1, "*": 2})

    with pytest.raises(
        ValueError, match="'*' key is not allowed in the codebook."
    ):
        get_codebook()
