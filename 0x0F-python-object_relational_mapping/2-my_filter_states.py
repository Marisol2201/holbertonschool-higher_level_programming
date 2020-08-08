#!/usr/bin/python3
"""takes in an argument and displays all values in the states table of
...hbtn_0e_0_usa where name matches the argument"""

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

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    states = cur.fetchall()

    for state in states:
        if state[1] == sys.argv[4]:
            print(state)

    # disconnect from server
    cur.close()
    dbconf.close()
