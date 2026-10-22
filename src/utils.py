import json
import logging
import os
from typing import Any, Dict, List

# Создаем папку logs в корне проекта, если ее еще нет
os.makedirs("logs", exist_ok=True)

# Инициализируем логер для этого модуля
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Настраиваем запись в файл utils.log с перезаписью (mode="w") при каждом запуске
file_handler = logging.FileHandler(os.path.join("logs", "utils.log"), mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Задаем формат логов: дата - имя модуля - уровень серьезности - сообщение
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей с транзакциями."""
    logger.debug(f"Попытка чтения JSON-файла по пути: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден по пути: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.debug(f"Файл успешно прочитан. Найдено элементов: {len(data)}")
                return data
            logger.error(f"Некорректный формат данных в {file_path}: ожидался список (list)")
            return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {str(e)}")
        return []
