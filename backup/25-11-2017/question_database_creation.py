import sqlite3
import random
def create1():
    import sqlite3
    connection = sqlite3.connect('question_sets.db')
    connection.execute('''CREATE TABLE QuestionSets(id integer primary key, name text, spanish bool, german bool)''')
    connection.commit()

def add():
    connection = sqlite3.connect('question_sets.db')
    name = input("Name: ")
    s_bool = int(input("Spanish: "))
    g_bool = int(input("German: "))
    connection.execute("INSERT INTO QuestionSets(name,spanish,german) VALUES (?,?,?)",(name,s_bool,g_bool))
    connection.commit()
    for item in connection.execute("SELECT * FROM QuestionSets"):
        print(item)

def remove():
    connection = sqlite3.connect('question_sets.db')
    pid = input("ID: ")
    connection.execute("DELETE FROM QuestionSets WHERE id = (?)",(pid,))
    connection.commit()
