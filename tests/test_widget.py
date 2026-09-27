from src.widget import get_date, mask_account_card


def test_mask_account_card_visa() -> None:
    """Тест маскировки карты с названием из одного слова."""
    assert mask_account_card("Visa 7000792289606361") == "Visa 7000 79** **** 6361"


def test_mask_account_card_maestro() -> None:
    """Тест маскировки карты с названием из нескольких слов."""
    assert mask_account_card("Mastercard Gold 7000792289606361") == "Mastercard Gold 7000 79** **** 6361"


def test_mask_account_card_account() -> None:
    """Тест маскировки счета."""
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


def test_mask_account_card_empty() -> None:
    """Тест обработки пустой строки."""
    assert mask_account_card("") == ""


def test_mask_account_card_short() -> None:
    """Тест обработки строки, где меньше двух элементов."""
    assert mask_account_card("Visa") == "Visa"


def test_get_date_correct() -> None:
    """Тест корректного преобразования формата даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
