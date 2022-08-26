from fastapi import FastAPI
from pydantic import BaseModel
from nlu_engine import nlu_engine
from repo import *

from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI()

random_messages = [
    "This is the result you're looking for",
    "Please follow the link for more information"
]

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        # you probably want some kind of logging here
        return Response("Internal server error", status_code=500)
        
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

@app.post('/askdoc/chat-api/v1')
def process_message(client_message: ClientMessage = None):
    
    result = nlu_engine.parse(client_message.message)
    intent = result['intent']['intentName']
    
    if not intent:
        return {
            "keyword_link_pair": []
        }
    elif intent == 'general_accmoodation':
        link = select_no_category_table(GeneralAccommodation)
    elif intent == 'careers':
        link = select_no_category_table(Careers)
    elif intent == 'crime':
        link = select_no_category_table(Crime)
    elif intent == 'finances':
        link = select_no_category_table(Finances)
    elif intent == 'doctor':
        link = select_no_category_table(Doctor)
    elif intent == 'dental':
        link = select_no_category_table(Dental)
    elif intent == 'library':
        link = select_no_category_table(Library)
    elif intent == 'mental_health':
        link = select_no_category_table(MentalHealth)
    elif intent == 'private_housing':
        link = select_no_category_table(PrivateHousing)
    elif intent == 'summer_accommodation':
        link = select_no_category_table(SummerAccommodation)
    elif intent == 'specific_halls':
        slots = result["slots"][0]
        print(slots)
        if len(slots) > 0:
            print(slots["value"]["value"])
            link = select_category_table(SpecificHalls, slots["value"]["value"])
        else:
            link = ""
    elif intent == 'hall_senior':
        link = select_no_category_table(HallSenior)
    elif intent == 'discount':
        link = select_no_category_table(Discount)
    elif intent == 'mitigation':
        link = select_no_category_table(Mitigation)
    elif intent == 'student_status':
        link = select_no_category_table(StudentStatus)
    elif intent == 'societies':
        link = select_no_category_table(Societies)    
    elif intent == 'chaplaincy':
        link = select_no_category_table(Chaplaincy)
    elif intent == 'travel':
        link = select_no_category_table(Travel)            
    else: # tuition fees
        link = select_no_category_table(TuitionFees)

    if not link:
        return {
            "keyword_link_pair": [link]
        }
    return {
        "keyword_link_pair": [{"keyword": keyword, "link":data} for keyword, data in link]
    }