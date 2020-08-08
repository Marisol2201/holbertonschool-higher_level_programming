#!/usr/bin/python3
"""takes in arguments and displays all values in the states table of
...hbtn_0e_0_usa where name matches the argument. But this time, write
...one that is safe from MySQL injections!"""

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

    cur.execute("""SELECT * FROM states
                WHERE name=%s 
                ORDER BY states.id ASC""", (sys.argv[4],))

    states = cur.fetchall()

    for state in states:
        print(state)

    # disconnect from server
    cur.close()
    dbconf.close()
