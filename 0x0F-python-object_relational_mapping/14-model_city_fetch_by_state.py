#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_city import City
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

    # create a configured "Session" class and create a Session
    query = session.query(City, State).join(State)
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
