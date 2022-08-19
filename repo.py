from db import engine
from models.data_models import *
from sqlmodel import Session, select, or_

def select_first_finance():
    with Session(engine) as session:
        statement = select(Finance)
        result = session.exec(statement)
        first = result.all()
        print(first)
        return [(row.keyword, row.link) for row in first]
    
def select_first_accommodation():
    with Session(engine) as session:
        statement = select(Accommodation)
        result = session.exec(statement)
        first = result.all()
        print(first)
        return [(row.keyword, row.link) for row in first]
    
def select_first_exams():
    with Session(engine) as session:        
        statement = select(ExamsAndAssessment)
        result = session.exec(statement)
        first = result.all()
        print(first)
        return [(row.keyword, row.link) for row in first]
    
def select_first_travel():
    with Session(engine) as session:
        statement = select(Travel).where(Travel.id == 1)
        result = session.exec(statement)
        first = result.all()
        print(first)
        return [(row.keyword, row.link) for row in first]
    
def select_first_clubs():
    with Session(engine) as session:
        statement = select(Societies)
        result = session.exec(statement)
        first = result.all()
        print(first)
        return [(row.keyword, row.link) for row in first]
