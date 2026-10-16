import json
import logging
from unittest.mock import mock_open, patch
import pytest
from src.utils import read_json_file


def test_read_json_file_success(caplog: pytest.LogCaptureFixture) -> None:
    mock_data = [{"id": 1, "state": "EXECUTED"}]
    with caplog.at_level(logging.DEBUG, logger="utils"):
        with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
            with patch("os.path.exists", return_value=True):
                assert read_json_file("dummy.json") == mock_data
                assert "Попытка чтения JSON-файла по пути" in caplog.text
                assert "Файл успешно прочитан" in caplog.text


def test_read_json_file_not_found(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.ERROR, logger="utils"):
        with patch("os.path.exists", return_value=False):
            assert read_json_file("missing.json") == []
            assert "Файл не найден по пути" in caplog.text


def test_read_json_file_invalid_json(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.ERROR, logger="utils"):
        with patch("builtins.open", mock_open(read_data="invalid json")):
            with patch("os.path.exists", return_value=True):
                assert read_json_file("corrupted.json") == []
                assert "Ошибка декодирования JSON в файле" in caplog.text
