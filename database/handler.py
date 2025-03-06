from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Load env variables from localconfig.env
from config import DATABASE_URL  

# Engine and Session creation
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    # creates table if it isnt already there
    Base.metadata.create_all(engine)
