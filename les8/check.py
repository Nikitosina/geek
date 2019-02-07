import sqlite3


def check(name='weather'):
    conn = sqlite3.connect("{}.db".format(name))
    cursor = conn.cursor()

    # print("Here's a listing of all the records in the table:")
    for row in cursor.execute("SELECT rowid, * FROM weather"):
        print(row)
