import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

QUEUE_NAME = "taskflow:jobs"


def enqueue_job(job_id: int):
    redis_client.rpush(QUEUE_NAME, job_id)
