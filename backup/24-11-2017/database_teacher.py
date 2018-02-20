import sqlite3

def create_teacher(teacher_name,teacher_password):
    connection = sqlite3.connect('login_details.db')
    connection.execute('''INSERT INTO LoginDetails(username,password,teacher,admin,sprogress,gprogress,
                       ascore)'''
                       "VALUES (?,?,1,0,0,0,0)",
                       (teacher_name,teacher_password,))
    connection.commit()


def create_admin(admin_name,admin_password):
    connection = sqlite3.connect('login_details.db')
    connection.execute('''INSERT INTO LoginDetails(username,password,teacher,admin,sprogress,gprogress,
                       ascore)'''
                       "VALUES (?,?,0,1,0,0,0)",
                       (admin_name,admin_password,))
    connection.commit()


option = input("Do you want a teacher account (1) or an admin account (2): ")
name = input("Username: ")
password = input("Password: ")

if option == "1":
    create_teacher(name,password)
    print("Added, return to main program.")
elif option == "2":
    create_admin(name,password)
    print("Added, return to main program.")
else:
    print("Incorrect option, please try again.")
