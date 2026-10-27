import os
from typing import Any, cast

from src.csv_xlsx_processing import read_transactions_from_csv, read_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
import src.utils as utils
from src.widget import get_date, mask_account_card


def process_bank_search(data: list[dict[str, Any]], search: str) -> list[dict[str, Any]]:
    import re

    pattern = re.compile(search, re.IGNORECASE)
    result = []
    for transaction in data:
        description = transaction.get("description", "")
        if pattern.search(description):
            result.append(transaction)
    return result


def get_file_transactions() -> list[dict[str, Any]]:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    json_path = os.path.join("data", "operations.json")
    csv_path = os.path.join("data", "operations.csv")
    xlsx_path = os.path.join("data", "operations.xlsx")

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        return cast(list[dict[str, Any]], utils.read_json_file(json_path))
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        return cast(list[dict[str, Any]], read_transactions_from_csv(csv_path))
    elif choice == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        return cast(list[dict[str, Any]], read_transactions_from_excel(xlsx_path))
    else:
        print("Неверный выбор.")
        return []


def get_status_filter(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию")
        print(f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}")
        status_input = input("Пользователь: ").strip().upper()

        if status_input in valid_statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{status_input}"')
            return filter_by_state(data, status_input)
        else:
            print(f'Программа: Status операции "{status_input}" недоступен.\n')


def main() -> None:
    data = get_file_transactions()
    if not data:
        return

    data = get_status_filter(data)
    if not data:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    sort_date = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_date == "да":
        direction = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        reverse = True if "убыван" in direction else False
        data = sort_by_date(data, reverse=reverse)

    only_rub = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if only_rub == "да":
        data = [
            t
            for t in data
            if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
            or t.get("currency_code") == "RUB"
        ]

    filter_word = (
        input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ")
        .strip()
        .lower()
    )
    if filter_word == "да":
        word = input("Пользователь: ").strip()
        data = process_bank_search(data, word)

    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")

    if not data:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(data)}\n")

    for t in data:
        raw_date = t.get("date", "")
        # Вот здесь используются функции из widget.py
        date_formatted = get_date(raw_date) if raw_date else "Нет даты"

        desc = t.get("description", "Без описания")

        from_acc = t.get("from", "")
        to_acc = t.get("to", "")

        from_mask = mask_account_card(from_acc) if from_acc else ""
        to_mask = mask_account_card(to_acc) if to_acc else ""

        if from_mask and to_mask:
            transfer_line = f"{from_mask} -> {to_mask}"
        elif to_mask:
            transfer_line = to_mask
        else:
            transfer_line = "Перевод неизвестен"

        op_amount = cast(dict[str, Any], t.get("operationAmount", {}))
        if op_amount:
            amount = op_amount.get("amount", "0")
            curr_name = cast(dict[str, Any], op_amount.get("currency", {})).get("name", "")
        else:
            amount = t.get("amount", "0")
            curr_name = t.get("currency_name", "")

        print(f"{date_formatted} {desc}")
        print(transfer_line)
        print(f"Сумма: {amount} {curr_name}\n")


if __name__ == "__main__":
    main()
