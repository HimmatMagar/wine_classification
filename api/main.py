import joblib
import pandas as pd
from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse


with open('model/estimater.pkl', 'rb') as f:
    model = joblib.load(f)


app = FastAPI()

@app.get('/')
def home():
    return {'message': {'Wine Type Classification'}}

class UserInput(BaseModel):
    wine_type: Annotated[float, Field(..., description="Wine type: 1 for white and 0 for red")]
    alcohol: Annotated[float, Field(..., description="Add the alcohol level")]
    density: Annotated[float, Field(..., description="Enter the density of wine")]
    volatile_acidity: Annotated[float, Field(..., description="Enter the volatile acidity")]
    pH: Annotated[float, Field(..., description="Enter the pH level of wine")]
    chlorides: Annotated[float, Field(..., description="Enter the chlorides of wine")]
    free_sulfur_dioxide: Annotated[float, Field(..., description="Enter the free sulfur dioxide")]
    residual_sugar: Annotated[float, Field(..., description="Enter the residual sugar")]
    total_sulfur_dioxide: Annotated[float, Field(..., description="Enter the sulfur dioxide")]
    citric_acid: Annotated[float, Field(..., description="Enter the citric acid")]
    sulphates: Annotated[float, Field(..., description="Enter the sulphates")]
    fixed_acidity: Annotated[float, Field(..., description="Enter the fixed acidity")]

@app.post('/predict')
def prediction(data: UserInput):
    input = pd.DataFrame([{
        'wine_type': data.wine_type,
        'alcohol': data.alcohol,
        'density': data.density,
        'volatile_acidity': data.volatile_acidity,
        'pH': data.pH,
        'chlorides': data.chlorides,
        'free_sulfur_dioxide': data.free_sulfur_dioxide,
        'residual_sugar': data.residual_sugar,
        'total_sulfur_dioxide': data.total_sulfur_dioxide,
        'citric_acid': data.citric_acid,
        'sulphates': data.sulphates,
        'fixed_acidity': data.fixed_acidity
    }])

    predict = model.predict(input)[0]
    return JSONResponse(status_code=200, content={'prediction': int(predict)})