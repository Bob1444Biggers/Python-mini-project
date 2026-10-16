import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join("logs", "masks.log"), mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    logger.debug(f"Запрос на маскирование карты. Вход: {card_number}")
    first_block = card_number[:4]
    second_block_visible = card_number[4:6]
    last_block = card_number[-4:]
    result = f"{first_block} {second_block_visible}** **** {last_block}"
    logger.debug(f"Карта успешно замаскирована: {result}")
    return result


def get_mask_account(account_number: str) -> str:
    logger.debug(f"Запрос на маскирование счета. Вход: {account_number}")
    last_four_digits = account_number[-4:]
    result = f"**{last_four_digits}"
    logger.debug(f"Счет успешно замаскирован: {result}")
    return result


if __name__ == "__main__":
    card_result = get_mask_card_number("7000792289606361")
    print(card_result)

    account_result = get_mask_account("73654108430135874305")
    print(account_result)

