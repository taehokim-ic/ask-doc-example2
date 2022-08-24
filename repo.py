from db import engine
from models.data_models import *
from sqlmodel import Session, select, or_


def select_table(table):
    with Session(engine) as session:
        statement = select(table)
        result = session.exec(statement)
        first = result.all()
        print(first)
        if not first:
            return []
        return [(row.keyword, row.link) for row in first]