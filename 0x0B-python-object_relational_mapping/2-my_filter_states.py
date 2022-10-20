#!/usr/bin/python3
"""
displays all values in states table where name matches arguments
"""
import MySQLdb


if __name__ == "__main__":
    from sys import argv
    dbconnect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], database=argv[3])

    cursor = dbconnect.cursor()

    cursor.execute("""
        SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC
        """.format(argv[4]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    dbconnect.close()
