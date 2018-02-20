# Import the database library
import sqlite3
# From the hashing library import the SHA512 algorithm
from hashlib import sha512


# Procedure to create a new teacher
def create_teacher(teacher_name, teacher_password):
    # Set up a connection to the login details database
    connection = sqlite3.connect('login_details.db')
    # Add to the database the name and password as well as setting it to teacher
    connection.execute('''INSERT INTO LoginDetails(username,password,teacher,admin,sprogress,gprogress,
                       ascore)'''
                       "VALUES (?,?,1,0,0,0,0)",
                       (teacher_name, teacher_password,))
    # Save all changes
    connection.commit()


# Procedure to create a new admin
def create_admin(admin_name, admin_password):
    # Set up a connection to the login details database
    connection = sqlite3.connect('login_details.db')
    # Add to the database the name and password as well as setting it to admin
    connection.execute('''INSERT INTO LoginDetails(username,password,teacher,admin,sprogress,gprogress,
                       ascore)'''
                       "VALUES (?,?,0,1,0,0,0)",
                       (admin_name, admin_password,))
    # Save all changes
    connection.commit()


# Ask if user is a teacher or admin
option = input("Do you want a teacher account (1) or an admin account (2): ")
# Ask for username
name = input("Username: ")
# Ask for password
password = input("Password: ")
# Set the hashing algorithm to SHA512
hash_new = sha512()
# Hash the password and turn it into byte format
hash_new.update(password.encode('utf-8'))
# Set the password to the hex of the hash
password = hash_new.hexdigest()

# If the user is a teacher
if option == "1":
    # Create a teacher
    create_teacher(name, password)
    # Output they have been added
    print("Added, return to main program.")
# If the user is an admin
elif option == "2":
    # Create an admin
    create_admin(name, password)
    # Output they have been added
    print("Added, return to main program.")
# If the user is neither a teacher nor an admin
else:
    # Output they have done something wrong
    print("Incorrect option, please try again.")
