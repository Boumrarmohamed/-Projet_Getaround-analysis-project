import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="GetAround Pricing API",
    description="API de prediction de prix pour GetAround",
    version="1.0"
)

class PredictionInput(BaseModel):
    input: List[List[float]]

@app.get("/")
def root():
    return {"message": "GetAround Pricing API"}

@app.post("/predict")
def predict(data: PredictionInput):
    try:
        # Mock prediction (random values for testing)
        predictions = [np.random.randint(50, 200) for _ in data.input]
        return {"prediction": predictions}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)