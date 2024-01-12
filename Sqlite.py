import sqlite3

# Connection to SQLite
connection = sqlite3.connect('student.db')

# Create a cursor object to insert records, create a table
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE STUDENT (
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT
);
"""
cursor.execute(table_info)

# Insert records into the table
cursor.execute("INSERT INTO STUDENT VALUES('Anand', 'Data Science', 'A')")
cursor.execute("INSERT INTO STUDENT VALUES('vikash', 'Data Science', 'A')")
cursor.execute("INSERT INTO STUDENT VALUES('bibek', 'Machine Learning', 'A')")
cursor.execute("INSERT INTO STUDENT VALUES('rakesh', 'Data Science', 'B')")
cursor.execute("INSERT INTO STUDENT VALUES('Ram', 'Data Science', 'A')")
cursor.execute("INSERT INTO STUDENT VALUES('Ganesh', 'Data Science', 'C')")
cursor.execute("INSERT INTO STUDENT VALUES('Payal', 'MERN', 'A')")
cursor.execute("INSERT INTO STUDENT VALUES('Achal', 'Data Science', 'B')")

print('The inserted records are:')

# Select and print all records from the STUDENT table
data = cursor.execute('SELECT * FROM STUDENT')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()

# Close the database connection
connection.close()
