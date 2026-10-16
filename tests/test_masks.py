import logging
import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("", " ** **** "),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str, caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.DEBUG, logger="masks"):
        assert get_mask_card_number(card_number) == expected
        assert "Запрос на маскирование карты" in caplog.text


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("1234567890", "**7890"),
        ("", "**"),
    ],
)
def test_get_mask_account(account_number: str, expected: str, caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.DEBUG, logger="masks"):
        assert get_mask_account(account_number) == expected
        assert "Запрос на маскирование счета" in caplog.text
