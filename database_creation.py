# Import the database library
import sqlite3


# Procedure to create the database
def create():
    # Connect to the database, if not found create it and connect
    connection = sqlite3.connect('login_details.db')
    # Add a table LoginDetails with necessary columns
    connection.execute('''CREATE TABLE LoginDetails (id integer primary key, username text, password text,
                                                      teacher integer, admin integer, sprogress integer, 
                                                      gprogress integer, ascore integer)''')
    # Save all changes
    connection.commit()

# Temporary Procedure to add test user
def add():
    # Connect to the database
    connection = sqlite3.connect('login_details.db')
    # Set the username
    user = "Ethan"
    # Set the password
    password = "Champion"
    # Insert the user into the database
    connection.execute("INSERT INTO LoginDetails(username,password,teacher,admin,sprogress,gprogress,"
                                   "ascore) VALUES (?,?,0,0,10,12,14)", (user,password,))
    # For item in database
    for row in connection.execute("SELECT * FROM LoginDetails"):
        # Output the record
        print(row)
    # Do not save changes to database
