#!/usr/bin/python3
"""Definition of the class City"""

from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship



class City(State):
    """Class City"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://brook:Volcano27!@localhost/hbtn_0d_usa')
    Base.metadata.create_all(engine)
