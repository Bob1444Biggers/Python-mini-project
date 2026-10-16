import json
from unittest.mock import mock_open, patch
from src.utils import read_json_file


def test_read_json_file_success() -> None:
    mock_data = [{"id": 1, "state": "EXECUTED"}]
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        with patch("os.path.exists", return_value=True):
            assert read_json_file("dummy.json") == mock_data


def test_read_json_file_not_found() -> None:
    with patch("os.path.exists", return_value=False):
        assert read_json_file("missing.json") == []


def test_read_json_file_invalid_json() -> None:
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("os.path.exists", return_value=True):
            assert read_json_file("corrupted.json") == []
