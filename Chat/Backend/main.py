from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel

App=FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://127.0.0.1:5500",
]

App.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@App.get("/get-messages")
def get_messages ():
    with open ("messages.json","rb") as f:
        messages=f.read()
        return Response (content=messages)

class Message (BaseModel):
    login:str
    content:str

@App.post("/send-message")
def send_message (message:Message):
    with open ("messages.json","r") as m:
        messages=json.loads(m.read())
        messages.append({"login":message.login,"content":message.content})
    with open ("messages.json", "w") as wr:
        wr.write(json.dumps(messages))



