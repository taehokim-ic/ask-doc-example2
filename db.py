from sqlmodel import create_engine, SQLModel
from models.data_models2 import *

# db_file_name = "ask_doc_db"
# DATABASE_URL = f"postgresql://postgres:password@localhost/{db_file_name}"

db_file_name = "database2.db"
DATABASE_URL = f"sqlite:///{db_file_name}"

engine = create_engine(DATABASE_URL, echo=False)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()

