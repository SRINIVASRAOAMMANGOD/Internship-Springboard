import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Always drop if you want a fresh table
cur.execute("DROP TABLE IF EXISTS EMPLOYEE")

cur.execute('''
    CREATE TABLE EMPLOYEE (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        EMPLOYEE_NAME TEXT,
        AGE INTEGER
    )''')

cur.execute("INSERT INTO EMPLOYEE (EMPLOYEE_NAME, AGE) VALUES ('John Doe', 30)")

# Correct way to pass multiple values
data = [("Bob", 30), ("Charlie", 22)]
cur.executemany("INSERT INTO EMPLOYEE (EMPLOYEE_NAME, AGE) VALUES (?, ?)", data)

conn.commit()

cur.execute("SELECT * FROM EMPLOYEE")
rows = cur.fetchall()
print(rows)

cur.execute("UPDATE EMPLOYEE SET AGE=? WHERE EMPLOYEE_NAME=?", (26, 'Charlie'))
conn.commit()

cur.execute("DELETE FROM EMPLOYEE WHERE EMPLOYEE_NAME=?", ('Bob',))
conn.commit()

# import pandas as pd
# df = pd.read_sql_query("SELECT * FROM EMPLOYEE", conn)
# print(df)
