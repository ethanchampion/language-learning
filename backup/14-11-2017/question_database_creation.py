import sqlite3
def create1():
    connection = sqlite3.connect('question_sets.db')
    connection.execute('''CREATE TABLE LoginDetails (id integer primary key, name text, words text)''')
    connection.commit()
