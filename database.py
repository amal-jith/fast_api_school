

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:amal1998@localhost/school"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()

# try:
#     engine = create_engine(DATABASE_URL)
#     with engine.connect() as connection:
#         print("Connected to the database successfully!")
# except Exception as e:
#     print(f"Error connecting to the database: {e}")



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()