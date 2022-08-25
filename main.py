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

# @app.get('/askdoc/chat-api/v1')
# def process_message():
#     print(db.keys())
#     return {
#         "message": random.choice(random_messages),
#         "link": db[random.choice(list(db.keys()))]
#     }

# @app.post('/askdoc/chat-api/v1')
# def process_message(client_message: ClientMessage = None):
    
#     result = nlu_engine.parse(client_message.message)
#     intent = result['intent']['intentName']
    
#     if not intent:
#         return {
#             "keyword_link_pair": []
#         }
#     elif intent == 'getAccommodationInfo':
#         link = select_table(Accommodation)
#     elif intent == 'careers':
#         link = select_table(Careers)
#     elif intent == 'chaplaincy':
#         link = select_table(Chaplaincy)
#     elif intent == 'societies':
#         link = select_table(Societies)
#     elif intent == 'getCourseInfo':
#         link = select_table(CourseInfo)
#     elif intent == 'crime':
#         link = select_table(Crime)
#     elif intent == 'saving money':
#         link = select_table(Discount)
#     elif intent == 'getExamAssessmentInfo':
#         link = select_table(ExamsAndAssessment)
#     elif intent == 'getFinanceInfo':
#         link = select_table(Finance)
#     elif intent == 'health':
#         link = select_table(Health)
#     elif intent == 'library':
#         link = select_table(Library)
#     elif intent == 'mental health':
#         link = select_table(MentalHealth)
#     elif intent == 'studentStatusAndEnrolment':
#         link = select_table(StudentStatus)
#     elif intent == 'success':
#         link = select_table(Success)
#     else: # travel
#         link = select_table(Travel)

#     if not link:
#         return {
#             "keyword_link_pair": link
#         }
#     return {
#         "keyword_link_pair": [{"keyword": keyword, "link":data} for keyword, data in link]
#     }
    

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
        link = select_no_category_table(Doctor)
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
    else: # tuition fees
        link = select_no_category_table(TuitionFees)

    if not link:
        return {
            "keyword_link_pair": link
        }
    return {
        "keyword_link_pair": [{"keyword": keyword, "link":data} for keyword, data in link]
    }