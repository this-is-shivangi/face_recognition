import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# main code start from here

class UserInput(Base):
    __tablename__ = "userinputs"

    id = Column(Integer, primary_key=True)
    house_area = Column(Integer)
    no_of_rooms = Column(Integer)
    age = Column(Integer)
    location = Column(String)

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    result = Column(Integer)
    inputs_id = Column(Integer, ForeignKey('userinputs.id'))

if __name__ == "__main__":
    engine = create_engine('sqlite:///project_db.sqlite3')
    Base.metadata.create_all(engine)

 
