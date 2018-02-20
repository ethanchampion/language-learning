import sqlite3
def create1():
    connection = sqlite3.connect('question_sets.db')
    connection.execute('''CREATE TABLE QuestionSets (id integer primary key, name text, words text)''')
    connection.commit()

##def add():
##    name,words = input("Name"),input("Words")
##    connection.execute("INSERT INTO QuestionSets(name,words) VALUES (?,?)",(name,words,))
##                
##    
##connection = sqlite3.connect('question_sets.db')
##add()
