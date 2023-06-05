from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str

@app.get("/", response_class=HTMLResponse)
def get_started():
    return '''
    <html>
    <head>
        <title>Get Started</title>
        <style>
            input{
                align: center;
            }
        </style>
    </head>
    <body>
        <h1 align="center">Language Detection</h1>
        <form method="get" action="/form">
            <input type="submit" value="get started">
        </form>
    </body>
    </html>
    '''

@app.get("/form", response_class=HTMLResponse)
def form():
    return '''
    <html>
    <head>
    <title>Form</title>
    </head>
    <body>
        <form method="get" action="/predict">
            Text: <input type="text" name="text">
            <input type="submit">
        </form>
    </body>
    </html>
    '''

@app.get("/predict")
def predict(text):
    language = predict_pipeline(text)
    return {"Langauge": language}

# run command :- app.main:app --reload