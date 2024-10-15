#!/usr/bin/python3
"""Module
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Attritbute
    """
    # Capture arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=db_name)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the query to list all states sorted by id in ascending order
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the executed query
    states = cur.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cur.close()
    db.close()
