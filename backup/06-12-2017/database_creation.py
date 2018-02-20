# Impor the database library
import sqlite3

# Procedure to create the database
def create():
    # Connect to the database, if not found create it and connect
    connection = sqlite3.connect('login_details.db')
    # Add a table LoginDetails with necessary columns
    connection.execute('''CREATE TABLE LoginDetails (id integer primary key, username text, password text, teacher integer, admin integer, sprogress integer, gprogress integer, ascore integer)''')
    # Save all changes
    connection.commit()
