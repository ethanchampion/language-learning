import sqlite3
def create():
    connection = sqlite3.connect('login_details.db')
    connection.execute('''CREATE TABLE LoginDetails (id integer primary key, username text, password text, teacher integer, admin integer, sprogress integer, gprogress integer, ascore integer)''')
    connection.commit()
