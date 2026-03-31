import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.linear_model import LinearRegression
from pydantic import BaseModel
app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

df = pd.read_csv("dataset/house_data.csv")
X = df[["size","bedrooms","age"]]
y = df["price"]
model = LinearRegression()
model.fit(X,y)
print("Training Completed !!!")
class HouseDetails(BaseModel):
    size : float
    bedrooms : int
    age : int
@app.post("/predict")
def predict_price(input:HouseDetails):
    house_details = np.array([[input.size,input.bedrooms,input.age]])
    price = model.predict(house_details)

    return{
        "predicted_price" : price[0]
    }
