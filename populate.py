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
    
discount = [
    ("local_offers_college_near", "https://www.imperial.ac.uk/human-resources/benefits/saving-you-money/local-discounts/"),
    ("tips_saving", "https://www.imperial.ac.uk/students/new-students/postgraduates/fees-and-funding/managing-your-money/money-saving-tips/"),
    ("finance_banking_save_jobs_food", "https://www.savethestudent.org/"),
    ("clothing_food_electronics_discounts", "https://www.myunidays.com/GB/en-GB"),
    ("food_drink_fashion_health_beauty", "https://www.studentbeans.com/uk"),
    ("vegan", "https://www.imperial.ac.uk/food-and-drink/catering-outlets/plantworks/"),
    ("loyaltee_wallet_rewards", "https://yoyogroup.com/products/yoyowallet/")
]

crime = [
    ("Incident_report_crime", "https://www.imperial.ac.uk/estates-facilities/customer-services-centre/report-issue/report-crimes-incidents/"),
    ("customer_service", "https://www.imperial.ac.uk/estates-facilities/customer-services-centre/"),
]

chaplaincy = [
    ("chaplain_meditation_prayer", "https://www.imperial.ac.uk/chaplaincy/visiting-the-chaplaincy/"),
    ("islam_muslim_prayer", "https://www.imperial.ac.uk/chaplaincy/visiting-the-chaplaincy/opportunities-for-muslim-prayers/"),
    ("prayer_room", "https://www.imperial.ac.uk/chaplaincy/visiting-the-chaplaincy/multi-faith-prayer-rooms/"),
    ("mindfulness_mediation", "https://www.imperial.ac.uk/chaplaincy/practicing-meditation/")
]


health = [
    ("health_centre", "https://www.imperialcollegehealthcentre.co.uk/"),
    ("appointments", "https://www.imperialcollegehealthcentre.co.uk/book-appointment"),
    ("register_new", "https://www.imperialcollegehealthcentre.co.uk/new-patients/"),
    ("prescription_repeat", "https://systmonline.tpp-uk.com/2/Login?Date=20220812154443"),
    ("teeth_tooth_dentist", "https://www.imperialcollegedental.co.uk/")
]

library = [
    ("library_books_study_cafe_learn_group_borrow_theses_referencing", "https://www.imperial.ac.uk/admin-services/library/")
]

course_info = [
    ("course_regulations_weightings_specifications_noticeboard_first_second_third_fourth", "https://www.imperial.ac.uk/computing/current-students/computing/"), 
    ("extracurricular_languagues_horizons_humanities_change", "https://www.imperial.ac.uk/horizons"), 
    ("horizons_enrolement", "https://www.imperial.ac.uk/horizons/enrolment/"), 
    ("i-explore_credit", "https://www.imperial.ac.uk/students/academic-support/i-explore/")
]

success = [
    ("procrastination_stress_management_mindfulness", "https://www.imperial.ac.uk/admin-services/ict/training-and-resources/inclusive-technology/procrastination-and-stress-management/"),
    ("revision_revising", "https://www.imperial.ac.uk/admin-services/ict/training-and-resources/inclusive-technology/revision/"),
    ("organisation_time_management", "https://www.imperial.ac.uk/admin-services/ict/training-and-resources/inclusive-technology/organisation-and-time-management/")
]

careers = [
    ("job_vacancies_events_appointments", "https://imperial.targetconnect.net/unauth/student/login"),
    ("career_interview_applications_jobs", "https://www.imperial.ac.uk/careers/applications-and-interviews/cv/"),
    ("personal_devlopment_self_reflection_experience", "https://www.imperial.ac.uk/students/imperial-award/")
]

tables = [
    (finance, Finance), 
    (exams, ExamsAndAssessment), 
    (student_status, StudentStatus), 
    (accommodation, Accommodation), 
    (travel, Travel), 
    (societies, Societies),
    (discount, Discount), 
    (crime, Crime), 
    (health, Health), 
    (library, Library), 
    (course_info, CourseInfo), 
    (success, Success),
    (careers, Careers),
    (chaplaincy, Chaplaincy)
]

def create_discount_db():
    with Session(engine) as session:
        for keyword, link in discount:
            session.add(Discount(keyword=keyword, link=link))
            session.commit()

def create_crime_db():
    with Session(engine) as session:
        for keyword, link in crime:
            session.add(Crime(keyword=keyword, link=link))
            session.commit()

def create_health_db():
    with Session(engine) as session:
        for keyword, link in health:
            session.add(Health(keyword=keyword, link=link))
            session.commit()

def create_library_db():
    with Session(engine) as session:
        for keyword, link in library:
            session.add(Library(keyword=keyword, link=link))
            session.commit()

def create_course_info_db():
    with Session(engine) as session:
        for keyword, link in course_info:
            session.add(CourseInfo(keyword=keyword, link=link))
            session.commit()

def create_success_db():
    with Session(engine) as session:
        for keyword, link in success:
            session.add(Success(keyword=keyword, link=link))
            session.commit()

def create_careers_db():
    with Session(engine) as session:
        for keyword, link in careers:
            session.add(Careers(keyword=keyword, link=link))
            session.commit()

def create_chaplaincy_db():
    with Session(engine) as session:
        for keyword, link in chaplaincy:
            session.add(Chaplaincy(keyword=keyword, link=link))
            session.commit()

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
    create_health_db()
    create_chaplaincy_db()
    create_library_db()
    create_success_db()
    create_careers_db()
    create_course_info_db()
    create_discount_db()
    create_crime_db()

