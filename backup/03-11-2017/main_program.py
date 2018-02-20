#####################################
# Memrize Learning Languages System #
# --------------------------------- #
#      By Ethan Champion 13RKS      #
#       Made in Python 3.6.3.       #
#    Variable Style: Underscores    #
#####################################

#############
# Libraries #
#############

from tkinter import *
import sqlite3
import random
import time
import os
import datetime
import sys
from database_creation import create
from backup_database import perform_backup
import subprocess

################
# Login System #
################

def close():
    global HELP_WINDOW_OPEN_BOOL
    HELP_WINDOW_OPEN_BOOL = False
    help_window.geometry("300x600+3000+3000")
    help_button.place(x=405, y=550)


def help_storage():
    global HELP_WINDOW_OPEN_BOOL
    try:
        if HELP_WINDOW_OPEN_BOOL == True:
            help_function()
    except NameError:
        pass


def help_function():
    global HELP_TEXT_LABEL
    global HELP_SECTION_TRACKER
    global HELP_WINDOW_OPEN_BOOL
    HELP_WINDOW_OPEN_BOOL = True
    help_window.geometry("300x600+803+2")
    close_button = Button(help_window, text="CLOSE", command=close, bg="white", width="6", height="1")
    close_button.config(font=("Lucida Sans", 8, "bold"))
    close_button.place(x=130, y=550)
    try:
        HELP_TEXT_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    help_label.place(x=47, y=10)
    help_button.place(x=3000, y=3000)
    if HELP_SECTION_TRACKER == 0:
        HELP_TEXT_LABEL = Label(help_window,text='''You are currently in the main menu. In
this section you have two choices. You
can either login if you already have an
account, or you can register by clicking
the corresponding button. Please note
you will have to remember your
password. Once you have done this you
will be able to login. At the bottom you
should also see buttons to quit the
application, go back if you need to, and
on this window close the help window.''',
                                font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 1:
        HELP_TEXT_LABEL = Label(help_window,text=
'''You are currently in the register section.
In this section you have two boxes to
fill. Your username that will be displayed
on leader boards, and password which
you will have to remember. When you
have filled these in simply press SUBMIT
and you will be taken to the login
section and your account
has been made.'''
                                ,font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 2:
        HELP_TEXT_LABEL = Label(help_window,text=
'''You are currently in the login section.
In this section you have to enter your
username you originally chose and the
password as well. If you forget your
password ask your teacher to reset it.
Once you have filled it in click SUBMIT or
press enter and you will sign in.''',
                                font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 3:
        Help_Text_Label = Label(help_window,text=
'''You have logged in successfully.
Now in this section you have to choose
what language you are going to be
learning or practicising. You will now
also be able to see a leader board
button at the bottom which displays
the top 5 learners of each class.''',
                                font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        Help_Text_Label.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 4:
        HELP_TEXT_LABEL = Label(help_window,text=
'''You now have a choice of which module
of your language you will choose. The
program provides three basic ones or
you can choose from the drop down
menu modules that your teacher has
added. Simply click the rectangle and it
will provide you which the options.''',
                                font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 5:
        HELP_TEXT_LABEL = Label(help_window,text=
'''Now that you have chosen a module you
are now presented with two options.
The first mode is learn mode where you
can spend as long as you want to
practice the words. You will be told
where you went wrong so that you can
improve. The other mode is arcade mode
which has a 60 second timer and you do
not receive any feedback to make it as
quick as possible.''',
                                font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)


def initial_register():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 1
    help_storage()
    back_welcome_button.place(x=299, y=550)
    new_username_field.place(x=237, y=220)
    new_password_field.place(x=430, y=220)
    username_password_label.place(x=200, y=150)
    submit_register_button.place(x=365, y=220)
    username_taken_label.place(x=3000, y=3000)
    register_button.place(x=3000, y=3000)
    login_button.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    main_gui.bind('<Return>', submit_register_process)


def initial_login():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 2
    help_storage()
    initial_choice_label.place(x=1000, y=10050)
    back_welcome_button.place(x=299, y=550)
    register_button.place(x=3000, y=3000)
    login_button.place(x=3000, y=3000)
    login_username_field.place(x=237, y=220)
    login_password_field.place(x=430, y=220)
    username_password_label.place(x=200, y=150)
    submit_login_button.place(x=365, y=220)
    login_error_label.place(x=3000, y=3000)
    main_gui.bind('<Return>', submit_login_process)


def submit_register_process(key):
    submit_register()


def submit_register():
    if new_username_field.get() and new_password_field.get():
        registered_label.place(x=3000, y=3000)
        username_taken_label.place(x=3000, y=3000)
        username_length_label.place(x=3000, y=3000)
        password_error_label.place(x=3000, y=3000)
        new_username = new_username_field.get()
        new_password = new_password_field.get()
        new_username_field.delete(0, END)
        new_password_field.delete(0, END)
        temp = [""]
        for row in connection.execute("SELECT * FROM LoginDetails WHERE username = ?", (new_username,)):
            temp = row
        if temp[0] == "":
            if len(new_username) < 3 or len(new_username) > 10:
                username_length_label.place(x=100, y=265)
            elif len(new_password) < 5:
                password_error_label.place(x=130, y=265)
            elif new_password == new_password.lower():
                password_error_label.place(x=130, y=265)
            else:
                registered_label.place(x=190, y=265)
                connection.execute('''INSERT INTO LoginDetails(username,password,teacher,admin,sprogress,gprogress,
                                   ascore)'''
                                   "VALUES (?,?,0,0,0,0,0)",
                                   (new_username, new_password,))
                connection.commit()               
        else:
            username_taken_label.place(x=190, y=265)


def submit_login_process(key):
    submit_login()


def submit_login():
    global LOGIN_USERNAME
    global LOGIN_PASSWORD
    global SPROGRESS
    global GPROGRESS
    if login_username_field.get() and login_password_field.get():
        LOGIN_USERNAME = login_username_field.get()
        LOGIN_PASSWORD = login_password_field.get()
        login_password_field.delete(0, END)
        login_username_field.delete(0, END)
        temp = ()
        for row in connection.execute("SELECT * FROM LoginDetails WHERE username = ? AND password = ?",
                                      (LOGIN_USERNAME, LOGIN_PASSWORD)):
            temp += row
        temp_check = temp
        temp = str(temp)
        if temp == "()":
            logging_in_label.place(x=3000, y=3000)
            login_error_label.place(x=190, y=265)
        elif temp_check[3] == 1:
            teacher_system()
        elif temp_check[4] == 1:
            admin_system()
        else:
            SPROGRESS = ""
            for row in connection.execute("SELECT sprogress FROM LoginDetails WHERE username = ? AND password = ?",
                                          (LOGIN_USERNAME, LOGIN_PASSWORD)):
                SPROGRESS = row
            GPROGRESS = ""
            for row in connection.execute("SELECT gprogress FROM LoginDetails WHERE username = ? AND password = ?",
                                          (LOGIN_USERNAME, LOGIN_PASSWORD)):
                GPROGRESS = row
            SPROGRESS = SPROGRESS[0]
            GPROGRESS = GPROGRESS[0]
            login_error_label.place(x=3000, y=3000)
            logging_in_label.place(x=190, y=265)
            login_system()


def main_window():
    global VIEW_STUDENT_PROGRESS_LABEL
    global HELP_SECTION_TRACKER
    global DONE_BACKUP_LABEL
    global RESET_PASSWORD_LABEL
    global DELETE_USER_LABEL
    global RESTORE_BACKUP_LABEL
    HELP_SECTION_TRACKER = 0
    help_storage()
    global ARCADE_MODE_BOOL
    ARCADE_MODE_BOOL = False
    global SPANISH_MODE_BOOL
    SPANISH_MODE_BOOL = False
    register_button.place(x=300, y=220)
    login_button.place(x=410, y=220)
    slogo_label.place(x=205, y=10)
    initial_choice_label.place(x=300, y=150)
    back_welcome_button.place(x=3000, y=3000)
    new_username_field.place(x=3000, y=3000)
    new_password_field.place(x=3000, y=3000)
    login_username_field.place(x=3000, y=3000)
    login_password_field.place(x=3000, y=3000)
    username_password_label.place(x=3000, y=3000)
    submit_register_button.place(x=3000, y=3000)
    submit_login_button.place(x=3000, y=3000)
    registered_label.place(x=3000, y=3000)
    logging_in_label.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    try:
        VIEW_STUDENT_PROGRESS_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        DONE_BACKUP_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        RESET_PASSWORD_LABEL.place(x=3000, y=3000)
        DONE_RESET_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        DELETE_USER_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        RESTORE_BACKUP_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    login_error_label.place(x=3000, y=3000)
    logout_button.place(x=3000, y=3000)
    spanish_learn_button.place(x=3000, y=3000)
    german_learn_button.place(x=3000, y=3000)
    back_learn_button.place(x=3000, y=3000)
    username_length_label.place(x=3000, y=3000)
    teacher_section_label.place(x=3000, y=3000)
    password_error_label.place(x=3000, y=3000)
    spanish_zone_label.place(x=3000, y=3000)
    spanish_arcade_button.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)
    welcome_back_label.place(x=3000, y=3000)
    leader_board_button.place(x=3000, y=3000)
    spanish_learn_entry.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    german_zone_label.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)
    german_arcade_start_button.place(x=3000, y=3000)
    spanish_arcade_start_button.place(x=3000, y=3000)
    spanish_question_menu.place(x=3000, y=3000)
    spanish_basics1_button.place(x=3000, y=3000)
    spanish_basics2_button.place(x=3000, y=3000)
    spanish_basics3_button.place(x=3000, y=3000)
    german_question_menu.place(x=3000, y=3000)
    german_basics1_button.place(x=3000, y=3000)
    german_basics2_button.place(x=3000, y=3000)
    german_basics3_button.place(x=3000, y=3000)
    view_student_progress_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    view_student_progress_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    back_teacher_button.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    id_field.place(x=3000, y=3000)
    reset_password_field.place(x=3000, y=3000)
    reset_password_button.place(x=3000, y=3000)
    

################
# Login System #
################

def login_system():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 3
    help_storage()
    submit_login_button.place(x=3000, y=3000)
    back_welcome_button.place(x=3000, y=3000)
    login_username_field.place(x=3000, y=3000)
    login_password_field.place(x=3000, y=3000)
    spanish_question_menu.place(x=3000, y=3000)
    spanish_basics1_button.place(x=3000, y=3000)
    spanish_basics2_button.place(x=3000, y=3000)
    spanish_basics3_button.place(x=3000, y=3000)
    german_question_menu.place(x=3000, y=3000)
    german_basics1_button.place(x=3000, y=3000)
    german_basics2_button.place(x=3000, y=3000)
    german_basics3_button.place(x=3000, y=3000)
    username_password_label.place(x=3000, y=3000)
    slogo_label.place(x=3000, y=3000)
    logging_in_label.place(x=3000, y=3000)
    welcome_back_label.place(x=205, y=10)
    spanish_learn_button.place(x=300, y=200)
    german_learn_button.place(x=410, y=200)
    leader_board_button.place(x=460, y=550)
    logout_button.place(x=225, y=550)


def spanish_basics1_module():
    global SPANISH_MODULE
    global MODULE_COUNT_TRACKER
    SPANISH_MODULE = "spanish_basics1.txt"
    MODULE_COUNT_TRACKER = 0
    with open(SPANISH_MODULE,'r') as f:
        contents = f.read()
        contents = contents.split(",")
        for item in contents:
            MODULE_COUNT_TRACKER += 1
    spanish_question_menu.place(x=3000, y=3000)
    spanish_basics1_button.place(x=3000, y=3000)
    spanish_basics2_button.place(x=3000, y=3000)
    spanish_basics3_button.place(x=3000, y=3000)
    spanish_learn()


def spanish_basics2_module():
    global SPANISH_MODULE
    global MODULE_COUNT_TRACKER
    SPANISH_MODULE = "spanish_basics2.txt"
    MODULE_COUNT_TRACKER = 0
    with open(SPANISH_MODULE,'r') as f:
        contents = f.read()
        contents = contents.split(",")
        for item in contents:
            MODULE_COUNT_TRACKER += 1
    spanish_question_menu.place(x=3000, y=3000)
    spanish_basics1_button.place(x=3000, y=3000)
    spanish_basics2_button.place(x=3000, y=3000)
    spanish_learn()
    spanish_basics3_button.place(x=3000, y=3000)


def spanish_basics3_module():
    global SPANISH_MODULE
    global MODULE_COUNT_TRACKER
    SPANISH_MODULE = "spanish_basics3.txt"
    MODULE_COUNT_TRACKER = 0
    with open(SPANISH_MODULE,'r') as f:
        contents = f.read()
        contents = contents.split(",")
        for item in contents:
            MODULE_COUNT_TRACKER += 1
    spanish_question_menu.place(x=3000, y=3000)
    spanish_basics1_button.place(x=3000, y=3000)
    spanish_basics2_button.place(x=3000, y=3000)
    spanish_basics3_button.place(x=3000, y=3000)
    spanish_learn()


def german_basics1_module():
    global GERMAN_MODULE
    global MODULE_COUNT_TRACKER
    GERMAN_MODULE = "german_basics1.txt"
    MODULE_COUNT_TRACKER = 0
    with open(GERMAN_MODULE,'r') as f:
        contents = f.read()
        contents = contents.split(",")
        for item in contents:
            MODULE_COUNT_TRACKER += 1
    german_question_menu.place(x=3000, y=3000)
    german_basics1_button.place(x=3000, y=3000)
    german_basics2_button.place(x=3000, y=3000)
    german_basics3_button.place(x=3000, y=3000)
    german_learn()


def german_basics2_module():
    global GERMAN_MODULE
    global MODULE_COUNT_TRACKER
    GERMAN_MODULE = "german_basics2.txt"
    MODULE_COUNT_TRACKER = 0
    with open(GERMAN_MODULE,'r') as f:
        contents = f.read()
        contents = contents.split(",")
        for item in contents:
            MODULE_COUNT_TRACKER += 1
    german_question_menu.place(x=3000, y=3000)
    german_basics1_button.place(x=3000, y=3000)
    german_basics2_button.place(x=3000, y=3000)
    german_learn()
    german_basics3_button.place(x=3000, y=3000)


def german_basics3_module():
    global GERMAN_MODULE
    global MODULE_COUNT_TRACKER
    GERMAN_MODULE = "german_basics3.txt"
    MODULE_COUNT_TRACKER = 0
    with open(GERMAN_MODULE,'r') as f:
        contents = f.read()
        contents = contents.split(",")
        for item in contents:
            MODULE_COUNT_TRACKER += 1
    german_question_menu.place(x=3000, y=3000)
    german_basics1_button.place(x=3000, y=3000)
    german_basics2_button.place(x=3000, y=3000)
    german_basics3_button.place(x=3000, y=3000)
    german_learn()


def spanish_modules():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 4
    help_storage()
    welcome_back_label.place(x=3000, y=3000)
    spanish_learn_button.place(x=3000, y=3000)
    german_learn_button.place(x=3000, y=3000)
    back_learn_button.place(x=299, y=550)
    spanish_zone_label.place(x=205, y=10)
    spanish_basics1_button.place(x=243, y=200)
    spanish_basics2_button.place(x=360,y=200)
    spanish_basics3_button.place(x=477, y=200)
    spanish_question_menu.place(x=360,y=300)


def ó():
    spanish_learn_entry.insert(END,"ó")


def í():
    spanish_learn_entry.insert(END,"í")


def é():
    spanish_learn_entry.insert(END,"é")


def á():
    spanish_learn_entry.insert(END,"á")


def ú():
    spanish_learn_entry.insert(END,"ú")


def ñ():
    spanish_learn_entry.insert(END,"ñ")


def ß():
    german_learn_entry.insert(END,"ß")


def ü():
    german_learn_entry.insert(END,"ü")


def ä():
    german_learn_entry.insert(END,"ä")


def upside_down_question_mark():
    spanish_learn_entry.insert(END,"¿")
    

def spanish_learn():
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global SCORE_TRACKER
    global ARCADE_SELECTED
    global HELP_SECTION_TRACKER
    global SPANISH_LEARN_COUNT
    global SPANISH_LEARN_SCORE
    global SPANISH_SCORE_COUNT
    ARCADE_MODE_BOOL = False
    SPANISH_MODE_BOOL = True
    SCORE_TRACKER = 0
    ARCADE_SELECTED = 0 
    HELP_SECTION_TRACKER = 5
    help_storage()
    SPANISH_SCORE_COUNT = 0
    SPANISH_LEARN_COUNT = 1
    SPANISH_LEARN_SCORE = 0
    spanish_arcade_button.place(x=410, y=200)
    spanish_learn_mode_button.place(x=293, y=200)


def german_modules():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 4
    help_storage()
    welcome_back_label.place(x=3000, y=3000)
    spanish_learn_button.place(x=3000, y=3000)
    german_learn_button.place(x=3000, y=3000)
    back_learn_button.place(x=299, y=550)
    german_zone_label.place(x=205, y=10)
    german_basics1_button.place(x=243, y=200)
    german_basics2_button.place(x=360,y=200)
    german_basics3_button.place(x=477, y=200)
    german_question_menu.place(x=360,y=300)


def german_learn():
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global GERMAN_SCORE_COUNT
    global HELP_SECTION_TRACKER
    global ARCADE_SELECTED
    global GERMAN_LEARN_SCORE
    global GERMAN_LEARN_COUNT
    ARCADE_MODE_BOOL = False
    SPANISH_MODE_BOOL = False
    ARCADE_SELECTED = 0
    HELP_SECTION_TRACKER = 5
    help_storage()
    GERMAN_SCORE_COUNT = 0
    GERMAN_LEARN_COUNT = 1
    GERMAN_LEARN_SCORE = 0
    german_arcade_button.place(x=410, y=200)
    german_learn_mode_button.place(x=293, y=200)


def spanish_redirect_mode(key):
    spanish_learn_mode()


def spanish_learn_mode():
    global HELP_SECTION_TRACKER
    global SPANISH_INCORRECT_ANSWER
    global SPANISH_MODULE
    global SPANISH_LEARN_QUESTION
    global SPANISH_LEARN_QUESTION_NEW
    global SPANISH_LEARN_ANSWER
    global MODULE_COUNT_TRACKER
    HELP_SECTION_TRACKER = 5
    help_storage()
    try:
        SPANISH_INCORRECT_ANSWER.place(x=3000, y=3000)
    except NameError:
        pass
    spanish_continue_button.place(x=3000, y=3000)
    logout_button.place(x=3000, y=3000)
    spanish_zone_label.place(x=3000, y=3000)
    spanish_arcade_button.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)
    ó_button.place(x=320, y=300)
    ñ_button.place(x=350, y=300)
    upside_down_question_mark_button.place(x=380, y=300)
    é_button.place(x=410, y=300)
    í_button.place(x=440, y=300)
    á_button.place(x=470, y=300)
    ú_button.place(x=290, y=300)
    spanish_submit_button.place(x=350, y=400)
    question_count = "Question Number " + str(SPANISH_LEARN_COUNT) + "."
    current_score = "Your current score is: " + str(SPANISH_LEARN_SCORE)
    with open(SPANISH_MODULE,'r') as f:
        contents = f.read()
        contents = contents.split(",")
    random_number = random.randint(0,MODULE_COUNT_TRACKER)
    try:
        SPANISH_LEARN_QUESTION = contents[random_number]
        if random_number % 2 == 0:
            SPANISH_LEARN_ANSWER = contents[random_number+1]
            even_question = question_count + "\n\n" + current_score + "\n\n\n\n" + SPANISH_LEARN_QUESTION
            even_question += "\n\nType the Spanish for the English above and press Enter:"
            SPANISH_LEARN_QUESTION_NEW = Label(main_gui, text = even_question, font=("Lucida Sans", 10, "bold"),
                                               bd = 3, bg = "orange", fg = "white")
            SPANISH_LEARN_QUESTION_NEW.place(x=200, y=100)
        else:
            SPANISH_LEARN_ANSWER = contents[random_number-1]
            odd_question = question_count + "\n\n" + current_score + "\n\n\n\n" + SPANISH_LEARN_QUESTION
            odd_question += "\n\nType the English for the Spanish above and press Enter:"
            SPANISH_LEARN_QUESTION_NEW = Label(main_gui, text = odd_question, font=("Lucida Sans", 10, "bold"),
                                               bd = 3, bg = "orange", fg = "white")
            SPANISH_LEARN_QUESTION_NEW.place(x=200, y=100)
        spanish_learn_entry.place(x=275, y=250)
        main_gui.bind('<Return>',spanish_learn_process_bypass)
    except IndexError:
        try:
            SPANISH_LEARN_QUESTION_NEW.place(x=3000, y=3000)
        except NameError:
            pass
        pass
        spanish_learn_mode()


def spanish_learn_process_bypass(key):
    spanish_learn_process()


def spanish_learn_process():
    global SPANISH_LEARN_SCORE
    global SCORE_TRACKER
    global SPANISH_LEARN_COUNT
    global SPANISH_LEARN_QUESTION
    global SPANISH_LEARN_ANSWER
    global ARCADE_SELECTED
    global STREAK_LABEL
    global SPANISH_INCORRECT_ANSWER
    if spanish_learn_entry.get():
        ó_button.place(x=3000, y=3000)
        ñ_button.place(x=3000, y=3000)
        upside_down_question_mark_button.place(x=3000, y=3000)
        é_button.place(x=3000, y=3000)
        í_button.place(x=3000, y=3000)
        á_button.place(x=3000, y=3000)
        ú_button.place(x=3000, y=3000)
        spanish_submit_button.place(x=3000, y=3000)
        try:
            STREAK_LABEL.place(x=3000, y=3000)
        except NameError:
            pass
        SPANISH_LEARN_QUESTION_NEW.place(x=3000, y=3000)
        their_answer = spanish_learn_entry.get()
        spanish_learn_entry.delete(0, END)
        SPANISH_LEARN_COUNT += 1
        if their_answer.lower() == SPANISH_LEARN_ANSWER.lower():
            SCORE_TRACKER += 1
            if SCORE_TRACKER >= 3 and SCORE_TRACKER < 10:
                STREAK_LABEL = Label(main_gui, text = "STREAK!\n" + str(SCORE_TRACKER) + "\nDouble points!",
                                     font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
                STREAK_LABEL.place(x=330, y=450)
                SPANISH_LEARN_SCORE += 2
            elif SCORE_TRACKER >= 10:
                STREAK_LABEL = Label(main_gui, text = "STREAK!\n" + str(SCORE_TRACKER) + "\nTriple points!",
                                     font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
                STREAK_LABEL.place(x=330, y=450)
                SPANISH_LEARN_SCORE += 3
            else:
                SPANISH_LEARN_SCORE += 1
            connection_cursor.execute("SELECT sprogress FROM LoginDetails WHERE username=?",(LOGIN_USERNAME,))
            past_score = connection_cursor.fetchone()
            new_score = past_score[0] + 1
            connection.execute("UPDATE LoginDetails SET sprogress = ? WHERE username = ?",
                               (new_score,LOGIN_USERNAME,))
            connection.commit()
            leader_board_refresh()
            spanish_learn_mode()
        else:
            SCORE_TRACKER = 0
            if ARCADE_SELECTED == 1:
                spanish_learn_mode()
            else:
                spanish_learn_entry.place(x=3000, y=3000)
                SPANISH_INCORRECT_ANSWER = Label(main_gui, text = "Incorrect answer.\n\nThe question was:\n" +
                                                 SPANISH_LEARN_QUESTION + "\n\nYou typed in:\n" + their_answer +
                                                 "\n\nThe correct answer was:\n" + SPANISH_LEARN_ANSWER +
                                                 "\n\nPress continue to carry on.", font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
                SPANISH_INCORRECT_ANSWER.place(x=300, y=100)
                spanish_continue_button.place(x=365, y=320)
                main_gui.bind('<Return>',spanish_redirect_mode)
    

def german_redirect_mode(key):
    german_learn_mode()


def german_learn_mode():
    global HELP_SECTION_TRACKER
    global GERMAN_INCORRECT_ANSWER
    global GERMAN_MODULE
    global GERMAN_LEARN_QUESTION
    global GERMAN_LEARN_ANSWER
    global GERMAN_LEARN_QUESTION_NEW
    global MODULE_COUNT_TRACKER
    ä_button.place(x=380, y=300)
    ß_button.place(x=350, y=300)
    ü_button.place(x=410, y=300)
    german_submit_button.place(x=350, y=400)
    HELP_SECTION_TRACKER = 5
    help_storage()
    try:
        GERMAN_INCORRECT_ANSWER.place(x=3000, y=3000)
    except NameError:
        pass
    german_continue_button.place(x=3000, y=3000)
    logout_button.place(x=3000, y=3000)
    german_zone_label.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)
    question_count = "Question Number " + str(GERMAN_LEARN_COUNT) + "."
    current_score = "Your current score is: " + str(GERMAN_LEARN_SCORE)
    with open(GERMAN_MODULE,'r') as f:
        contents = f.read()
        contents = contents.split(",")
    random_number = random.randint(0,MODULE_COUNT_TRACKER)
    try:
        GERMAN_LEARN_QUESTION = contents[random_number]
        if random_number % 2 == 0:
            GERMAN_LEARN_ANSWER = contents[random_number+1]
            even_question = question_count + "\n\n" + current_score + "\n\n\n\n" + GERMAN_LEARN_QUESTION
            even_question += "\n\nType the English for the German above and press Enter:"
            GERMAN_LEARN_QUESTION_NEW = Label(main_gui, text = even_question, font=("Lucida Sans", 10, "bold"),
                                              bd = 3, bg = "orange", fg = "white")
            GERMAN_LEARN_QUESTION_NEW.place(x=200, y=100)
        else:
            GERMAN_LEARN_ANSWER = contents[random_number-1]
            odd_question = question_count + "\n\n" + current_score + "\n\n\n\n" + GERMAN_LEARN_QUESTION
            odd_question += "\n\nType the German for the English above and press Enter:"
            GERMAN_LEARN_QUESTION_NEW = Label(main_gui, text = odd_question, font=("Lucida Sans", 10, "bold"),
                                              bd = 3, bg = "orange", fg = "white")
            GERMAN_LEARN_QUESTION_NEW.place(x=200, y=100)
        german_learn_entry.place(x=275, y=250)
        main_gui.bind('<Return>',german_learn_process)
    except IndexError:
        try:
            GERMAN_LEARN_QUESTION.place(x=3000, y=3000)
        except NameError:
            pass
        pass
        german_learn_mode()


def german_learn_process(key):
    global GERMAN_LEARN_SCORE
    global GERMAN_LEARN_COUNT
    global SCORE_TRACKER
    global STREAK_LABEL
    global ARCADE_SELECTED
    global GERMAN_INCORRECT_ANSWER
    global GERMAN_LEARN_QUESTION
    global ARCADE_MODE_BOOL
    ß_button.place(x=3000, y=3000)
    ü_button.place(x=3000, y=3000)
    german_submit_button.place(x=3000, y=3000)
    ä_button.place(x=3000, y=3000)
    if german_learn_entry.get():
        try:
            STREAK_LABEL.place(x=3000, y=3000)
        except NameError:
            pass
        GERMAN_LEARN_QUESTION_NEW.place(x=3000, y=3000)
        their_answer = german_learn_entry.get()
        german_learn_entry.delete(0, END)
        GERMAN_LEARN_COUNT += 1
        if their_answer.lower() == GERMAN_LEARN_ANSWER.lower():
            SCORE_TRACKER += 1
            if SCORE_TRACKER >= 3 and SCORE_TRACKER < 10:
                STREAK_LABEL = Label(main_gui, text = "STREAK!\n" + str(SCORE_TRACKER) + "\nDouble points!",
                                     font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
                STREAK_LABEL.place(x=330, y=450)
                GERMAN_LEARN_SCORE += 2
            elif SCORE_TRACKER >= 10:
                STREAK_LABEL = Label(main_gui, text = "STREAK!\n" + str(SCORE_TRACKER) + "\nTriple points!",
                                     font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
                STREAK_LABEL.place(x=330, y=450)
                GERMAN_LEARN_SCORE += 3
            else:
                GERMAN_LEARN_SCORE += 1
            if ARCADE_MODE_BOOL == False:
                connection_cursor.execute("SELECT gprogress FROM LoginDetails WHERE username=?",(LOGIN_USERNAME,))
                past_score = connection_cursor.fetchone()
                new_score = past_score[0] + 1
                connection.execute("UPDATE LoginDetails SET gprogress = ? WHERE username = ?",
                                   (new_score,LOGIN_USERNAME,))
                connection.commit()
                german_learn_mode()
            else:
                german_learn_mode()
        else:
            SCORE_TRACKER = 0
            if ARCADE_SELECTED == 1:
                german_learn_mode()
            else:
                german_learn_entry.place(x=3000, y=3000)
                GERMAN_INCORRECT_ANSWER = Label(main_gui, text = "Incorrect answer.\n\nThe question was:\n" +
                                                GERMAN_LEARN_QUESTION + "\n\nYou typed in:\n" + their_answer +
                                                "\n\nThe correct answer was:\n" + GERMAN_LEARN_ANSWER +
                                                "\n\nPress continue to carry on.", font=("Lucida Sans", 10, "bold"),
                                                bd = 3, bg = "orange", fg = "white")
                GERMAN_INCORRECT_ANSWER.place(x=300, y=100)
                german_continue_button.place(x=365, y=320)
                main_gui.bind('<Return>',german_redirect_mode)


def spanish_arcade():
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global ARCADE_SELECTED
    global HELP_SECTION_TRACKER
    ARCADE_MODE_BOOL = True
    SPANISH_MODE_BOOL = True
    ARCADE_SELECTED = 1
    HELP_SECTION_TRACKER = 7
    help_storage()
    spanish_zone_label.place(x=3000, y=3000)
    spanish_arcade_button.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)
    spanish_arcade_start_button.place(x=360, y=300)


def german_arcade():
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global ARCADE_SELECTED
    global HELP_SECTION_TRACKER
    ARCADE_MODE_BOOL = True
    SPANISH_MODE_BOOL = False
    ARCADE_SELECTED = 1
    HELP_SECTION_TRACKER = 7
    help_storage()
    german_zone_label.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)
    german_arcade_start_button.place(x=360, y=300)
    

def spanish_arcade_mode():
    global HELP_SECTION_TRACKER
    global ARCADE_TIMER
    HELP_SECTION_TRACKER = 8
    help_storage()
    spanish_arcade_start_button.place(x=3000, y=3000)
    spanish_learn_mode()
    ARCADE_TIMER = 60
    countdown()
    main_gui.after(60500,main_learn)


def countdown():
    global ARCADE_TIMER
    global TIMER_THING
    if ARCADE_TIMER >= -1:
        try:
            TIMER_THING.place(x=3000, y=3000)
        except NameError:
            pass
        if ARCADE_TIMER >= 0:
            timer_label = str(ARCADE_TIMER) + " Seconds Left!"
            TIMER_THING = Label(main_gui, text = timer_label, font=("Lucida Sans", 10, "bold"), bd = 3,
                                bg = "orange", fg = "white")
            TIMER_THING.place(x=330, y=340)
            ARCADE_TIMER -= 1
            main_gui.after(1000,countdown)


def german_arcade_mode():
    global HELP_SECTION_TRACKER
    global ARCADE_TIMER
    HELP_SECTION_TRACKER = 8
    help_storage()
    german_arcade_start_button.place(x=3000, y=3000)
    german_learn_mode()
    ARCADE_TIMER = 60
    countdown()
    main_gui.after(60500,main_learn)


def close_leader_board():
    global LEADER_BOARD_OPEN_BOOL
    LEADER_BOARD_OPEN_BOOL = False
    leader_board_window.geometry("300x600+3000+3000")
    leader_board_button.place(x=460, y=550)


def leader_board_refresh():
    global LEADER_BOARD_OPEN_BOOL
    try:
        if LEADER_BOARD_OPEN_BOOL == True:
            leader_board()
    except NameError:
        pass


def leader_board():
    global LEADER_BOARD_OPEN_BOOL
    LEADER_BOARD_OPEN_BOOL = True
    leader_board_window.geometry("800x200+2+603")
    close_board = Button(leader_board_window, text="CLOSE", command=close_leader_board, bg="white", width="6",
                         height="1")
    close_board.config(font=("Lucida Sans", 8, "bold"))
    close_board.place(x=735, y=10)
    leader_board_label.place(x=280, y=10)
    leader_board_button.place(x=3000, y=3000)
    spanish_progress_list = []
    i = 1
    spanish_progress_list.append("SPANISH LEADER BOARD\n----------------------------------")
    for row1 in connection.execute("SELECT username,sprogress FROM LoginDetails ORDER BY sprogress DESC LIMIT 5"):
        row1 = str(row1)
        row1 = row1.replace("(","")
        row1 = row1.replace(")","")
        row1 = row1.replace("'","")
        spanish_progress_list.append("\n")
        spanish_progress_list.append(str(i) + ": " + row1)
        i += 1
    spanish_progress_list = ''.join(spanish_progress_list)
    top_5_spanish = Label(leader_board_window, text = spanish_progress_list, font=("Lucida Sans", 10, "bold"),
                          bd = 3, bg = "orange", fg = "white")
    top_5_spanish.place(x=50, y=70)
    german_progress_list = []
    i = 1
    german_progress_list.append("GERMAN LEADER BOARD\n-----------------------------------")
    for row2 in connection.execute("SELECT username,gprogress FROM LoginDetails ORDER BY gprogress DESC LIMIT 5"):
        row2 = str(row2)
        row2 = row2.replace("(","")
        row2 = row2.replace(")","")
        row2 = row2.replace("'","")
        german_progress_list.append("\n")
        german_progress_list.append(str(i) + ": " + row2)
        i += 1
    german_progress_list = ''.join(german_progress_list)
    top_5_german = Label(leader_board_window, text = german_progress_list, font=("Lucida Sans", 10, "bold"), bd = 3,
                         bg = "orange", fg = "white")
    top_5_german.place(x=310, y=70)
    arcade_progress_list = []
    i = 1
    arcade_progress_list.append("ARCADE LEADER BOARD\n-----------------------------------")
    for row3 in connection.execute("SELECT username,ascore FROM LoginDetails ORDER BY ascore DESC LIMIT 5"):
        row3 = str(row3)
        row3 = row3.replace("(","")
        row3 = row3.replace(")","")
        row3 = row3.replace("'","")
        arcade_progress_list.append("\n")
        arcade_progress_list.append(str(i) + ": " + row3)
        i += 1
    arcade_progress_list = ''.join(arcade_progress_list)
    top_5_arcade = Label(leader_board_window, text = arcade_progress_list, font=("Lucida Sans", 10, "bold"), bd = 3,
                         bg = "orange", fg = "white")
    top_5_arcade.place(x=570, y=70)


def main_learn():
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global SPANISH_LEARN_SCORE
    global GERMAN_LEARN_SCORE
    global HELP_SECTION_TRACKER
    global ARCADE_TIMER
    global GERMAN_INCORRECT_ANSWER
    global SPANISH_INCORRECT_ANSWER
    if ARCADE_MODE_BOOL:
        if SPANISH_MODE_BOOL:
            connection_cursor.execute("SELECT ascore FROM LoginDetails WHERE username=?",(LOGIN_USERNAME,))
            past_score = connection_cursor.fetchone()
            if past_score[0] < SPANISH_LEARN_SCORE:
                connection.execute("UPDATE LoginDetails SET ascore = ? WHERE username = ?",
                                   (SPANISH_LEARN_SCORE,LOGIN_USERNAME,))
                connection.commit()
        else:
            connection_cursor.execute("SELECT ascore FROM LoginDetails WHERE username=?",(LOGIN_USERNAME,))
            past_score = connection_cursor.fetchone()
            if past_score[0] < GERMAN_LEARN_SCORE:
                connection.execute("UPDATE LoginDetails SET ascore = ? WHERE username = ?",
                                   (GERMAN_LEARN_SCORE,LOGIN_USERNAME,))
                connection.commit()
    HELP_SECTION_TRACKER = 3
    help_storage()
    try:
        ARCADE_TIMER = -1
    except NameError:
        pass
    main_gui.unbind("<Return>")
    back_welcome_button.place(x=3000, y=3000)
    welcome_back_label.place(x=205, y=10)
    spanish_submit_button.place(x=3000, y=3000)
    german_submit_button.place(x=3000, y=3000)
    spanish_learn_button.place(x=300, y=200)
    back_learn_button.place(x=3000, y=3000)
    german_learn_button.place(x=410, y=200)
    spanish_zone_label.place(x=3000, y=3000)
    spanish_arcade_button.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)
    german_zone_label.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)
    spanish_question_menu.place(x=3000, y=3000)
    spanish_basics1_button.place(x=3000, y=3000)
    spanish_basics2_button.place(x=3000, y=3000)
    spanish_basics3_button.place(x=3000, y=3000)
    german_question_menu.place(x=3000, y=3000)
    german_basics1_button.place(x=3000, y=3000)
    german_basics2_button.place(x=3000, y=3000)
    german_basics3_button.place(x=3000, y=3000)
    ó_button.place(x=3000, y=3000)
    í_button.place(x=3000, y=3000)
    ñ_button.place(x=3000, y=3000)
    upside_down_question_mark_button.place(x=3000, y=3000)
    é_button.place(x=3000, y=3000)
    ú_button.place(x=3000, y=3000)
    á_button.place(x=3000, y=3000)
    ä_button.place(x=3000, y=3000)
    ß_button.place(x=3000, y=3000)
    ü_button.place(x=3000, y=3000)
    try:
        question_count_label.place(x=3000, y=3000)
        current_score_label.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        SPANISH_LEARN_QUESTION_NEW.place(x=3000, y=3000)
        spanish_learn_entry.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        GERMAN_LEARN_QUESTION_NEW.place(x=3000, y=3000)
        german_learn_entry.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        spanish_arcade_start_button.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        german_arcade_start_button.place(x=3000, y=3000)
    except NameError:
        pass
    logout_button.place(x=225, y=550)
    try:
        SPANISH_INCORRECT_ANSWER.place(x=3000, y=3000)
    except NameError:
        pass
    spanish_continue_button.place(x=3000, y=3000)
    try:
        GERMAN_INCORRECT_ANSWER.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        STREAK_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    german_continue_button.place(x=3000, y=3000)


def logout():
    leader_board_window.geometry("300x600+3000+3000")
    main_window()


def quit_function():
    main_gui.destroy()


################
# Admin System #
################

def admin_system():
    print("WIP")

##################
# Teacher System #
##################

def teacher_system():
    global VIEW_STUDENT_PROGRESS_LABEL
    global DONE_BACKUP_LABEL
    global RESET_PASSWORD_LABEL
    global DONE_RESET_LABEL
    global DELETE_USER_LABEL
    global RESTORE_BACKUP_LABEL
    id_field.place(x=3000, y=3000)
    reset_password_field.place(x=3000, y=3000)
    reset_password_button.place(x=3000, y=3000)
    back_teacher_button.place(x=3000, y=3000)
    submit_login_button.place(x=3000, y=3000)
    back_welcome_button.place(x=3000, y=3000)
    login_username_field.place(x=3000, y=3000)
    login_password_field.place(x=3000, y=3000)
    username_password_label.place(x=3000, y=3000)
    slogo_label.place(x=3000, y=3000)
    logging_in_label.place(x=3000, y=3000)
    back_teacher_button.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    teacher_section_label.place(x=225, y=10)
    logout_button.place(x=225, y=550)
    view_student_progress_button.place(x=400, y=200)
    change_password_button.place(x=300, y=200)
    add_questions_button.place(x=250, y=250)
    remove_questions_button.place(x=350, y=250)
    delete_user_button.place(x=450, y=250)
    initial_choice_label.place(x=300, y=130)
    save_backup_button.place(x=300, y=300)
    restore_backup_button.place(x=400, y=300)
    try:
        RESET_PASSWORD_LABEL.place(x=3000, y=3000)
        DONE_RESET_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        VIEW_STUDENT_PROGRESS_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        DONE_BACKUP_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        DELETE_USER_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        RESTORE_BACKUP_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    

def view_student_progress():
    global VIEW_STUDENT_PROGRESS_LABEL
    view_student_progress_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    back_teacher_button.place(x=299, y=550)
    i = 0
    for row in connection.execute("SELECT username,sprogress,gprogress,ascore FROM LoginDetails"):
        i += 1
    view_student_progress_list = []
    new_row = [""] * 4
    j = 1
    view_student_progress_list.append("LIST OF STUDENTS\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nNAME  -  SPANISH PROGRESS  -  GERMAN PROGRESS  -  ARCADE SCORE\n")
    for row in connection.execute("SELECT username,sprogress,gprogress,ascore FROM LoginDetails"):
        new_row[0] = str(row[0])
        new_row[1] = str(row[1])
        new_row[2] = str(row[2])
        new_row[3] = str(row[3])
        row = str(new_row)
        row = row.replace("[","")
        row = row.replace("]","")
        row = row.replace("'","")
        view_student_progress_list.append("\n")
        view_student_progress_list.append(str(j) + ": " + row)
        j += 1
    view_student_progress_list = ''.join(view_student_progress_list)
    VIEW_STUDENT_PROGRESS_LABEL = Label(main_gui, text = view_student_progress_list, font=("Lucida Sans", 10, "bold"), bd = 3,
                         bg = "orange", fg = "white")
    VIEW_STUDENT_PROGRESS_LABEL.place(x=10, y=110)
    

def change_password():
    global RESET_PASSWORD_LABEL
    view_student_progress_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    back_teacher_button.place(x=299, y=550)
    reset_password_list = "RESET USER PASSWORD\n\nStep 1: View list of students in other section.\nStep 2: Get the user ID of the student.\nStep 3: Enter the ID and the new password.\nStep 4: Click finalize and their password will have been reset.\n\nID:                                           PASSWORD:"
    RESET_PASSWORD_LABEL = Label(main_gui, text = reset_password_list, font=("Lucida Sans", 10, "bold"), bd = 3,
                         bg = "orange", fg = "white")
    RESET_PASSWORD_LABEL.place(x=190, y=110)
    id_field.place(x=237, y=240)
    reset_password_field.place(x=430, y=240)
    reset_password_button.place(x=365, y=240)


def reset_password_process():
    global RESET_PASSWORD_LABEL
    global DONE_RESET_LABEL
    if reset_password_field.get() and id_field.get():
        id_reset = id_field.get()
        reset_password = reset_password_field.get()
        reset_password_field.delete(0, END)
        id_field.delete(0, END)
        temp = ()
        for row in connection.execute("SELECT * FROM LoginDetails WHERE id = ?",
                                      (id_reset)):
            temp += row
        temp_check = temp
        temp = str(temp)
        if temp == "()":
            pass
        else:
            RESET_PASSWORD_LABEL.place(x=3000, y=3000)
            id_field.place(x=3000, y=3000)
            reset_password_field.place(x=3000, y=3000)
            reset_password_button.place(x=3000, y=3000)
            connection.execute("UPDATE LoginDetails SET password = ? WHERE id = ?",
                               (reset_password,id_reset))
            connection.commit()
            done_reset_text = "Password has been reset."
            DONE_RESET_LABEL = Label(main_gui, text = done_reset_text, font=("Lucida Sans", 10, "bold"), bd = 3,
                                 bg = "orange", fg = "white")
            DONE_RESET_LABEL.place(x=310, y=200)


def add_questions():
    print("WIP")


def remove_questions():
    print("WIP")


def delete_user():
    global DELETE_USER_LABEL
    view_student_progress_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    back_teacher_button.place(x=299, y=550)
    delete_user_list = "DELETE USER\n\nStep 1: Go back to the view list of students and get the id of the student to remove.\nStep 2: Go back here and enter the id.\nStep 3: Click finalize and the user will be deleted.\nID:                  "
    DELETE_USER_LABEL = Label(main_gui, text = delete_user_list, font=("Lucida Sans", 10, "bold"), bd = 3,
                         bg = "orange", fg = "white")
    DELETE_USER_LABEL.place(x=100, y=110)
    id_field.place(x=237, y=220)


def save_backup():
    global DONE_BACKUP_LABEL
    view_student_progress_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    back_teacher_button.place(x=299, y=550)
    done_backup_text = "BACKUP HAS BEEN MADE."
    DONE_BACKUP_LABEL = Label(main_gui, text = done_backup_text, font=("Lucida Sans", 10, "bold"), bd = 3,
                         bg = "orange", fg = "white")
    DONE_BACKUP_LABEL.place(x=340, y=200)
    backup_directory = os.path.dirname(sys.argv[0])
    directory = backup_directory
    directory += '/'
    backup_directory += '/backup/'
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    backup_directory += date
    perform_backup(backup_directory,directory)


def restore_backup():
    global RESTORE_BACKUP_LABEL
    view_student_progress_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    back_teacher_button.place(x=299, y=550)
    restore_backup_text = "HOW TO RESTORE A BACKUP\n\nStep 1: Decide how long ago the system was damaged.\nStep 2: Check the backup directory for the latest working backup.\nStep 3: Copy the contents inside and then close any Python programs that you have open.\nStep 4: Delete all items inside the Memrize folder that are not folders. DO NOT DELETE THE BACKUP FOLDER.\nStep 5: Then simply paste all of the backup files into the folder and run the program.\nStep 7: Delete any backups that are corrupted."
    RESTORE_BACKUP_LABEL = Label(main_gui, text = restore_backup_text, font=("Lucida Sans", 10, "bold"), bd = 3,
                         bg = "orange", fg = "white")
    RESTORE_BACKUP_LABEL.place(x=80, y=120)
    backup_directory = os.path.dirname(sys.argv[0])
    directory = str(backup_directory)
    print(directory)
    subprocess.Popen('explorer'.format(directory))
    
#######################
# SQLite3 connections #
#######################

connection = sqlite3.connect('login_details.db')
connection_cursor = connection.cursor()

###################
# Windows Go Here #
###################

main_gui = Tk()
main_gui.title("Memrize  -  By Ethan Champion")
main_gui.geometry("800x600+2+2")
main_gui.configure(background="orange")
main_gui.resizable(0, 0)
main_gui.overrideredirect(True)
main_gui.lift()

help_window = Toplevel(main_gui)
help_window.title("Help Window")
help_window.configure(background="orange")
help_window.geometry("300x600+3000+3000")
help_window.resizable(0, 0)
help_window.overrideredirect(True)

leader_board_window = Toplevel(main_gui)
leader_board_window.title("Leaderboard")
leader_board_window.configure(background="orange")
leader_board_window.geometry("500x600+3000+3000")
leader_board_window.resizable(0, 0)
leader_board_window.overrideredirect(True)

##################
# Labels Go Here #
##################

slogo_image = PhotoImage(file="slogo.gif")
slogo_label = Label(main_gui, image=slogo_image)
slogo_label.place(x=205, y=10)

initial_choice_image = PhotoImage(file="options.gif")
initial_choice_label = Label(main_gui, image=initial_choice_image)
initial_choice_label.place(x=300, y=150)

teacher_section_image = PhotoImage(file="teacher_section.gif")
teacher_section_label = Label(main_gui, image=teacher_section_image)
teacher_section_label.place(x=3000, y=3000)

username_password_image = PhotoImage(file="username_password.gif")
username_password_label = Label(main_gui, image=username_password_image)
username_password_label.place(x=3000, y=3000)

help_image = PhotoImage(file="help_page.gif")
help_label = Label(help_window, image=help_image)
help_label.place(x=3000, y=3000)

leader_board_image = PhotoImage(file="leader_board.gif")
leader_board_label = Label(leader_board_window, image=leader_board_image)
leader_board_label.place(x=3000, y=3000)

username_taken_image = PhotoImage(file="username_taken.gif")
username_taken_label = Label(main_gui, image=username_taken_image)
username_taken_label.place(x=3000, y=3000)

username_length_image = PhotoImage(file="username_length.gif")
username_length_label = Label(main_gui, image=username_length_image)
username_length_label.place(x=3000, y=3000)

password_error_image = PhotoImage(file="password_error.gif")
password_error_label = Label(main_gui, image=password_error_image)
password_error_label.place(x=3000, y=3000)

logging_in_image = PhotoImage(file="logging_in.gif")
logging_in_label = Label(main_gui, image=logging_in_image)
logging_in_label.place(x=3000, y=3000)

registered_image = PhotoImage(file="registered.gif")
registered_label = Label(main_gui, image=registered_image)
registered_label.place(x=3000, y=3000)

login_error_image = PhotoImage(file="login_error.gif")
login_error_label = Label(main_gui, image=login_error_image)
login_error_label.place(x=3000, y=3000)

welcome_back_image = PhotoImage(file="welcome_back.gif")
welcome_back_label = Label(main_gui, image=welcome_back_image)
welcome_back_label.place(x=3000, y=3000)

spanish_zone_image = PhotoImage(file="spanish_zone.gif")
spanish_zone_label = Label(main_gui, image=spanish_zone_image)
spanish_zone_label.place(x=3000, y=3000)

german_zone_image = PhotoImage(file="german_zone.gif")
german_zone_label = Label(main_gui, image=german_zone_image)
german_zone_label.place(x=3000, y=3000)

###################
# Entries go here #
###################

new_username_field = Entry(main_gui)
new_username_field.place(x=3000, y=3000)

new_password_field = Entry(main_gui, show="*")
new_password_field.place(x=3000, y=3000)

login_username_field = Entry(main_gui)
login_username_field.place(x=3000, y=3000)

login_password_field = Entry(main_gui, show="*")
login_password_field.place(x=3000, y=3000)

spanish_learn_entry = Entry(main_gui, width = 40)
spanish_learn_entry.place(x=3000, y=3000)

german_learn_entry = Entry(main_gui, width = 40)
german_learn_entry.place(x=3000, y=3000)

id_field = Entry(main_gui)
id_field.place(x=3000, y=3000)

reset_password_field = Entry(main_gui)
reset_password_field.place(x=3000, y=3000)

###################
# Buttons go here #
###################

quit_button = Button(main_gui, text="QUIT", command=quit_function, bg="white", width="5", height="1")
quit_button.config(font=("Lucida Sans", 8, "bold"))
quit_button.place(x=352, y=550)
quit_button.flash()

help_button = Button(main_gui, text="HELP", command=help_function, bg="white", width="5", height="1")
help_button.config(font=("Lucida Sans", 8, "bold"))
help_button.place(x=405, y=550)
help_button.flash()

back_welcome_button = Button(main_gui, text="BACK", command=main_window, bg="white", width="5", height="1")
back_welcome_button.config(font=("Lucida Sans", 8, "bold"))
back_welcome_button.place(x=3000, y=3000)
back_welcome_button.flash()

back_learn_button = Button(main_gui, text="BACK", command=main_learn, bg="white", width="5", height="1")
back_learn_button.config(font=("Lucida Sans", 8, "bold"))
back_learn_button.place(x=3000, y=3000)
back_learn_button.flash()

back_teacher_button = Button(main_gui, text="BACK", command=teacher_system, bg="white", width="5", height="1")
back_teacher_button.config(font=("Lucida Sans", 8, "bold"))
back_teacher_button.place(x=3000, y=3000)
back_teacher_button.flash()

register_button = Button(main_gui, text="REGISTER", command=initial_register, bg="white", width="9", height="2")
register_button.config(font=("Lucida Sans", 12, "bold"))
register_button.place(x=300, y=220)
register_button.flash()

login_button = Button(main_gui, text="LOGIN", command=initial_login, bg="white", width="8", height="2")
login_button.config(font=("Lucida Sans", 12, "bold"))
login_button.place(x=410, y=220)
login_button.flash()

submit_register_button = Button(main_gui, text="SUBMIT", command=submit_register, bg="white", width="7", height="2")
submit_register_button.config(font=("Lucida Sans", 8, "bold"))
submit_register_button.place(x=3000, y=3000)
submit_register_button.flash()

submit_login_button = Button(main_gui, text="SUBMIT", command=submit_login, bg="white", width="7", height="2")
submit_login_button.config(font=("Lucida Sans", 8, "bold"))
submit_login_button.place(x=3000, y=3000)
submit_login_button.flash()

spanish_learn_button = Button(main_gui, text="SPANISH", command=spanish_modules, bg="white", width="9", height="2")
spanish_learn_button.config(font=("Lucida Sans", 12, "bold"))
spanish_learn_button.place(x=3000, y=3000)
spanish_learn_button.flash()

german_learn_button = Button(main_gui, text="GERMAN", command=german_modules, bg="white", width="9", height="2")
german_learn_button.config(font=("Lucida Sans", 12, "bold"))
german_learn_button.place(x=3000, y=3000)
german_learn_button.flash()

spanish_basics1_button = Button(main_gui, text="BASICS 1", command=spanish_basics1_module, bg="white", width="9",
                                height="2")
spanish_basics1_button.config(font=("Lucida Sans", 12, "bold"))
spanish_basics1_button.place(x=3000, y=3000)
spanish_basics1_button.flash()

spanish_basics2_button = Button(main_gui, text="BASICS 2", command=spanish_basics2_module, bg="white", width="9",
                                height="2")
spanish_basics2_button.config(font=("Lucida Sans", 12, "bold"))
spanish_basics2_button.place(x=3000, y=3000)
spanish_basics2_button.flash()

spanish_basics3_button = Button(main_gui, text="BASICS 3", command=spanish_basics3_module, bg="white", width="9",
                                height="2")
spanish_basics3_button.config(font=("Lucida Sans", 12, "bold"))
spanish_basics3_button.place(x=3000, y=3000)
spanish_basics3_button.flash()

german_basics1_button = Button(main_gui, text="BASICS 1", command=german_basics1_module, bg="white", width="9",
                               height="2")
german_basics1_button.config(font=("Lucida Sans", 12, "bold"))
german_basics1_button.place(x=3000, y=3000)
german_basics1_button.flash()

german_basics2_button = Button(main_gui, text="BASICS 2", command=german_basics2_module, bg="white", width="9",
                               height="2")
german_basics2_button.config(font=("Lucida Sans", 12, "bold"))
german_basics2_button.place(x=3000, y=3000)
german_basics2_button.flash()

german_basics3_button = Button(main_gui, text="BASICS 3", command=german_basics3_module, bg="white", width="9",
                               height="2")
german_basics3_button.config(font=("Lucida Sans", 12, "bold"))
german_basics3_button.place(x=3000, y=3000)
german_basics3_button.flash()

spanish_learn_mode_button = Button(main_gui, text="LEARN MODE", command=spanish_learn_mode, bg="white", width="12",
                                   height="3")
spanish_learn_mode_button.config(font=("Lucida Sans", 10, "bold"))
spanish_learn_mode_button.place(x=3000, y=3000)
spanish_learn_mode_button.flash()

spanish_arcade_button = Button(main_gui, text="ARCADE MODE", command=spanish_arcade, bg="white", width="14",
                               height="3")
spanish_arcade_button.config(font=("Lucida Sans", 10, "bold"))
spanish_arcade_button.place(x=3000, y=3000)
spanish_arcade_button.flash()

german_learn_mode_button = Button(main_gui, text="LEARN MODE", command=german_learn_mode, bg="white", width="12",
                                  height="3")
german_learn_mode_button.config(font=("Lucida Sans", 10, "bold"))
german_learn_mode_button.place(x=3000, y=3000)
german_learn_mode_button.flash()

german_arcade_button = Button(main_gui, text="ARCADE MODE", command=german_arcade, bg="white", width="14",
                              height="3")
german_arcade_button.config(font=("Lucida Sans", 10, "bold"))
german_arcade_button.place(x=3000, y=3000)
german_arcade_button.flash()

spanish_arcade_start_button = Button(main_gui, text="START", command=spanish_arcade_mode, bg="white", width="7",
                                     height="2")
spanish_arcade_start_button.config(font=("Lucida Sans", 10, "bold"))
spanish_arcade_start_button.place(x=3000, y=3000)
spanish_arcade_start_button.flash()

german_arcade_start_button = Button(main_gui, text="START", command=german_arcade_mode, bg="white", width="7",
                                    height="2")
german_arcade_start_button.config(font=("Lucida Sans", 10, "bold"))
german_arcade_start_button.place(x=3000, y=3000)
german_arcade_start_button.flash()

leader_board_button = Button(main_gui, text="LEADER-BOARD", command=leader_board, bg="white", width="13",
                             height="1")
leader_board_button.config(font=("Lucida Sans", 8, "bold"))
leader_board_button.place(x=3000, y=3000)
leader_board_button.flash()

logout_button = Button(main_gui, text="LOGOUT", command=logout, bg="white", width="8", height="1")
logout_button.config(font=("Lucida Sans", 8, "bold"))
logout_button.place(x=3000, y=3000)
logout_button.flash()

spanish_continue_button = Button(main_gui, text="CONTINUE", command=spanish_learn_mode, bg="white", width="9",
                                 height="2")
spanish_continue_button.config(font=("Lucida Sans", 8, "bold"))
spanish_continue_button.place(x=3000, y=3000)
spanish_continue_button.flash()

german_continue_button = Button(main_gui, text="CONTINUE", command=german_learn_mode, bg="white", width="9",
                                height="2")
german_continue_button.config(font=("Lucida Sans", 8, "bold"))
german_continue_button.place(x=3000, y=3000)
german_continue_button.flash()

ó_button = Button(main_gui, text="ó", command=ó, bg="white", width="2", height="1")
ó_button.config(font=("Lucida Sans", 8, "bold"))
ó_button.place(x=3000, y=3000)
ó_button.flash()

í_button = Button(main_gui, text="í", command=í, bg="white", width="2", height="1")
í_button.config(font=("Lucida Sans", 8, "bold"))
í_button.place(x=3000, y=3000)
í_button.flash()

é_button = Button(main_gui, text="é", command=é, bg="white", width="2", height="1")
é_button.config(font=("Lucida Sans", 8, "bold"))
é_button.place(x=3000, y=3000)
é_button.flash()

upside_down_question_mark_button = Button(main_gui, text="¿", command=upside_down_question_mark, bg="white",
                                          width="2", height="1")
upside_down_question_mark_button.config(font=("Lucida Sans", 8, "bold"))
upside_down_question_mark_button.place(x=3000, y=3000)
upside_down_question_mark_button.flash()

ñ_button = Button(main_gui, text="ñ", command=ñ, bg="white", width="2", height="1")
ñ_button.config(font=("Lucida Sans", 8, "bold"))
ñ_button.place(x=3000, y=3000)
ñ_button.flash()

ú_button = Button(main_gui, text="ú", command=ú, bg="white", width="2", height="1")
ú_button.config(font=("Lucida Sans", 8, "bold"))
ú_button.place(x=3000, y=3000)
ú_button.flash()

á_button = Button(main_gui, text="á", command=á, bg="white", width="2", height="1")
á_button.config(font=("Lucida Sans", 8, "bold"))
á_button.place(x=3000, y=3000)
á_button.flash()

ä_button = Button(main_gui, text="ä", command=ä, bg="white", width="2", height="1")
ä_button.config(font=("Lucida Sans", 8, "bold"))
ä_button.place(x=3000, y=3000)
ä_button.flash()

ü_button = Button(main_gui, text="ü", command=ü, bg="white", width="2", height="1")
ü_button.config(font=("Lucida Sans", 8, "bold"))
ü_button.place(x=3000, y=3000)
ü_button.flash()

ß_button = Button(main_gui, text="ß", command=ß, bg="white", width="2", height="1")
ß_button.config(font=("Lucida Sans", 8, "bold"))
ß_button.place(x=3000, y=3000)
ß_button.flash()

spanish_submit_button = Button(main_gui, text="SUBMIT", command=spanish_learn_process, bg="white", width="9",
                                 height="2")
spanish_submit_button.config(font=("Lucida Sans", 8, "bold"))
spanish_submit_button.place(x=3000, y=3000)
spanish_submit_button.flash()

german_submit_button = Button(main_gui, text="SUBMIT", command=german_learn_process, bg="white", width="9",
                                 height="2")
german_submit_button.config(font=("Lucida Sans", 8, "bold"))
german_submit_button.place(x=3000, y=3000)
german_submit_button.flash()

view_student_progress_button = Button(main_gui, text="LIST OF\nPROGRESS", command=view_student_progress, bg="white", width="12",
                                 height="3")
view_student_progress_button.config(font=("Lucida Sans", 8, "bold"))
view_student_progress_button.place(x=3000, y=3000)
view_student_progress_button.flash()

change_password_button = Button(main_gui, text="CHANGE\nPASSWORD", command=change_password, bg="white", width="12",
                                 height="3")
change_password_button.config(font=("Lucida Sans", 8, "bold"))
change_password_button.place(x=3000, y=3000)
change_password_button.flash()

add_questions_button = Button(main_gui, text="ADD\nQUESTIONS", command=add_questions, bg="white", width="12",
                                 height="3")
add_questions_button.config(font=("Lucida Sans", 8, "bold"))
add_questions_button.place(x=3000, y=3000)
add_questions_button.flash()

remove_questions_button = Button(main_gui, text="REMOVE\nQUESTIONS", command=remove_questions, bg="white", width="12",
                                 height="3")
remove_questions_button.config(font=("Lucida Sans", 8, "bold"))
remove_questions_button.place(x=3000, y=3000)
remove_questions_button.flash()

delete_user_button = Button(main_gui, text="DELETE\nUSER", command=delete_user, bg="white", width="12",
                                 height="3")
delete_user_button.config(font=("Lucida Sans", 8, "bold"))
delete_user_button.place(x=3000, y=3000)
delete_user_button.flash()

save_backup_button = Button(main_gui, text="SAVE\nBACKUP", command=save_backup, bg="white", width="12",
                                 height="3")
save_backup_button.config(font=("Lucida Sans", 8, "bold"))
save_backup_button.place(x=3000, y=3000)
save_backup_button.flash()

restore_backup_button = Button(main_gui, text="RESTORE\nBACKUP", command=restore_backup, bg="white", width="12",
                                 height="3")
restore_backup_button.config(font=("Lucida Sans", 8, "bold"))
restore_backup_button.place(x=3000, y=3000)
restore_backup_button.flash()

reset_password_button = Button(main_gui, text="RESET", command=reset_password_process, bg="white", width="7", height="2")
reset_password_button.config(font=("Lucida Sans", 8, "bold"))
reset_password_button.place(x=3000, y=3000)
reset_password_button.flash()

########################
# Option Menus Go Here #
########################

spanish_option_menu_default = StringVar(main_gui)
spanish_option_menu_default.set("Question sets from teachers:")

spanish_question_menu = OptionMenu(main_gui, spanish_option_menu_default, "Basics 1", "Basics 2", "Basics 3")
spanish_question_menu.config(font=("Lucida Sans", 8, "bold"))
spanish_question_menu.place(x=3000, y=3000)

german_option_menu_default = StringVar(main_gui)
german_option_menu_default.set("Question sets from teachers:")

german_question_menu = OptionMenu(main_gui, german_option_menu_default, "Basics 1", "Basics 2", "Basics 3")
german_question_menu.config(font=("Lucida Sans", 8, "bold"))
german_question_menu.place(x=3000, y=3000)

############################
# Initialising the Program #
############################

if os.path.isfile('login_details.db') == False:
    create()

main_window()
main_gui.mainloop()
