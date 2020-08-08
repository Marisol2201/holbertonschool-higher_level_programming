#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """Your code should not be executed when imported"""

    # This engine just used to query for list of databases
    mysql_engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
        sys.argv[1], sys.argv[2],
        'localhost', 3306, sys.argv[3]))

    # create a configured "Session" class and create a Session
    Session = sessionmaker(bind=mysql_engine)
    session = Session()

    session.query(State).filter(State.id == 2).update(
        {State.name: 'New Mexico'})
    session.commit()
