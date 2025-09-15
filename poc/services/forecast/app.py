from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel

app = FastAPI()

class ForecastRequest(BaseModel):
    series: list[float]

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/forecast")
def forecast(req: ForecastRequest):
    data = np.array(req.series)
    mean = data.mean() if len(data) > 0 else 0
    forecasted = list(mean + np.random.randn(10))  # dummy forecast
    return {"forecast": forecasted}
