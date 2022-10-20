#!/usr/bin/python3
"""
This python script lists all cities from hbtn_0e_4_usa database
"""


import MySQLdb


def filter_cities():
    """
    This method lists all the cities from hbtn_0e_4_usa database
    """
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()

    state = sys.argv[4]

    cur.execute("SELECT name\
                    FROM cities\
                    WHERE state_id = (SELECT id\
                                      FROM states\
                                      WHERE name = %(name)s)\
                                      ORDER BY id", {'name': state})

    rows = cur.fetchall()

    length = len(rows)
    if length == 0:
        print()
        return

    for i in range(0, length - 1):
        print("{}".format(rows[i][0]), end=", ")
    print("{}".format(rows[len(rows) - 1][0]))

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
