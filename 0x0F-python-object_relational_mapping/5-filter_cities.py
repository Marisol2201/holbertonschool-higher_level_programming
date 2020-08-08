#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of
...that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    """Your code should not be executed when imported"""

    state = sys.argv[4]
    # Open database connection
    dbconf = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3],)

    # create a Cursor object. It will let you execute all the queries you need
    cur = dbconf.cursor()

    cur.execute("""SELECT cities.name
                FROM cities
                INNER JOIN states ON states.id = cities.state_id
                WHERE states.name=%s
                ORDER BY cities.id ASC
                """, (sys.argv[4],))

    states = cur.fetchall()
    list_states = []

    if states:
        for state in states:
            list_states.append(state[0])
    print(", ".join(list_states))

    # disconnect from server
    cur.close()
    dbconf.close()
