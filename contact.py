import datetime
import os
import sqlite3
import re

choose_filename = 'task.db'
# choose_to_view_contacts_in_table = True


def get_menu_choice():
    print("1. Add new contact")
    print("2. Update contact")
    print("3. Delete contact")
    print("4. Display all the contacts that have duplicated consecutive characters in name")
    print("5. Exit")
    return input("Please enter your choice (1-5): ")


class Contact:

    # The initialisation method for this class.
    def __init__(self, filename):
        self.filename = filename
        self.db = sqlite3.connect(self.filename)
        self.connect()
        self.view_contact()

    def connect(self):
        self.db = sqlite3.connect(self.filename)
        need_create = not os.path.exists(self.filename)
        if need_create:
            cursor = self.db.cursor()
            cursor.execute("CREATE TABLE contact ("
                           "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
                           "first_name TEXT NOT NULL,"
                           "last_name TEXT NOT NULL,"
                           "address TEXT NOT NULL,"
                           "email TEXT NOT NULL,"
                           "phone TEXT NOT NULL,"
                           "created_at DATETIME )")
            self.db.commit()
            cursor.close()

    def fetch_records(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM contact')
        self.db.commit()
        records = cursor.fetchall()
        return records

    def add_contact_to_db(self, contact_list):
        cursor = self.db.cursor()
        cursor.executemany( "INSERT INTO contact ("
                            "first_name, last_name, address, email, phone, created_at)"
                            " VALUES (?, ?, ?, ?, ?, ?)", contact_list)
        self.db.commit()
        cursor.close()
        print("New address has been created successfully.")
        print()

    def update_contact(self, contact_list):
        cursor = self.db.cursor()
        cursor.executemany(
            """UPDATE contact SET first_name = ?, last_name = ?, address = ?, email = ?, phone = ? WHERE id = ? """,
            contact_list)
        self.db.commit()
        cursor.close()
        print("Address has been updated successfully.")
        print()

    def delete_contact(self, contact_list):
        cursor = self.db.cursor()
        cursor.executemany(
            "DELETE FROM contact WHERE id = ? ",
            contact_list)
        self.db.commit()
        cursor.close()
        print("Address has been deleted successfully.")
        print()

    def view_contact(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM contact ORDER  BY created_at')
        self.db.commit()
        records = cursor.fetchall()

        template = "| {:>4} | {:>15} | {:>15} | {:>20} | {:>20} | {:>15} | {:>30} |"
        print(template.format("ID", "First Name", "Last Name", "Address", "Email", "Phone", "Created at"))
        for item in records:
            print(template.format(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
        cursor.close()

    def find_duplicated_characters_name(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT first_name, last_name FROM contact')
        self.db.commit()
        records = cursor.fetchall()
        for item in records:
            name = item[0] + " " + item[1]
            if re.findall(r'(\w)\1', name):
                print(name)
                print()
        cursor.close()


contacts_creation = Contact(choose_filename)

choice = get_menu_choice()
while choice != "5":

    if choice == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        address = input("Enter address: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        created_at = datetime.datetime.now()
        contact = [(first_name, last_name, address, email, phone, created_at)]
        contacts_creation.add_contact_to_db(contact)
        contacts_creation.view_contact()

    elif choice == "2":
        id = input("Enter id: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        address = input("Enter address: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        contact = [(first_name, last_name, address, email, phone, id)]
        contacts_creation.update_contact(contact)
        contacts_creation.view_contact()

    elif choice == "3":
        id = input("Enter id: ")
        contact = [(id)]
        contacts_creation.delete_contact(contact)
        contacts_creation.view_contact()

    elif choice == "4":
        contacts_creation.find_duplicated_characters_name()

    choice = get_menu_choice()


