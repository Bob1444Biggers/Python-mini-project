from collections import Counter


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей операций по значению ключа 'state'."""
    filtered_list = []

    for op in operations:
        op_state = str(op.get("state", "")).upper()
        if op_state == state.upper():
            filtered_list.append(op)

    return filtered_list


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей операций по дате от новых к старым (или наоборот)."""
    sorted_list = sorted(operations, key=lambda op: op.get("date", ""), reverse=reverse)

    return sorted_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Подсчитывает количество банковских операций определенных типов на основе поля description."""
    descriptions = [
        transaction.get("description", "")
        for transaction in data
        if transaction.get("description") in categories
    ]
    counts = Counter(descriptions)
    return {category: counts[category] for category in categories}
