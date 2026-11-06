import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

QUEUE_NAME = "taskflow:jobs"
DEAD_LETTER_NAME = "taskflow:dead"
MAX_ATTEMPTS = 3


def enqueue_job(job_id: int):
    redis_client.rpush(QUEUE_NAME, job_id)


def move_to_dead_letter(job_id: int):
    redis_client.rpush(DEAD_LETTER_NAME, job_id)
