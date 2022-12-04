from sqlalchemy import Column,Float, Integer,DateTime,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker



eng = create_engine("sqlite:///pricing.db", echo=True)

Base= declarative_base()

class BaseDistancePrice(Base):
    __tablename__= "distance_base_price"
    id=Column(Integer, primary_key = True, index = True)
    distance=Column(Float)
    fare = Column(Float)



class DistanceAddition(Base):
    __tablename__ = "distance_addition"
    id=Column(Integer, primary_key = True, index = True)
    distance_addition = Column(Float)
    fare = Column(Float)



                                                                                                                        
class TimeFactor(Base):
    __tablename__ = "time_factor"
    id=Column(Integer, primary_key = True, index = True)
    time = Column(Integer)
    time_multiplier = Column(Float)
    



session = sessionmaker(bind=eng)

Base.metadata.create_all(eng)  





