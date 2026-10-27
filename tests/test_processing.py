from src.processing import filter_by_state, process_bank_operations, sort_by_date


def test_filter_by_state() -> None:
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
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    expected = [
        {"id": 2, "state": "CANCELED"},
    ]
    assert filter_by_state(data, state="CANCELED") == expected


def test_filter_by_state_case_insensitive() -> None:
    data = [
        {"id": 1, "state": "Executed"},
        {"id": 2, "state": "canceled"},
    ]
    assert filter_by_state(data, state="executed") == [{"id": 1, "state": "Executed"}]
    assert filter_by_state(data, state="CANCELED") == [{"id": 2, "state": "canceled"}]


def test_filter_by_state_empty() -> None:
    assert filter_by_state([]) == []


def test_sort_by_date_descending() -> None:
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
    assert sort_by_date([]) == []


def test_process_bank_operations() -> None:
    data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод с карты на карту"},
        {"id": 3, "description": "Перевод организации"},
    ]
    categories = ["Перевод организации", "Открытие вклада"]
    expected = {"Перевод организации": 2, "Открытие вклада": 0}
    assert process_bank_operations(data, categories) == expected
