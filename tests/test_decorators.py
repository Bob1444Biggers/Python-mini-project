import os
from typing import Any

import pytest

from src.decorators import log


@log()
def add_numbers(x: int, y: int) -> int:
    return x + y


@log()
def divide_numbers(x: int, y: int) -> float:
    return x / y


@log(filename="test_log.txt")
def successful_file_func(x: int) -> int:
    return x * 2


@log(filename="test_log.txt")
def failing_file_func(x: int) -> float:
    return x / 0


def test_log_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    result = add_numbers(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert captured.out == "add_numbers ok\n"


def test_log_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(ZeroDivisionError):
        divide_numbers(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "divide_numbers error: ZeroDivisionError. Inputs: (1, 0), {}\n"


def test_log_file_success(tmp_path: Any) -> None:
    log_file = tmp_path / "test_log.txt"
    log_file_path = str(log_file)

    @log(filename=log_file_path)
    def dummy_func() -> str:
        return "success"

    assert dummy_func() == "success"

    with open(log_file_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "dummy_func ok\n"


def test_log_file_error(tmp_path: Any) -> None:
    log_file = tmp_path / "test_log.txt"
    log_file_path = str(log_file)

    @log(filename=log_file_path)
    def dummy_fail_func(a: int) -> float:
        return a / 0

    with pytest.raises(ZeroDivisionError):
        dummy_fail_func(5)

    with open(log_file_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "dummy_fail_func error: ZeroDivisionError. Inputs: (5,), {}\n"
