from fastapi import FastAPI, BackgroundTasks
import requests
import os

app = FastAPI()

FORECAST_URL = os.getenv("FORECAST_URL", "http://forecast:8000/forecast")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: dict, background_tasks: BackgroundTasks):
    # simulate enqueue job to worker
    background_tasks.add_task(call_forecast, data)
    return {"message": "Job queued"}

def call_forecast(data):
    try:
        r = requests.post(FORECAST_URL, json=data, timeout=10)
        print("Forecast result:", r.json())
    except Exception as e:
        print("Forecast error:", e)
