from unittest.mock import MagicMock, patch

import pandas as pd

from src.csv_xlsx_processing import read_transactions_from_csv, read_transactions_from_excel


@patch("pandas.read_csv")
def test_read_transactions_from_csv_success(mock_read_csv: MagicMock) -> None:
    mock_df = pd.DataFrame(
        [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv("dummy.csv")

    assert len(result) == 1
    assert result[0]["id"] == 650703
    assert result[0]["operationAmount"]["currency"]["code"] == "PEN"


@patch("pandas.read_csv")
def test_read_transactions_from_csv_error(mock_read_csv: MagicMock) -> None:
    mock_read_csv.side_effect = FileNotFoundError

    result = read_transactions_from_csv("invalid.csv")

    assert result == []


@patch("pandas.read_excel")
def test_read_transactions_from_excel_success(mock_read_excel: MagicMock) -> None:
    mock_df = pd.DataFrame(
        [
            {
                "id": 3598919,
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": "29740",
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            }
        ]
    )
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel("dummy.xlsx")

    assert len(result) == 1
    assert result[0]["id"] == 3598919
    assert result[0]["operationAmount"]["amount"] == "29740"


@patch("pandas.read_excel")
def test_read_transactions_from_excel_error(mock_read_excel: MagicMock) -> None:
    mock_read_excel.side_effect = Exception

    result = read_transactions_from_excel("invalid.xlsx")

    assert result == []
