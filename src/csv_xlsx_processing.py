import pandas as pd


def read_transactions_from_csv(file_path: str) -> list[dict]:
    """Считывает финансовые операции из CSV файла и возвращает список словарей."""
    try:
        df = pd.read_csv(file_path, sep=";")
        df = df.dropna(how="all")
        df = df.fillna("")

        transactions = []
        for _, row in df.iterrows():
            transaction = {
                "id": int(row["id"]) if row["id"] != "" else "",
                "state": str(row["state"]),
                "date": str(row["date"]),
                "operationAmount": {
                    "amount": str(row["amount"]),
                    "currency": {"name": str(row["currency_name"]), "code": str(row["currency_code"])},
                },
                "from": str(row["from"]),
                "to": str(row["to"]),
                "description": str(row["description"]),
            }
            transactions.append(transaction)

        return transactions
    except (FileNotFoundError, Exception):
        return []


def read_transactions_from_excel(file_path: str) -> list[dict]:
    """Считывает финансовые операции из Excel файла и возвращает список словарей."""
    try:
        df = pd.read_excel(file_path)
        df = df.dropna(how="all")
        df = df.fillna("")

        transactions = []
        for _, row in df.iterrows():
            transaction = {
                "id": int(row["id"]) if row["id"] != "" else "",
                "state": str(row["state"]),
                "date": str(row["date"]),
                "operationAmount": {
                    "amount": str(row["amount"]),
                    "currency": {"name": str(row["currency_name"]), "code": str(row["currency_code"])},
                },
                "from": str(row["from"]),
                "to": str(row["to"]),
                "description": str(row["description"]),
            }
            transactions.append(transaction)

        return transactions
    except (FileNotFoundError, Exception):
        return []
