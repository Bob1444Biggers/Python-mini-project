from src.processing import filter_by_state, sort_by_date


def test_filter_by_state() -> None:
    """Тест фильтрации списка операций по умолчанию (EXECUTED)."""
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    expected = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    assert filter_by_state(data) == expected


def test_filter_by_state_canceled() -> None:
    """Тест фильтрации списка по конкретному статусу CANCELED."""
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    expected = [
        {"id": 2, "state": "CANCELED"},
    ]
    assert filter_by_state(data, state="CANCELED") == expected


def test_filter_by_state_empty() -> None:
    """Тест фильтрации пустого списка."""
    assert filter_by_state([]) == []


def test_sort_by_date_descending() -> None:
    """Тест сортировки по дате от новых к старым (по умолчанию)."""
    data = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "2023-03-01"},
        {"id": 3, "date": "2023-02-01"},
    ]
    expected = [
        {"id": 2, "date": "2023-03-01"},
        {"id": 3, "date": "2023-02-01"},
        {"id": 1, "date": "2023-01-01"},
    ]
    assert sort_by_date(data) == expected


def test_sort_by_date_ascending() -> None:
    """Тест сортировки по дате от старых к новым (reverse=False)."""
    data = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "2023-03-01"},
    ]
    expected = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "2023-03-01"},
    ]
    assert sort_by_date(data, reverse=False) == expected


def test_sort_by_date_empty() -> None:
    """Тест сортировки пустого списка по дате."""
    assert sort_by_date([]) == []
