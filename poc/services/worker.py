from celery import Celery
import os

BROKER = os.getenv("REDIS_URL", "redis://redis:6379/0")
app = Celery("worker", broker=BROKER)

@app.task
def heavy_job(payload):
    print("Processing:", payload)
    return {"result": sum(payload)}
