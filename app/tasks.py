import time


def task_add(payload):
    a = payload["a"]
    b = payload["b"]
    return a + b


def task_uppercase(payload):
    return str(payload["text"]).upper()


def task_sleep(payload):
    seconds = float(payload.get("seconds", 1))
    time.sleep(seconds)
    return f"slept {seconds} seconds"


TASK_HANDLERS = {
    "add": task_add,
    "uppercase": task_uppercase,
    "sleep": task_sleep,
}


def run_task(task_type, payload):
    handler = TASK_HANDLERS.get(task_type)
    if handler is None:
        raise ValueError(f"Unknown task type: {task_type}")
    return handler(payload)
