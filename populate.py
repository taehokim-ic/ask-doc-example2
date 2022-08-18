from sqlmodel import Session

from db import engine
from models.data_models import *

finance = [
    ("tuition_fees", "https://www.imperial.ac.uk/students/fees-and-funding/tuition-fees/undergraduate-tuition-fees/2022-23/faculty-of-engineering/"),
    ("tuition_fees", "https://www.imperial.ac.uk/study/ug/fees-and-funding/loans-and-grants/tuition-loan/"),
    ("maintenance_loan_home", "https://www.imperial.ac.uk/study/ug/fees-and-funding/loans-and-grants/tuition-loan/"),
    ("tuition_fees_loan_home", "https://www.imperial.ac.uk/study/ug/fees-and-funding/loans-and-grants/tuition-loan/"),
    ("canadian_loan", "https://www.imperial.ac.uk/study/ug/fees-and-funding/loans-and-grants/canadian-loans/"),
    ("us_loan", "https://www.imperial.ac.uk/study/ug/fees-and-funding/loans-and-grants/us-loans/"),
    ("hardship_fund", "https://www.imperial.ac.uk/computing/current-students/-doc-hardship-fund/"),
    ("cost_of_living", "https://www.imperial.ac.uk/study/ug/fees-and-funding/managing-your-money/living-costs/"),
    ("financial assistance", "https://www.imperial.ac.uk/students/fees-and-funding/financial-assistance/student-support-fund/")
]

exams = [
    ("mitigation_cw_form", "https://imperiallondon.sharepoint.com/sites/UG-DocMitigations-CO/_layouts/15/AccessDenied.aspx?Source=https%3A%2F%2Fimperiallondon%2Esharepoint%2Ecom%2Fsites%2FUG%2DDocMitigations%2DCO&correlation=a9ef58a0%2Df037%2D4000%2Dd051%2D627321c1d153"),
    ("mitigation_exam_form", "https://imperiallondon.sharepoint.com/sites/UG-DocMitigations-CO/Lists/Mitigation_Circumstances_for_assessments/AllItems.aspx")
]

student_status = [
    ("interrupt_studies", "https://www.imperial.ac.uk/student-support-zone/advice/my-student-status/interrupting-your-studies/"),
    ("my_imperial", "https://www.imperial.ac.uk/admin-services/ict/self-service/admin-systems/my-imperial/"),
    ("official_doc_request", "https://www.imperial.ac.uk/student-records-and-data/for-current-students/request-an-official-document/"),
    ("reg_status_change", "https://www.imperial.ac.uk/student-records-and-data/for-current-students/undergraduate-and-taught-postgraduate/changes-to-registration-status/"),
    ("personal_details_change", "https://www.imperial.ac.uk/student-records-and-data/for-current-students/undergraduate-and-taught-postgraduate/changes-to-personal-details/")
]

accommodation = [
    ("wilson_general_info", "https://www.imperial.ac.uk/students/accommodation/prospective/ug/ug/wilson-house/"), 
    ("kempporter_general_info", "https://www.imperial.ac.uk/students/accommodation/prospective/ug/ug/kemp-porter/"),
    ("woodward_general_info", "https://www.imperial.ac.uk/students/accommodation/prospective/ug/ug/woodward/"),
    ("southside_general_info", "https://www.imperial.ac.uk/students/accommodation/prospective/ug/ug/southside/"),
    ("eastside_general_info", "https://www.imperial.ac.uk/students/accommodation/prospective/ug/ug/eastside/"),
    ("beit_general_info", "https://www.imperial.ac.uk/students/accommodation/prospective/ug/ug/beit/"),
    ("xenia_general_info", "https://www.imperial.ac.uk/students/accommodation/prospective/ug/ug/xenia/"),
    ("putneyb_general_info", "https://www.imperial.ac.uk/students/accommodation/prospective/ug/ug/boathouse/"),
    ("evelyng_general_info", "https://www.imperial.ac.uk/students/accommodation/current-residents/afterfirstyear/returning-students-accommodation/"),
    ("parsons_general_info", "https://www.imperial.ac.uk/students/accommodation/current-residents/afterfirstyear/parsons/"),
    ("woodward_residents_site", "https://woodward.halls.imperial.ac.uk/"),
    ("kempporter_residents_site", "https://kempporter.halls.imperial.ac.uk/#"),
    ("wilson_residents_site", "https://wilson.halls.imperial.ac.uk/"),
    ("find_flatmate", "https://web.yammer.com/main/org/ic.ac.uk/feed")
]

travel = [
    ("shuttle_bus_imp", "https://www.imperial.ac.uk/estates-facilities/travel/shuttle-bus/"),
    ("cycling_imp", "https://www.imperial.ac.uk/estates-facilities/travel/cycling/"),
    ("travel_options", "https://www.imperial.ac.uk/study/living-in-london/getting-around/"),
    ("oyster_tfl_discount", "https://www.imperial.ac.uk/student-records-and-data/for-current-students/student-travel-discounts/")
]

societies = [
    ("list_activities_clubs_socieites", "https://www.imperialcollegeunion.org/activities/a-to-z"),
    ("new_society_club", "https://www.imperialcollegeunion.org/activities/start-something-new"),
    ("arts_music_drama_art", "https://www.imperialcollegeunion.org/activities/arts"),
    ("media", "https://www.imperialcollegeunion.org/activities/media"),
    ("athletes_sports", "https://www.imperialcollegeunion.org/activities/imperial-athletes"),
    ("tankards_engraving", "https://www.imperialcollegeunion.org/activities/tankards"),
    ("appeals_misconduct_supervisor_circumstances", "https://www.imperialcollegeunion.org/advice/academic-issues"),
    ("complaints", "https://www.imperialcollegeunion.org/advice/complaints"),
    ("feedback", "https://www.imperialcollegeunion.org/advice/feedback"),
    ("whatson_events_calender", "https://www.imperialcollegeunion.org/whats-on/listings/upcoming"),
    ("food_drink", "https://www.imperialcollegeunion.org/food-drink"),
    ("book_venue_bar", "https://www.imperialcollegeunion.org/food-drink/book-bar"),
    ("shop_merch_clothes_memorabillia", "https://www.imperialcollegeunion.org/shop/products")
]

def create_finance_db():
    with Session(engine) as session:
        for keyword, link in finance:
            session.add(Finance(keyword=keyword, link=link))
            session.commit()

def create_accommodation_db():
    with Session(engine) as session:
        for keyword, link in accommodation:
            session.add(Accommodation(keyword=keyword, link=link))
            session.commit()

        
def create_exams_db():
    with Session(engine) as session:
        for keyword, link in exams:
            session.add(ExamsAndAssessment(keyword=keyword, link=link))
            session.commit()
            
def create_travel_db():
    with Session(engine) as session:
        for keyword, link in travel:
            session.add(Travel(keyword=keyword, link=link))
            session.commit()

def create_clubs_db():
    with Session(engine) as session:
        for keyword, link in societies:
            session.add(Societies(keyword=keyword, link=link))
            session.commit()            
            
if __name__ == "__main__":            
    create_accommodation_db()
    create_finance_db()
    create_exams_db()
    create_travel_db()
    create_clubs_db()

