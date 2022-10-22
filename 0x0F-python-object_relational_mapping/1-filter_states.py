#!/usr/bin/python3
"""This script lists all states with a name starting with N"""


if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name
<<<<<<< HEAD
                LIKE (%s) ORDER BY id ASC", ('%N'))
=======
                LIKE (%s) ORDER BY id ASC", ('N%',))
>>>>>>> d643fb27f974f2388e132450e573bcb7d7cbc18c
    rows = cur.fetchall()
    for row in rows:
        print(row)
