from db import engine
from models.data_models import *
from sqlmodel import Session, select, or_

def select_first_finance():
    with Session(engine) as session:
        statement = select(Finance).where(Finance.id == 1)
        result = session.exec(statement)
        first = result.first()
        return first.link
    
def select_first_accommodation():
    with Session(engine) as session:
        statement = select(Accommodation).where(Accommodation.id == 1)
        result = session.exec(statement)
        first = result.first()
        return first.link
    
def select_first_exams():
    with Session(engine) as session:        
        statement = select(ExamsAndAssessment).where(ExamsAndAssessment.id == 1)
        result = session.exec(statement)
        first = result.first()
        return first.link
    
def select_first_travel():
    with Session(engine) as session:
        statement = select(Travel).where(Travel.id == 1)
        result = session.exec(statement)
        first = result.first()
        return first.link
    
def select_first_clubs():
    with Session(engine) as session:
        statement = select(Societies).where(Societies.id == 1)
        result = session.exec(statement)
        first = result.first()
        return first.link

