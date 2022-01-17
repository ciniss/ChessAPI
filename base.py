from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://student19:st202119@212.182.24.105:15432/student19')

Session = sessionmaker(bind=engine)

Base = declarative_base()
