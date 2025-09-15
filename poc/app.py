from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from prophet import Prophet
from datetime import datetime, timedelta
import random

app = FastAPI(title="Forecast Service")

class ForecastResponse(BaseModel):
    timestamp: str
    predicted_replicas: int

@app.get("/forecast", response_model=ForecastResponse)
def forecast():
    # --- dummy synthetic CPU data for demo ---
    now = datetime.utcnow()
    df = pd.DataFrame({
        "ds": [now - timedelta(hours=i) for i in range(48)],
        "y": [random.uniform(30, 70) for _ in range(48)],
    })
    m = Prophet(daily_seasonality=True)
    m.fit(df)
    future = m.make_future_dataframe(periods=1, freq="H")
    forecast = m.predict(future)
    next_hour = forecast.tail(1)["yhat"].values[0]
    replicas = max(2, int(round(next_hour / 20)))  # naive mapping CPU→replicas
    return ForecastResponse(
        timestamp=(now + timedelta(hours=1)).isoformat(),
        predicted_replicas=replicas
    )
