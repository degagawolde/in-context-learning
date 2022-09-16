import string
from tokenize import String
from urllib import response
from fastapi import FastAPI
from fastapi.logger import logger
from pydantic import BaseModel
import pickle

app = FastAPI()

#Creating a class for the attributes input to the ML model.


class EntityDocument(BaseModel):
	document: str

class NewsDocument(BaseModel):
    title: str
    description: str
    body:str
 


# #Loading the trained model
# with open("./finalized_model.pkl", "rb") as f:
#     loaded_model = pickle.load(f)

@app.post('/jdentities')
def get_entities(data: EntityDocument):
    received = data.dict()
    document = received['document']
    pred_name = 'in progress'
    
    response = {'document': document, 'prediction':  pred_name}
    logger.info(response)
    
    return response


@app.post('/bnewscore')
def get_score(data: NewsDocument):
    received = data.dict()
    title = received['title']
    description = received['description']
    body = received['body']
    
    pred_name = 'in progress'
    
    response = {'title': title, 'Prediction':  pred_name}
    logger.info(response.json())

    return response

# homepage route
@app.get("/")
def read_root():
	return {'message': 'This is the homepage of the API '}
