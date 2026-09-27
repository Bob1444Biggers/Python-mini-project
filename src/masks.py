def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты.

    Формат: XXXX XX** **** XXXX крутых цифирок
    """
    # Выделяем нужные части номера с помощью срезов
    first_block = card_number[:4]
    second_block_visible = card_number[4:6]
    last_block = card_number[-4:]

    # Собираем строку в правильном формате
    return f"{first_block} {second_block_visible}** **** {last_block}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета.

    Формат: **XXXX (только последние 4 цифры важны как никак)
    """
    # Берем последние 4 цифры
    last_four_digits = account_number[-4:]

    # Возвращаем маску
    return f"**{last_four_digits}"


if __name__ == "__main__":
    # Тест функции маскирования карты чтобы проверить работоспособность
    card_result = get_mask_card_number("7000792289606361")
    print(card_result)  # Ожидается: 7000 79** **** 6361

    # Тест функции маскирования счета чтобы не спалили
    account_result = get_mask_account("73654108430135874305")
    print(account_result)  # Ожидается: **4305
