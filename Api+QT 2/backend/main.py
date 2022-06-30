from fastapi import FastAPI, Response
from json import loads
from typing import List
from pydantic import BaseModel


App=FastAPI()

@App.get("/get-surveys")
def get_surveys():
    with open("surveys.txt","r") as f:
        surveys_text=f.read()
        surveys_list=surveys_text.split()
        return surveys_list

@App.get("/surveys/{name}")
def get_survey(name):
    with open (f"{name}.json","r") as f:
        return Response(content=f.read())

class Answer(BaseModel):
    id  :str
    symbol  :str

@App.post("/surveys/{name}")
def post_answers(name :str,answers  :List[Answer]):
    print(answers)
    scores = {'spalanie':0,'aerodynamika':0}
    with open (f"{name}_meta.json","r") as f:
        meta_model=loads(f.read())
    for a in answers:
        category=meta_model[a.id]["category"]
        change=meta_model[a.id][a.symbol]
        scores[category]+=change
    return scores




