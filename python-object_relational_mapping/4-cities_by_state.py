#!/usr/bin/python3
"""
This script lists all `states` from the database
`hbtn_0e_0_usa` starting with `N`.
"""
import MySQLdb
import sys


def cities_by_states():
    """
    lists all states
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute('SELECT cities.id, cities.name, states.name \
                FROM cities LEFT JOIN states \
                  ON cities.state_id = states.id')

    results = cur.fetchall()

    cur.close()
    db.close()

    for row in results:
        print(row)


if __name__ == "__main__":
    cities_by_states()




