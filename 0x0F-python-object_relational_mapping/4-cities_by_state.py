#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    """Your code should not be executed when imported"""

    # Open database connection
    dbconf = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3],)

    # create a Cursor object. It will let you execute all the queries you need
    cur = dbconf.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states\
                ON states.id = cities.state_id\
                ORDER BY cities.id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

    # disconnect from server
    cur.close()
    dbconf.close()
