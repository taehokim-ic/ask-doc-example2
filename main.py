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
    
    if intent == 'general_accommodation':
        link = select_no_category_table(GeneralAccommodation)
    elif intent == 'careers':
        link = select_no_category_table(Careers)
    elif intent == 'study_interruption':
        link = select_no_category_table(StudyInterruption)
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
        result_slot = result["slots"]
        
        if len(result_slot) > 0:
            slots = result_slot[0]
            if len(slots) > 0:
                link = select_category_table(SpecificHalls, slots["value"]["value"])
        else:
            link = ""
    elif intent == 'hall_senior':
        link = select_no_category_table(HallSenior)
    elif intent == "academic_appeal":
        link = select_no_category_table(AcademicAppeal)
    elif intent == 'discount':
        link = select_no_category_table(Discount)
    elif intent == 'mitigation':
        link = select_no_category_table(Mitigation)
    elif intent == 'student_status':
        link = select_no_category_table(StudentStatus)
    elif intent == 'societies':
        link = select_no_category_table(Societies)
    elif intent == 'eating_discorder':
        link = select_no_category_table(EatingDisorder)
    elif intent == 'exercise':
        link = select_no_category_table(Exercise)
    elif intent == 'food_and_drinks':
        link = select_no_category_table(FoodAndDrinks)
    elif intent == 'illness':
        link = select_no_category_table(Illness)
    elif intent == 'mental_crisis':
        link = select_no_category_table(MentalCrisis)
    elif intent == 'self_harm':
        link = select_no_category_table(SelfHarm)            
    elif intent == 'chaplaincy':
        link = select_no_category_table(Chaplaincy)
    elif intent == 'travel':
        link = select_no_category_table(Travel)
    elif intent == 'exam_revision':
        link = select_no_category_table(ExamRevision)                     
    elif intent == 'tuition_fees': # tuition fees
        link = select_no_category_table(TuitionFees)
    elif intent == 'friends':
        link = select_no_category_table(Friends)
    elif intent == 'arithmetic_mark_check':
        link = select_no_category_table(ArithmeticMarkCheck)
    elif intent == 'course_info_y1':
        # NO SLOTS
        link = select_category_module_table(CourseInfo, category="first year")
    elif intent == 'course_info_y2':
        # NO SLOTS
        link = select_category_module_table(CourseInfo, category="second year")
    elif intent == 'course_info_y3':
        # NO SLOTS
        link = select_category_module_table(CourseInfo, category="third year")
    elif intent == 'course_info_y4':
        # NO SLOTS
        link = select_category_module_table(CourseInfo, category="fourth year")
    elif intent == 'docsoc':
        # NO SLOTS
        link = [("DoCSoC", "https://docsoc.co.uk/")]
    elif intent == 'doc':
        link = [("DoC FAQs", "/2122/questions")]
    else:
        link = ""
    if not link:
        return {
            "keyword_link_pair": [link]
        }
    return {
        "keyword_link_pair": [{"keyword": keyword, "link":data} for keyword, data in link]
    }