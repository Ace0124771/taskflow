import pytest

from app.tasks import run_task


def test_add():
    assert run_task("add", {"a": 2, "b": 3}) == 5


def test_uppercase():
    assert run_task("uppercase", {"text": "hello"}) == "HELLO"


def test_sleep_returns_message():
    result = run_task("sleep", {"seconds": 0})
    assert "slept" in result


def test_unknown_task_raises():
    with pytest.raises(ValueError):
        run_task("explode", {})
