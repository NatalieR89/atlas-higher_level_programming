#!/usr/bin/python3
"""
Module
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Attribute
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute({
            'name': argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)