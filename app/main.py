from fastapi import FastAPI
from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging
from loguru import logger

#FastAPI uses these specification directly, including documentation, so these are important
class PolarityScores(BaseModel):
    pos: float
    compound: float
    neu: float
    neg: float

class Request(BaseModel):
    phrase: str

app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

# Server
import uvicorn
from fastapi import FastAPI

# Modeling

app = FastAPI(title='This ones sentimental', version='0.1',
              description='A FastApi serving of vaderSentiment')

# Initialize logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename='sample.log')

log_format = "{time} | {level} | {message} | {file} | {line} | {function} | {exception}"
logger.add(sink='app/data/log_files/logs.log', format=log_format, level='DEBUG', compression='zip')

@app.get('/')
@app.get('/home')
async def read_home():
    """
    Home endpoint which can be used to test the availability of the application.

    :return: Dict with key 'message' and value 'Fake or Not API live!'
    """
    logger.debug('User checked the root page')
    return {'message': 'Fake or Not API live!'}

@app.post("/predict", response_model=PolarityScores)    
def sentiment(request: Request):
    print(request)
    return analyzer.polarity_scores(request.phrase)

if __name__ == "__main__":
    # Run app with uvicorn with port and host specified. Host needed for docker port mapping
    uvicorn.run(app, port=24601, host="0.0.0.0")
