#!/usr/bin/python3
"""
List all cities and corresponding states of given database where name matches arguments
"""
import MySQLdb


if __name__ == "__main__":
    from sys import argv
    dbconnect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], database=argv[3])

    cursor = dbconnect.cursor()

    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC""")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    dbconnect.close()
