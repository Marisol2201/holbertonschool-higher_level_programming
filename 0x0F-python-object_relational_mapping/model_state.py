#!/usr/bin/python3
"""contains the class definition of a State and an
...instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# returns a new base class from which all mapped classes should inherit
Base = declarative_base()


class State(Base):
    """When the class definition is completed, a new Table and mapper() will
    ...have been generated"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
