# Eliya Statema
# 5/1/25
# Phone Book Database

import sqlite3

MIN = 1
MAX = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
QUIT = 5

def main():
   choice = 0
   while choice != QUIT:
       display_menu()
       choice = get_menu_choice()

       if choice == CREATE:
           create()
       elif choice == READ:
           read()
       elif choice == UPDATE:
           update()
       elif choice == DELETE:
           delete()

def display_menu():
    print('''Actions:
    1. Create a new entry
    2. Read an entry
    3. Update an existing entry
    4. Delete an entry
    5. Exit the program''')

def get_menu_choice():
    choice = int(input("Enter the number of the action you would like to perform: "))
    return choice

def create():
    print("Create New Entry")
    name = input("Name: ")
    number = input("Number: ")
    insert_row(name, number)
    print("This entry has been added.")

def insert_row(name, number):
    connect = sqlite3.connect("phonebook.db")
    cur = connect.cursor()
    cur.execute('''INSERT INTO Entries (Name, Number)
                    VALUES (?, ?)''',
          (name, number))
    connect.commit()
    connect.close()

def read():
    name = input("Enter a name to search for: ")
    num_found = display_entry(name)

def display_entry(name):
    results = []
    connect = sqlite3.connect("phonebook.db")
    cur = connect.cursor()
    cur.execute("SELECT * FROM Entries WHERE lower(Name) == ?", (name.lower(),))
    results = cur.fetchall()
    for row in results:
        print(f"ID: {row[0]:<3} \nName: {row[1]:<15} \nNumber: {row[2]:<6}")
    connect.close()
    return len(results)

def update():
    read()
    select_ID = int(input("Select the ID of the entry you would like to update: "))
    name = input("Updated Name: ")
    number = input("Updated Number: ")
    num_updated = update_row(select_ID, name, number)
    print(f"This entry has been updated.")

def update_row(ID, name, number):
    connect = sqlite3.connect("phonebook.db")
    cur = connect.cursor()
    cur.execute("UPDATE Entries SET Name = ?, Number = ? WHERE ID == ?", (name, number, ID))
    connect.commit()
    num_updated = cur.rowcount
    connect.close()
    return num_updated

def delete():
    read()
    select_ID = int(input("Select the ID of the entry you would like to delete: "))
    sure = input("Are you sure you would like to delete this entry? (y/n) ")
    if sure.lower() == "y":
        entry_delete = delete_row(select_ID)
    print(f"This entry has been deleted.")

def delete_row(ID):
    connect = sqlite3.connect("phonebook.db")
    cur = connect.cursor()
    cur.execute("DELETE FROM Entries WHERE ID == ?", (ID,))
    connect.commit()
    num_deleted = cur.rowcount
    connect.close()
    return num_deleted

if __name__ == '__main__':
    main()