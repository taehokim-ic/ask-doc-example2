from db import engine
from models.data_models2 import *
from sqlmodel import Session, select, or_


def select_no_category_table(table):
    with Session(engine) as session:
        statement = select(table)
        result = session.exec(statement)
        first = result.all()
        print(first)
        if not first:
            return []
        return [(row.keyword, row.link) for row in first]

def select_category_table(table, category):
    with Session(engine) as session:
        statement = select(table).where(table.category == category)
        result = session.exec(statement)
        first = result.all()
        if not first:
            return []
        return [(row.keyword, row.link) for row in first]
    
def select_category_module_table(table, category="general",module="general"):
    with Session(engine) as session:
        statement = select(table).where(table.category == category).where(table.module == module)
        result = session.exec(statement)
        first = result.all()
        if not first:
            return []
        return [(row.keyword, row.link) for row in first]
    
def add_message(message: str, table=Questions):
    with Session(engine) as session:
        session.add(table(message=message))
        session.commit()