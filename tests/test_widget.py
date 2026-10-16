import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("Visa 7000792289606361", "Visa 7000 79** **** 6361"),
        ("Mastercard Gold 7000792289606361", "Mastercard Gold 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", ""),  # Пустая строка
        ("Visa", "Visa"),  # Некорректный формат (меньше двух элементов)
    ],
)
def test_mask_account_card(user_input: str, expected: str) -> None:
    """Тестирование маскировки разных типов карт и счетов."""
    assert mask_account_card(user_input) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59", "31.12.2023"),
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    """Тестирование преобразования формата даты."""
    assert get_date(date_str) == expected
