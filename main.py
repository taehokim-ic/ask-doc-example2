# import random
from fastapi import FastAPI
from pydantic import BaseModel
from nlu_engine import nlu_engine
from repo import *

from starlette.middleware.cors import CORSMiddleware
# from starlette.requests import Request
# from starlette.responses import Response

app = FastAPI()

db = {
    "tuition": "https://www.imperial.ac.uk/students/fees-and-funding/tuition-fees/undergraduate-tuition-fees/2022-23/faculty-of-engineering/",
    "loan": "https://www.imperial.ac.uk/study/ug/fees-and-funding/loans-and-grants/tuition-loan/",
    "mitigation": "https://imperiallondon.sharepoint.com/sites/UG-DocMitigations-CO/_layouts/15/AccessDenied.aspx?Source=https%3A%2F%2Fimperiallondon%2Esharepoint%2Ecom%2Fsites%2FUG%2DDocMitigations%2DCO&correlation=a9ef58a0%2Df037%2D4000%2Dd051%2D627321c1d153"
}

random_messages = [
    "This is the result you're looking for",
    "Please follow the link for more information"
]

# async def catch_exceptions_middleware(request: Request, call_next):
#     try:
#         return await call_next(request)
#     except Exception:
#         # you probably want some kind of logging here
#         return Response("Internal server error", status_code=500)
        
app.middleware('http')(catch_exceptions_middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClientMessage(BaseModel):
    message: str
    
    class Config:
        orm_mode = True

# @app.get('/askdoc/chat-api/v1')
# def process_message():
#     print(db.keys())
#     return {
#         "message": random.choice(random_messages),
#         "link": db[random.choice(list(db.keys()))]
#     }

@app.post('/askdoc/chat-api/v1')
def process_message(client_message: ClientMessage = None):
    
    result = nlu_engine.parse(client_message.message)
    intent = result['intent']['intentName']
    
    if not intent:
        link = ''
    elif intent == 'getAccommodationInfo':
        link = select_first_accommodation()
    # elif intent == 'careers':
    #     pass
    # elif intent == 'chaplaincy':
    #     pass
    elif intent == 'societies':
        link = select_first_clubs()
    # elif intent == 'getCourseInfo':
    #     pass
    # elif intent == 'crime':
    #     pass
    # elif intent == 'saving money':
    #     pass
    elif intent == 'getExamAssessmentInfo':
        link = select_first_exams()
    elif intent == 'getFinanceInfo':
        link = select_first_finance()
    # elif intent == 'health':
    #     pass
    # elif intent == 'library':
    #     pass
    # elif intent == 'mental health':
    #     pass
    # elif intent == 'studentStatusAndEnrolment':
    #     pass
    # elif intent == 'success':
    #     pass
    else: # travel
        link = select_first_travel()

    return {
        "keyword_link_pair": [
            {
                "keyword": "wilson",
                "link": link
            }
        ]
    }
    
# def link_preview_json(link: str, message: str) -> dict:
#     result: dict = {}
#     result["message"] = message
#     result["preview_objects"] = []
#     if link:
#         preview = link_preview(link, parser="lxml")
#         result["preview_objects"].append({
#             "link": link,
#             "title": preview.title,
#             "description": preview.description,
#             "image": preview.image
#         })        
#     else:
#         return result

# def fetch_data_from():
#     return
