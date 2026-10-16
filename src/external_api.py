import os
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_transaction_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях (тип float).

    Если транзакция в USD или EUR, отправляет запрос к APILayer Exchange Rates Data API.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount = float(operation_amount.get("amount", 0.0))
    currency = operation_amount.get("currency", {}).get("code", "RUB")

    if currency == "RUB":
        return amount

    if currency in ["USD", "EUR"]:
        api_key = os.getenv("EXCHANGE_RATES_API_KEY")
        if not api_key:
            return 0.0

        url = f"https://apilayer.com{currency}&amount={amount}"
        headers = {"apikey": api_key}

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return float(data.get("result", 0.0))
            return 0.0
        except requests.RequestException:
            return 0.0

    return 0.0
