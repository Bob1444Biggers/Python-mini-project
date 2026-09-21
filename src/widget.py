from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Великолепно Маскирует номер карты или счета с сохранением типа."""
    if not user_input or not user_input.strip():
        return ""

    parts = user_input.split()

    if len(parts) < 2:
        return user_input

    number = parts[-1]
    type_name = " ".join(parts[:-1])

    if type_name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{type_name} {masked_number}"


def get_date(date_str: str) -> str:
    """Преобразует строку даты ISO в формат ДД.ММ.ГГГГ."""
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
