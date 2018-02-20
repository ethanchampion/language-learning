# Import the database library
import sqlite3

# Procedure to create the database
def create1():
    # Create a connection, if file not found then it creates it
    connection = sqlite3.connect('question_sets.db')
    # Create a table with all the necessary columns
    connection.execute('''CREATE TABLE QuestionSets(id integer primary key, name text, spanish bool, german bool)''')
    # Save all changes
    connection.commit()
