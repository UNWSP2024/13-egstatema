# Eliya Statema
# 5/1/25
# Create Phone Book Database

import sqlite3

def main():
    # Connect to the database
    conn = sqlite3.connect('phonebook.db')
    # Get a database cursor
    cur = conn.cursor()
    # Add the Cities table
    add_entries_table(cur)
    # Add rows to the Cities table
    add_data(cur)
    # Commit changes
    conn.commit()
    # Close the connection
    conn.close()

# Adds the Entries table to the database
def add_entries_table(cur):
    # If the table already exists, drop it.
    cur.execute("DROP TABLE IF EXISTS Entries")
    # Create table
    cur.execute('''CREATE TABLE Entries (ID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT,
                                        Number TEXT)''')

# Adds rows to Entries table
def add_data(cur):
     data_pop = [(1, 'Anna Brown', '123-456-7899'),
                 (2, 'Sam Smith', '555-666-7777'),
                 (3, 'Bob Anderson', '380-8000-9999')]

     for row in data_pop:
        cur.execute('''INSERT INTO Entries (ID, Name, Number)
                        VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

if __name__ == "__main__":
    main()