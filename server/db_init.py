from db_config import *
from sqlalchemy import inspect
import db_models

def init_db():
    Base.metadata.create_all(bind=engine)

def print_all_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tables in the database:")
    for table in tables:
        print(table)

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
    print_all_tables()