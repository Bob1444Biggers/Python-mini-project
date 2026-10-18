from typing import Any
from unittest.mock import patch

import pytest

from src.external_api import convert_transaction_amount


@pytest.fixture
def rub_transaction() -> dict:
    return {"operationAmount": {"amount": "150.00", "currency": {"code": "RUB"}}}


@pytest.fixture
def usd_transaction() -> dict:
    return {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}


def test_convert_rub(rub_transaction: dict) -> None:
    assert convert_transaction_amount(rub_transaction) == 150.00


@patch("src.external_api.requests.get")
@patch("src.external_api.os.getenv")
def test_convert_usd_success(mock_getenv: Any, mock_get: Any, usd_transaction: dict) -> None:
    mock_getenv.return_value = "mocked_api_key"
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 8500.00}

    assert convert_transaction_amount(usd_transaction) == 8500.00
    assert mock_get.called
