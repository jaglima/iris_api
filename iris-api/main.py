from fastapi import FastAPI
from pydantic import BaseModel
from src import irisModel
from typing import List

app = FastAPI()


class PredictionResponse(BaseModel):
    predicted_species: List[int]


class IrisPayload(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict")
async def predict_species(payload: IrisPayload):
    data = [
        [
            payload.sepal_length,
            payload.sepal_width,
            payload.petal_length,
            payload.petal_width,
        ]
    ]

    prediction = irisModel(data)
    return PredictionResponse(predicted_species=prediction)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
