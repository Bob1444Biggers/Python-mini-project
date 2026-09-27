import pytest


@pytest.fixture
def sample_operations() -> list[dict]:
    """Фикстура, предоставляющая тестовый список операций для обработки."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-03-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-02-01T12:00:00"},
        {"id": 4, "state": "EXECUTED", "date": "2023-02-01T12:00:00"},  # Одинаковая дата для проверки стабильности сортировки классных делишек
    ]
