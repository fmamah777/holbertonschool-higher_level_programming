#!/usr/bin/python3
""" lists all cities of a state given as an argument
from the hbtn_0e_4_usa DB.
"""
import MySQLdb


if __name__ == "__main__":
    from sys import argv
    dbconnect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], database=argv[3])

    cursor = dbconnect.cursor()

    cursor.execute("""
        SELECT cities.name FROM states
        JOIN cities ON cities.state_id = states.id
        WHERE states.name = '{}'
        ORDER BY cities.id ASC
        """.format(argv[4].split()[0]))

    print(', '.join(row[0] for row in cursor.fetchall()))

    cursor.close()
    dbconnect.close()
