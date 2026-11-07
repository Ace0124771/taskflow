import os

import redis

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")

redis_client = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

QUEUE_NAME = "taskflow:jobs"
DEAD_LETTER_NAME = "taskflow:dead"
MAX_ATTEMPTS = 3
JOB_TIMEOUT_SECONDS = 5


def enqueue_job(job_id: int):
    redis_client.rpush(QUEUE_NAME, job_id)


def move_to_dead_letter(job_id: int):
    redis_client.rpush(DEAD_LETTER_NAME, job_id)
