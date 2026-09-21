def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей операций по значению ключа но не юнайт (типо шутка) 'state'."""
    filtered_list = []

    for op in operations:
        if op.get("state") == state:
            filtered_list.append(op)

    return filtered_list


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей операций по дате от новых к старым (или наоборот)."""
    sorted_list = sorted(operations, key=lambda op: op.get("date", ""), reverse=reverse)

    return sorted_list
