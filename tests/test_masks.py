from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Тест корректной маскировки номера карты."""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_empty() -> None:
    """Тест маскировки карты с пустой строкой."""
    assert get_mask_card_number("") == " ** **** "


def test_get_mask_account() -> None:
    """Тест корректной маскировки номера счета."""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_empty() -> None:
    """Тест маскировки счета с пустой строкой."""
    assert get_mask_account("") == "**"
