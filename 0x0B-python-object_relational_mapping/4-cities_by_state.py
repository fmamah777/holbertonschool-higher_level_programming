#!/usr/bin/python3
"""
This python script lists all cities from hbtn_0e_4_usa database
"""


import MySQLdb


def select_state():
    """
    This method lists all the cities from hbtn_0e_4_usa database
    """
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities, states\
                    WHERE cities.state_id = states.id\
                    ORDER BY cities.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    select_state()
