# <YOUR_IMPORTS>
import os
import dill
import json
import pandas as pd
from pydantic import BaseModel
from datetime import datetime




class Form(BaseModel):
    description: str
    fuel: str
    id: int
    image_url: str
    lat: float
    long: float
    manufacturer: str
    model: str
    odometer: float
    posting_date: str
    price: float
    region: str
    region_url: str
    state: str
    title_status: str
    transmission: str
    url: str
    year: int





class Prediction(BaseModel):

    id: int
    pred: str
    price: float







path = os.environ.get('PROJECT_PATH', '.')

def predict():
    model = dill.load(open(f'{path}/data/models/cars_pipe_202408021836.pkl', 'rb'))
    files = os.listdir(f'{path}/data/test')
    combined_df = pd.DataFrame()
    for x in files:
        with open(path+files) as f:
            data = json.load(f)

            df = pd.DataFrame([data])

            combined_df = pd.concat([combined_df, df], ignore_index=True)
    combined_df.to_csv(f'{path}/data/predictions/predict{datetime.now().strftime("%Y%m%d%H%M")}.csv')



if __name__ == '__main__':
    predict()
