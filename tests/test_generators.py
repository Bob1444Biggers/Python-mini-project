import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# --- Тестирование функции (важно учитывать тестирование) filter_by_currency ---

def test_filter_by_currency_empty():
    """Проверяет, что генератор корректно обрабатывает пустой список и не падает."""
    assert list(filter_by_currency([], "USD")) == []


def test_filter_by_currency_no_match(sample_operations):
    """Проверяет случай, когда транзакции в заданной валюте полностью отсутствуют."""
    assert list(filter_by_currency(sample_operations, "USD")) == []


def test_filter_by_currency_valid():
    """Проверяет корректную фильтрацию по валюте на кастомных данных."""
    custom_data = [
        {"id": 10, "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 20, "operationAmount": {"currency": {"code": "RUB"}}},
        {"id": 30, "operationAmount": {"currency": {"code": "USD"}}},
    ]
    usd_tx = list(filter_by_currency(custom_data, "USD"))
    assert len(usd_tx) == 2
    assert usd_tx[0]["id"] == 10
    assert usd_tx[1]["id"] == 30


# --- Тестирование функции transaction_descriptions ---

def test_transaction_descriptions_valid(sample_operations):
    """Проверяет, что функция возвращает пустые строки, если ключа 'description' нет."""
    descriptions = list(transaction_descriptions(sample_operations))
    assert descriptions == ["", "", "", ""]


def test_transaction_descriptions_with_data():
    """Тестирует работу функции с заполненными описаниями."""
    custom_data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"}
    ]
    descriptions = list(transaction_descriptions(custom_data))
    assert descriptions == ["Перевод организации", "Перевод со счета на счет"]


# --- Тестирование генератора card_number_generator ---

@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
    ]
)
def test_card_number_generator_ranges(start, stop, expected):
    """Проверяет корректность генерации и форматирования номеров карт в диапазоне."""
    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_boundary():
    """Убеждается, что генератор корректно обрабатывает крайние значения (start == stop)."""
    gen = card_number_generator(7, 7)
    assert next(gen) == "0000 0000 0000 0007"
    with pytest.raises(StopIteration):
        next(gen)
