#!/usr/bin/python3
"""contains the class definition of a City"""

from model_state import State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """links to the MySQL table cities"""
    __tablename__ = 'cities'
    id = Column(
        Integer, primary_key=True, autoincrement=True,
        unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
