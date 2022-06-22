from fastapi import FastAPI, Response

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
