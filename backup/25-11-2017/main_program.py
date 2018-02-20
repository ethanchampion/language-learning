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
from tkinter import ttk
import sqlite3
import random
import time
import os
import datetime
import sys
from database_creation import create
from question_database_creation import create1
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
on this window close the help window.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
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
has been made.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 2:
        HELP_TEXT_LABEL = Label(help_window,text=
'''You are currently in the login section.
In this section you have to enter your
username you originally chose and the
password as well. If you forget your
password ask your teacher to reset it.
Once you have filled it in click SUBMIT or
press enter and you will sign in.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 3:
        Help_Text_Label = Label(help_window,text=
'''You have logged in successfully.
Now in this section you have to choose
what language you are going to be
learning or practicising. You will now
also be able to see a leader board
button at the bottom which displays
the top 5 learners of each class.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        Help_Text_Label.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 4:
        HELP_TEXT_LABEL = Label(help_window,text=
'''You now have a choice of which module
of your language you will choose. The
program provides three basic ones or
you can choose from the drop down
menu modules that your teacher has
added. Simply click the rectangle and it
will provide you which the options.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
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
quick as possible.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 6:
        HELP_TEXT_LABEL = Label(help_window,text=
'''You are now in the teacher section.
In this section you have 7 options to
choose from.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 7:
        HELP_TEXT_LABEL = Label(help_window,text=
'''This is a basic module which you
can use to see the ids of each student.
You will be able to use this when
changing user passwords and when
deleting users.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 8:
        HELP_TEXT_LABEL = Label(help_window,text=
'''This is the change password module.
You should use the list progress button
on the previous section to check the id
of the student you want to reset their
password.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 9:
        HELP_TEXT_LABEL = Label(help_window,text=
'''This is the add questions function.
You should see a notepad opened up on
your screen. Follow the on screen
instructions and make sure to only
select either spanish or german.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 10:
        HELP_TEXT_LABEL = Label(help_window,text=
'''This is the remove questions
function. Like with other functions
simply follow the instructions and
select the id of the question set
that you would like to remove. Type
it in and then submit. It will
automatically be removed.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 11:
        HELP_TEXT_LABEL = Label(help_window,text=
'''This is the delete user function.
This will delete any user in the
database. Simply find the user's ID
and enter it. Then submit and it
will be deleted.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 12:
        HELP_TEXT_LABEL = Label(help_window,text=
'''This is the save backup function.
This will save a backup automatically
so that nothing is lost in the
database. Make sure to do this
regularly.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)
    elif HELP_SECTION_TRACKER == 13:
        HELP_TEXT_LABEL = Label(help_window,text=
'''This is the restore backup
function. This will open lots of
things but it is pretty easy.
Essentially read the notepad
that has been opened.''', font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        HELP_TEXT_LABEL.place(x=10,y=100)


def create_spanish_combo_box():
    global SPANISH_MODULE_COMBOBOX
    spanish_question_sets = []
    for item in question_connection.execute("SELECT * FROM QuestionSets"):
        if item[2] == 1:
            spanish_question_sets.append(item[1])
    spanish_module_default = StringVar(main_gui)
    try:
        spanish_module_default.set(spanish_question_sets[0])
    except IndexError:
        spanish_module_default.set("No Spanish question sets found.")
    SPANISH_MODULE_COMBOBOX = ttk.Combobox(main_gui, textvariable=spanish_module_default, values=spanish_question_sets, width=60)
    SPANISH_MODULE_COMBOBOX.state(['readonly'])
    SPANISH_MODULE_COMBOBOX.place(x=3000, y=3000)


def create_id_combo_box():
    global ID_MODULE_COMBOBOX
    id_question_sets = []
    for item in question_connection.execute("SELECT * FROM QuestionSets"):
        temp_array = [item[0],item[1]]
        id_question_sets.append(temp_array)
    id_module_default = StringVar(main_gui)
    try:
        id_module_default.set(id_question_sets[0])
    except IndexError:
        id_module_default.set("No question sets found.")
    ID_MODULE_COMBOBOX = ttk.Combobox(main_gui, textvariable=id_module_default, values=id_question_sets, width=60)
    ID_MODULE_COMBOBOX.state(['readonly'])
    ID_MODULE_COMBOBOX.place(x=3000, y=3000)


def create_german_combo_box():
    global GERMAN_MODULE_COMBOBOX
    german_question_sets = []
    for item in question_connection.execute("SELECT * FROM QuestionSets"):
        if item[3] == 1:
            german_question_sets.append(item[1])
    german_module_default = StringVar(main_gui)
    try:
        german_module_default.set(german_question_sets[0])
    except IndexError:
        german_module_default.set("No question sets found.")
    GERMAN_MODULE_COMBOBOX = ttk.Combobox(main_gui, textvariable=german_module_default, values=german_question_sets, width=60)
    GERMAN_MODULE_COMBOBOX.state(['readonly'])
    GERMAN_MODULE_COMBOBOX.place(x=3000, y=3000)


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
                connection.execute("INSERT INTO LoginDetails(username,password,teacher,admin,sprogress,gprogress,ascore) VALUES (?,?,0,0,0,0,0)",(new_username, new_password,))
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
        for row in connection.execute("SELECT * FROM LoginDetails WHERE username = ? AND password = ?",(LOGIN_USERNAME, LOGIN_PASSWORD)):
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
            for row in connection.execute("SELECT sprogress FROM LoginDetails WHERE username = ? AND password = ?",(LOGIN_USERNAME, LOGIN_PASSWORD)):
                SPROGRESS = row
            GPROGRESS = ""
            for row in connection.execute("SELECT gprogress FROM LoginDetails WHERE username = ? AND password = ?",(LOGIN_USERNAME, LOGIN_PASSWORD)):
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
    global DONE_ADD_QUESTIONS_LABEL
    global RESET_PASSWORD_LABEL
    global SPANISH_MODULE_COMBOBOX
    global ID_MODULE_COMBOBOX
    global REMOVE_QUESTIONS_LABEL
    global DONE_QUESTIONS_LABEL
    global DELETE_USER_LABEL
    global RESTORE_BACKUP_LABEL
    global DONE_REMOVE_LABEL
    global ADD_QUESTIONS_LABEL
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
    id_questions_field.place(x=3000, y=3000)
    remove_questions_continue_button.place(x=3000, y=3000)
    submit_login_button.place(x=3000, y=3000)
    registered_label.place(x=3000, y=3000)
    logging_in_label.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
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
    add_questions_field.place(x=3000, y=3000)
    add_questions_spanish_checkbutton.place(x=3000, y=3000)
    add_questions_german_checkbutton.place(x=3000, y=3000)
    id_delete_field.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)
    welcome_back_label.place(x=3000, y=3000)
    remove_user_button.place(x=3000, y=3000)
    leader_board_button.place(x=3000, y=3000)
    spanish_learn_entry.place(x=3000, y=3000)
    add_questions_submit_button.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    german_zone_label.place(x=3000, y=3000)
    module_spanish_continue_button.place(x=3000, y=3000)
    module_german_continue_button.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)
    german_arcade_start_button.place(x=3000, y=3000)
    spanish_arcade_start_button.place(x=3000, y=3000)
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
    try:
        ID_MODULE_COMBOBOX.place(x=3000, y=3000)
        REMOVE_QUESTIONS_LABEL.place(x=3000, y=3000)
        DONE_QUESTIONS_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        ADD_QUESTIONS_LABEL.place(x=3000, y=3000)
        DONE_ADD_QUESTIONS_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        GERMAN_MODULE_COMBOBOX.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        SPANISH_MODULE_COMBOBOX.place(x=3000, y=3000)
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
        RESET_PASSWORD_LABEL.place(x=3000, y=3000)
        DONE_RESET_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        DELETE_USER_LABEL.place(x=3000, y=3000)
        DONE_REMOVE_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    

################
# Login System #
################

def login_system():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 3
    help_storage()
    submit_login_button.place(x=3000, y=3000)
    back_welcome_button.place(x=3000, y=3000)
    login_password_field.place(x=3000, y=3000)
    username_password_label.place(x=3000, y=3000)
    slogo_label.place(x=3000, y=3000)
    login_username_field.place(x=3000, y=3000)
    logging_in_label.place(x=3000, y=3000)
    welcome_back_label.place(x=205, y=10)
    spanish_learn_button.place(x=300, y=200)
    german_learn_button.place(x=410, y=200)
    leader_board_button.place(x=460, y=550)
    logout_button.place(x=225, y=550)


def spanish_modules():
    global SPANISH_MODULE_COMBOBOX
    create_spanish_combo_box()
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 4
    help_storage()
    welcome_back_label.place(x=3000, y=3000)
    spanish_learn_button.place(x=3000, y=3000)
    german_learn_button.place(x=3000, y=3000)
    back_learn_button.place(x=299, y=550)
    SPANISH_MODULE_COMBOBOX.place(x=220, y=200)
    spanish_zone_label.place(x=205, y=10)
    module_spanish_continue_button.place(x=620, y=200)


def spanish_module_selected():
    global SPANISH_MODULE_COMBOBOX
    global SPANISH_MODULE
    if SPANISH_MODULE_COMBOBOX.get():
        SPANISH_MODULE = SPANISH_MODULE_COMBOBOX.get()
        SPANISH_MODULE = SPANISH_MODULE.replace(" ","_").lower()
        SPANISH_MODULE += ".txt"
        spanish_learn()
        

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
    global SPANISH_MODULE_COMBOBOX
    global SPANISH_MODULE
    global MODULE_COUNT_TRACKER
    MODULE_COUNT_TRACKER = 0
    try:
        with open(SPANISH_MODULE,'r') as f:
            contents = f.read()
            contents = contents.split(",")
            for item in contents:
                MODULE_COUNT_TRACKER += 1
        SPANISH_MODULE_COMBOBOX.place(x=3000, y=3000)
        module_spanish_continue_button.place(x=3000, y=3000)
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
    except FileNotFoundError:
        SPANISH_MODULE_COMBOBOX.place(x=3000, y=3000)
        module_spanish_continue_button.place(x=3000, y=3000)
        spanish_modules()


def german_modules():
    global GERMAN_MODULE_COMBOBOX
    create_german_combo_box()
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 4
    help_storage()
    welcome_back_label.place(x=3000, y=3000)
    spanish_learn_button.place(x=3000, y=3000)
    german_learn_button.place(x=3000, y=3000)
    back_learn_button.place(x=299, y=550)
    GERMAN_MODULE_COMBOBOX.place(x=220, y=200)
    german_zone_label.place(x=205, y=10)
    module_german_continue_button.place(x=620, y=200)


def german_module_selected():
    global GERMAN_MODULE_COMBOBOX
    global GERMAN_MODULE
    if GERMAN_MODULE_COMBOBOX.get():
        GERMAN_MODULE = GERMAN_MODULE_COMBOBOX.get()
        GERMAN_MODULE = GERMAN_MODULE.replace(" ","_").lower()
        GERMAN_MODULE += ".txt"
        german_learn()


def german_learn():
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global GERMAN_SCORE_COUNT
    global HELP_SECTION_TRACKER
    global ARCADE_SELECTED
    global GERMAN_LEARN_SCORE
    global GERMAN_LEARN_COUNT
    global GERMAN_MODULE_COMBOBOX
    global MODULE_COUNT_TRACKER
    global SCORE_TRACKER
    global GERMAN_MODULE
    SCORE_TRACKER = 0
    MODULE_COUNT_TRACKER = 0
    with open(GERMAN_MODULE,'r') as f:
        contents = f.read()
        contents = contents.split(",")
        for item in contents:
            MODULE_COUNT_TRACKER += 1
    GERMAN_MODULE_COMBOBOX.place(x=3000, y=3000)
    module_german_continue_button.place(x=3000, y=3000)
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
            SPANISH_LEARN_QUESTION_NEW = Label(main_gui, text = even_question, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
            SPANISH_LEARN_QUESTION_NEW.place(x=200, y=100)
        else:
            SPANISH_LEARN_ANSWER = contents[random_number-1]
            odd_question = question_count + "\n\n" + current_score + "\n\n\n\n" + SPANISH_LEARN_QUESTION
            odd_question += "\n\nType the English for the Spanish above and press Enter:"
            SPANISH_LEARN_QUESTION_NEW = Label(main_gui, text = odd_question, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
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
                STREAK_LABEL = Label(main_gui, text = "STREAK!\n" + str(SCORE_TRACKER) + "\nDouble points!", font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
                STREAK_LABEL.place(x=330, y=450)
                SPANISH_LEARN_SCORE += 2
            elif SCORE_TRACKER >= 10:
                STREAK_LABEL = Label(main_gui, text = "STREAK!\n" + str(SCORE_TRACKER) + "\nTriple points!", font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
                STREAK_LABEL.place(x=330, y=450)
                SPANISH_LEARN_SCORE += 3
            else:
                SPANISH_LEARN_SCORE += 1
            connection_cursor.execute("SELECT sprogress FROM LoginDetails WHERE username=?",(LOGIN_USERNAME,))
            past_score = connection_cursor.fetchone()
            new_score = past_score[0] + 1
            connection.execute("UPDATE LoginDetails SET sprogress = ? WHERE username = ?",(new_score,LOGIN_USERNAME,))
            connection.commit()
            leader_board_refresh()
            spanish_learn_mode()
        else:
            SCORE_TRACKER = 0
            if ARCADE_SELECTED == 1:
                spanish_learn_mode()
            else:
                spanish_learn_entry.place(x=3000, y=3000)
                SPANISH_INCORRECT_ANSWER = Label(main_gui, text = "Incorrect answer.\n\nThe question was:\n" + SPANISH_LEARN_QUESTION + "\n\nYou typed in:\n" + their_answer + "\n\nThe correct answer was:\n" + SPANISH_LEARN_ANSWER + "\n\nPress continue to carry on.", font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
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
            GERMAN_LEARN_QUESTION_NEW = Label(main_gui, text = even_question, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
            GERMAN_LEARN_QUESTION_NEW.place(x=200, y=100)
        else:
            GERMAN_LEARN_ANSWER = contents[random_number-1]
            odd_question = question_count + "\n\n" + current_score + "\n\n\n\n" + GERMAN_LEARN_QUESTION
            odd_question += "\n\nType the German for the English above and press Enter:"
            GERMAN_LEARN_QUESTION_NEW = Label(main_gui, text = odd_question, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
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
                STREAK_LABEL = Label(main_gui, text = "STREAK!\n" + str(SCORE_TRACKER) + "\nDouble points!", font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
                STREAK_LABEL.place(x=330, y=450)
                GERMAN_LEARN_SCORE += 2
            elif SCORE_TRACKER >= 10:
                STREAK_LABEL = Label(main_gui, text = "STREAK!\n" + str(SCORE_TRACKER) + "\nTriple points!", font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
                STREAK_LABEL.place(x=330, y=450)
                GERMAN_LEARN_SCORE += 3
            else:
                GERMAN_LEARN_SCORE += 1
            if ARCADE_MODE_BOOL == False:
                connection_cursor.execute("SELECT gprogress FROM LoginDetails WHERE username=?",(LOGIN_USERNAME,))
                past_score = connection_cursor.fetchone()
                new_score = past_score[0] + 1
                connection.execute("UPDATE LoginDetails SET gprogress = ? WHERE username = ?",(new_score,LOGIN_USERNAME,))
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
                GERMAN_INCORRECT_ANSWER = Label(main_gui, text = "Incorrect answer.\n\nThe question was:\n" + GERMAN_LEARN_QUESTION + "\n\nYou typed in:\n" + their_answer + "\n\nThe correct answer was:\n" + GERMAN_LEARN_ANSWER + "\n\nPress continue to carry on.", font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
                GERMAN_INCORRECT_ANSWER.place(x=300, y=100)
                german_continue_button.place(x=365, y=320)
                main_gui.bind('<Return>',german_redirect_mode)


def spanish_arcade():
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global ARCADE_SELECTED
    ARCADE_MODE_BOOL = True
    SPANISH_MODE_BOOL = True
    ARCADE_SELECTED = 1
    help_storage()
    spanish_zone_label.place(x=3000, y=3000)
    spanish_arcade_button.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)
    spanish_arcade_start_button.place(x=360, y=300)


def german_arcade():
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global ARCADE_SELECTED
    ARCADE_MODE_BOOL = True
    SPANISH_MODE_BOOL = False
    ARCADE_SELECTED = 1
    help_storage()
    german_zone_label.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)
    german_arcade_start_button.place(x=360, y=300)
    

def spanish_arcade_mode():
    global ARCADE_TIMER
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
            TIMER_THING = Label(main_gui, text = timer_label, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
            TIMER_THING.place(x=330, y=340)
            ARCADE_TIMER -= 1
            main_gui.after(1000,countdown)


def german_arcade_mode():
    global ARCADE_TIMER
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
    close_board = Button(leader_board_window, text="CLOSE", command=close_leader_board, bg="white", width="6", height="1")
    close_board.config(font=("Lucida Sans", 8, "bold"))
    close_board.place(x=735, y=10)
    leader_board_label.place(x=280, y=10)
    leader_board_button.place(x=3000, y=3000)
    spanish_progress_list = []
    i = 1
    new_row1 = [""] * 2
    spanish_progress_list.append("SPANISH LEADER BOARD\n----------------------------------")
    for row1 in connection.execute("SELECT username,teacher,admin,sprogress FROM LoginDetails ORDER BY sprogress DESC LIMIT 5"):
        if row1[1] == 1 or row1[2] == 1:
            pass
        else:
            new_row1[0] = row1[0]
            new_row1[1] = str(row1[3])
            row1 = str(new_row1)
            row1 = row1.replace("[","")
            row1 = row1.replace("]","")
            row1 = row1.replace("'","")
            spanish_progress_list.append("\n")
            spanish_progress_list.append(str(i) + ": " + row1)
            i += 1
    spanish_progress_list = ''.join(spanish_progress_list)
    top_5_spanish = Label(leader_board_window, text = spanish_progress_list, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
    top_5_spanish.place(x=50, y=70)
    german_progress_list = []
    i = 1
    new_row2 = [""] * 2
    german_progress_list.append("GERMAN LEADER BOARD\n-----------------------------------")
    for row2 in connection.execute("SELECT username,teacher,admin,gprogress FROM LoginDetails ORDER BY gprogress DESC LIMIT 5"):
        if row2[1] == 1 or row2[2] == 1:
            pass
        else:
            new_row2[0] = row2[0]
            new_row2[1] = str(row2[3])
            row2 = str(new_row2)
            row2 = row2.replace("[","")
            row2 = row2.replace("]","")
            row2 = row2.replace("'","")
            german_progress_list.append("\n")
            german_progress_list.append(str(i) + ": " + row2)
            i += 1
    german_progress_list = ''.join(german_progress_list)
    top_5_german = Label(leader_board_window, text = german_progress_list, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
    top_5_german.place(x=310, y=70)
    arcade_progress_list = []
    i = 1
    new_row3 = [""] * 2
    arcade_progress_list.append("ARCADE LEADER BOARD\n-----------------------------------")
    for row3 in connection.execute("SELECT username,teacher,admin,ascore FROM LoginDetails ORDER BY ascore DESC LIMIT 5"):
        if row3[1] == 1 or row3[2] == 1:
            pass
        else:
            new_row3[0] = row3[0]
            new_row3[1] = str(row3[3])
            row3 = str(new_row3)
            row3 = row3.replace("[","")
            row3 = row3.replace("]","")
            row3 = row3.replace("'","")
            arcade_progress_list.append("\n")
            arcade_progress_list.append(str(i) + ": " + row3)
            i += 1
    arcade_progress_list = ''.join(arcade_progress_list)
    top_5_arcade = Label(leader_board_window, text = arcade_progress_list, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
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
    global SPANISH_MODULE_COMBOBOX
    if ARCADE_MODE_BOOL:
        if SPANISH_MODE_BOOL:
            connection_cursor.execute("SELECT ascore FROM LoginDetails WHERE username=?",(LOGIN_USERNAME,))
            past_score = connection_cursor.fetchone()
            if past_score[0] < SPANISH_LEARN_SCORE:
                connection.execute("UPDATE LoginDetails SET ascore = ? WHERE username = ?",(SPANISH_LEARN_SCORE,LOGIN_USERNAME,))
                connection.commit()
        else:
            connection_cursor.execute("SELECT ascore FROM LoginDetails WHERE username=?",(LOGIN_USERNAME,))
            past_score = connection_cursor.fetchone()
            if past_score[0] < GERMAN_LEARN_SCORE:
                connection.execute("UPDATE LoginDetails SET ascore = ? WHERE username = ?",(GERMAN_LEARN_SCORE,LOGIN_USERNAME,))
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
    module_german_continue_button.place(x=3000, y=3000)
    german_learn_button.place(x=410, y=200)
    spanish_zone_label.place(x=3000, y=3000)
    spanish_arcade_button.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)
    module_spanish_continue_button.place(x=3000, y=3000)
    german_zone_label.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)
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
    logout_button.place(x=225, y=550)
    spanish_continue_button.place(x=3000, y=3000)
    german_continue_button.place(x=3000, y=3000)
    try:
        GERMAN_MODULE_COMBOBOX.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        SPANISH_MODULE_COMBOBOX.place(x=3000, y=3000)
    except NameError:
        pass
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
    try:
        SPANISH_INCORRECT_ANSWER.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        GERMAN_INCORRECT_ANSWER.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        STREAK_LABEL.place(x=3000, y=3000)
    except NameError:
        pass


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
    global ADD_QUESTIONS_LABEL
    global VIEW_STUDENT_PROGRESS_LABEL
    global DONE_BACKUP_LABEL
    global RESET_PASSWORD_LABEL
    global DONE_RESET_LABEL
    global DELETE_USER_LABEL
    global DONE_ADD_QUESTIONS_LABEL
    global DONE_REMOVE_LABEL
    global DONE_QUESTIONS_LABEL
    global ID_MODULE_COMBOBOX
    global REMOVE_QUESTIONS_LABEL
    global RESTORE_BACKUP_LABEL
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 6
    help_storage()
    id_field.place(x=3000, y=3000)
    id_delete_field.place(x=3000, y=3000)
    reset_password_field.place(x=3000, y=3000)
    reset_password_button.place(x=3000, y=3000)
    back_teacher_button.place(x=3000, y=3000)
    submit_login_button.place(x=3000, y=3000)
    back_welcome_button.place(x=3000, y=3000)
    login_username_field.place(x=3000, y=3000)
    login_password_field.place(x=3000, y=3000)
    id_questions_field.place(x=3000, y=3000)
    remove_questions_continue_button.place(x=3000, y=3000)
    add_questions_field.place(x=3000, y=3000)
    add_questions_submit_button.place(x=3000, y=3000)
    add_questions_spanish_checkbutton.place(x=3000, y=3000)
    add_questions_german_checkbutton.place(x=3000, y=3000)
    username_password_label.place(x=3000, y=3000)
    slogo_label.place(x=3000, y=3000)
    logging_in_label.place(x=3000, y=3000)
    remove_user_button.place(x=3000, y=3000)
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
        ADD_QUESTIONS_LABEL.place(x=3000, y=3000)
        DONE_ADD_QUESTIONS_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
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
        DONE_REMOVE_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    try:
        REMOVE_QUESTIONS_LABEL.place(x=3000, y=3000)
        ID_MODULE_COMBOBOX.place(x=3000, y=3000)
        DONE_QUESTIONS_LABEL.place(x=3000, y=3000)
    except NameError:
        pass
    

def view_student_progress():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 7
    help_storage()
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
    view_student_progress_list = []
    new_row = [""] * 5
    view_student_progress_list.append("LIST OF STUDENTS\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nNAME  -  SPANISH PROGRESS  -  GERMAN PROGRESS  -  ARCADE SCORE\n")
    for row in connection.execute("SELECT id,username,teacher,admin,sprogress,gprogress,ascore FROM LoginDetails"):
        if row[2] == 1 or row[3] == 1:
            pass
        else:
            new_row[0] = str(row[0])
            new_row[1] = str(row[1])
            new_row[2] = str(row[4])
            new_row[3] = str(row[5])
            new_row[4] = str(row[6])
            row = str(new_row)
            row = row.replace("[","")
            row = row.replace("]","")
            row = row.replace("'","")
            view_student_progress_list.append("\n")
            view_student_progress_list.append(row)
    view_student_progress_list = ''.join(view_student_progress_list)
    VIEW_STUDENT_PROGRESS_LABEL = Label(main_gui, text = view_student_progress_list, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
    VIEW_STUDENT_PROGRESS_LABEL.place(x=10, y=110)
    

def change_password():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 8
    help_storage()
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
    RESET_PASSWORD_LABEL = Label(main_gui, text = reset_password_list, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
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


        for row in connection.execute("SELECT * FROM LoginDetails WHERE id = ?",(id_reset)):
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
            connection.execute("UPDATE LoginDetails SET password = ? WHERE id = ?",(reset_password,id_reset))
            connection.commit()
            done_reset_text = "Password has been reset."
            DONE_RESET_LABEL = Label(main_gui, text = done_reset_text, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
            DONE_RESET_LABEL.place(x=310, y=200)


def add_questions():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 9
    help_storage()
    global DELETE_USER_LABEL
    global ADD_QUESTIONS_LABEL
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
    add_questions_field.place(x=261, y=302)
    add_questions_spanish_checkbutton.place(x=429, y=300)
    add_questions_german_checkbutton.place(x=508, y=300)
    add_questions_list = "ADD QUESTIONS\n\nStep 1. Type the words in the text file that opened. The format is translated word then English\nversion. E.G: hola,hello,buenos dias,good day. Continue in this manner. Make sure that the words are\ncapitalized, as it will not make the file look nicer.\nStep 2. Save the file with all lower case and wherever there is a space use an underscore. E.G: spanish_basics1.\nStep 3. Type the name of the text file in the first field. Wherever there is an underscore change\nit back to a space and also capitalize the first letter of the words.\nStep 4. Check the relevant checkbox. If the language is spanish or german then check the right one.\nIf not simply type the name of the language. E.G: Latin\n\nName of question set    Spanish?    German?"
    ADD_QUESTIONS_LABEL = Label(main_gui, text =add_questions_list, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
    ADD_QUESTIONS_LABEL.place(x=20, y=110)
    add_questions_submit_button.place(x=550, y=300)
    subprocess.Popen(["notepad.exe"])


def submit_question_set():
    global ADD_QUESTIONS_LABEL
    global DONE_ADD_QUESTIONS_LABEL
    if add_questions_field.get() and ((spanish_module_add.get() and not german_module_add.get()) or (german_module_add.get() and not spanish_module_add.get())):
        name = add_questions_field.get()
        spanish = spanish_module_add.get()
        german = german_module_add.get()
        question_connection.execute("INSERT INTO QuestionSets(name,spanish,german) VALUES (?,?,?)",(name,spanish,german))
        question_connection.commit()
        done_add_questions_text = "QUESTIONS HAVE BEEN\nADDED"
        DONE_ADD_QUESTIONS_LABEL = Label(main_gui, text = done_add_questions_text, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
        DONE_ADD_QUESTIONS_LABEL.place(x=310, y=200)
        ADD_QUESTIONS_LABEL.place(x=3000, y=3000)
        add_questions_submit_button.place(x=3000, y=3000)
        add_questions_field.place(x=3000, y=3000)
        add_questions_spanish_checkbutton.place(x=3000, y=3000)
        add_questions_german_checkbutton.place(x=3000, y=3000)
    

def remove_questions():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 10
    help_storage()
    global ID_MODULE_COMBOBOX
    global REMOVE_QUESTIONS_LABEL
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
    remove_questions_list = "REMOVE QUESTIONS\n\nStep 1. Look at the corresponding ID in the drop down box.\nStep 2. Enter the ID below then click remove.\n\n\n\nID:"
    REMOVE_QUESTIONS_LABEL = Label(main_gui, text = remove_questions_list, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
    REMOVE_QUESTIONS_LABEL.place(x=190, y=110)
    id_questions_field.place(x=340, y=245)
    create_id_combo_box()
    ID_MODULE_COMBOBOX.place(x=200, y=300)
    remove_questions_continue_button.place(x=500, y=240)


def remove_questions_process():
    if id_questions_field.get():
        id_entered = id_questions_field.get()
        id_questions_field.delete(0, END)
        temp = ()
        for row in question_connection.execute("SELECT * FROM QuestionSets WHERE id = ?",(id_entered,)):
            temp += row
        temp_check = temp
        temp = str(temp)
        if temp == "()":
            pass
        else:
            global ID_MODULE_COMBOBOX
            global REMOVE_QUESTIONS_LABEL
            global DONE_QUESTIONS_LABEL
            question_connection.execute("DELETE FROM QuestionSets WHERE id = (?)",(id_entered,))
            question_connection.commit()
            REMOVE_QUESTIONS_LABEL.place(x=3000, y=3000)
            id_questions_field.place(x=3000, y=3000)
            ID_MODULE_COMBOBOX.place(x=3000, y=3000)
            remove_questions_continue_button.place(x=3000, y=3000)
            done_questions_text = "QUESTION SET\nHAS BEEN REMOVED"
            DONE_QUESTIONS_LABEL = Label(main_gui, text = done_questions_text, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
            DONE_QUESTIONS_LABEL.place(x=310, y=200) 


def delete_user():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 11
    help_storage()
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
    delete_user_list = "DELETE USER\n\nStep 1: Go back to the view list of students and get the id of the student to remove.\nStep 2: Go back here and enter the id.\nStep 3: Click finalize and the user will be deleted.\n"
    DELETE_USER_LABEL = Label(main_gui, text = delete_user_list, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
    DELETE_USER_LABEL.place(x=100, y=110)
    id_delete_field.place(x=237, y=230)
    remove_user_button.place(x=375, y=230)


def remove_user_process():
    global DONE_REMOVE_LABEL
    global DELETE_USER_LABEL
    if id_field.get():
        id_reset = id_field.get()
        id_field.delete(0, END)
        temp = ()
        for row in connection.execute("SELECT * FROM LoginDetails WHERE id = ?",(id_reset,)):
            temp += row
        temp_check = temp
        temp = str(temp)
        if temp == "()":
            pass
        else:
            DELETE_USER_LABEL.place(x=3000, y=3000)
            id_field.place(x=3000, y=3000)
            remove_user_button.place(x=3000, y=3000)
            reset_password_field.place(x=3000, y=3000)
            reset_password_button.place(x=3000, y=3000)
            connection.execute("DELETE FROM LoginDetails WHERE id = ?",(id_reset,))
            connection.commit()
            done_remove_text = "USER HAS BEEN\nREMOVED"
            DONE_REMOVE_LABEL = Label(main_gui, text = done_remove_text, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
            DONE_REMOVE_LABEL.place(x=310, y=200) 


def save_backup():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 12
    help_storage()
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
    DONE_BACKUP_LABEL = Label(main_gui, text = done_backup_text, font=("Lucida Sans", 10, "bold"), bd = 3, bg = "orange", fg = "white")
    DONE_BACKUP_LABEL.place(x=340, y=200)
    backup_directory = os.path.dirname(sys.argv[0])
    directory = backup_directory
    directory += '/'
    backup_directory += '/backup/'
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    backup_directory += date
    perform_backup(backup_directory,directory)


def restore_backup():
    global HELP_SECTION_TRACKER
    HELP_SECTION_TRACKER = 13
    help_storage()
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
    current_directory = os.path.dirname(sys.argv[0])
    directory = str(current_directory)
    os.startfile(directory)
    help_directory = directory + "\\restore_backup_help.txt"
    os.startfile(help_directory)
    backup_directory = directory + "\\backup"
    os.startfile(backup_directory)
    quit_function()
    exit()
    
#######################
# SQLite3 connections #
#######################

if os.path.isfile('login_details.db') == False:
    create()

if os.path.isfile('question_sets.db') == False:
    create1()

connection = sqlite3.connect('login_details.db')
connection_cursor = connection.cursor()

question_connection = sqlite3.connect('question_sets.db')
question_connection_cursor = question_connection.cursor()

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

id_delete_field = Entry(main_gui)
id_delete_field.place(x=3000, y=3000)

id_questions_field = Entry(main_gui)
id_questions_field.place(x=3000, y=3000)

reset_password_field = Entry(main_gui)
reset_password_field.place(x=3000, y=3000)

add_questions_field = Entry(main_gui)
add_questions_field.place(x=3000, y=3000)

spanish_module_add = IntVar()
add_questions_spanish_checkbutton = Checkbutton(main_gui, variable=spanish_module_add, bg="orange")
add_questions_spanish_checkbutton.place(x=3000, y=3000)

german_module_add = IntVar()
add_questions_german_checkbutton = Checkbutton(main_gui, variable=german_module_add, bg="orange")
add_questions_german_checkbutton.place(x=3000, y=3000)

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

spanish_learn_mode_button = Button(main_gui, text="LEARN MODE", command=spanish_learn_mode, bg="white", width="12", height="3")
spanish_learn_mode_button.config(font=("Lucida Sans", 10, "bold"))
spanish_learn_mode_button.place(x=3000, y=3000)
spanish_learn_mode_button.flash()

spanish_arcade_button = Button(main_gui, text="ARCADE MODE", command=spanish_arcade, bg="white", width="14", height="3")
spanish_arcade_button.config(font=("Lucida Sans", 10, "bold"))
spanish_arcade_button.place(x=3000, y=3000)
spanish_arcade_button.flash()

german_learn_mode_button = Button(main_gui, text="LEARN MODE", command=german_learn_mode, bg="white", width="12", height="3")
german_learn_mode_button.config(font=("Lucida Sans", 10, "bold"))
german_learn_mode_button.place(x=3000, y=3000)
german_learn_mode_button.flash()

german_arcade_button = Button(main_gui, text="ARCADE MODE", command=german_arcade, bg="white", width="14", height="3")
german_arcade_button.config(font=("Lucida Sans", 10, "bold"))
german_arcade_button.place(x=3000, y=3000)
german_arcade_button.flash()

spanish_arcade_start_button = Button(main_gui, text="START", command=spanish_arcade_mode, bg="white", width="7", height="2")
spanish_arcade_start_button.config(font=("Lucida Sans", 10, "bold"))
spanish_arcade_start_button.place(x=3000, y=3000)
spanish_arcade_start_button.flash()

german_arcade_start_button = Button(main_gui, text="START", command=german_arcade_mode, bg="white", width="7", height="2")
german_arcade_start_button.config(font=("Lucida Sans", 10, "bold"))
german_arcade_start_button.place(x=3000, y=3000)
german_arcade_start_button.flash()

leader_board_button = Button(main_gui, text="LEADER-BOARD", command=leader_board, bg="white", width="13", height="1")
leader_board_button.config(font=("Lucida Sans", 8, "bold"))
leader_board_button.place(x=3000, y=3000)
leader_board_button.flash()

logout_button = Button(main_gui, text="LOGOUT", command=logout, bg="white", width="8", height="1")
logout_button.config(font=("Lucida Sans", 8, "bold"))
logout_button.place(x=3000, y=3000)
logout_button.flash()

spanish_continue_button = Button(main_gui, text="CONTINUE", command=spanish_learn_mode, bg="white", width="9", height="2")
spanish_continue_button.config(font=("Lucida Sans", 8, "bold"))
spanish_continue_button.place(x=3000, y=3000)
spanish_continue_button.flash()

german_continue_button = Button(main_gui, text="CONTINUE", command=german_learn_mode, bg="white", width="9", height="2")
german_continue_button.config(font=("Lucida Sans", 8, "bold"))
german_continue_button.place(x=3000, y=3000)
german_continue_button.flash()

remove_questions_continue_button = Button(main_gui, text="CONTINUE", command=remove_questions_process, bg="white", width="9", height="2")
remove_questions_continue_button.config(font=("Lucida Sans", 8, "bold"))
remove_questions_continue_button.place(x=3000, y=3000)
remove_questions_continue_button.flash()

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

upside_down_question_mark_button = Button(main_gui, text="¿", command=upside_down_question_mark, bg="white", width="2", height="1")
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

spanish_submit_button = Button(main_gui, text="SUBMIT", command=spanish_learn_process, bg="white", width="9", height="2")
spanish_submit_button.config(font=("Lucida Sans", 8, "bold"))
spanish_submit_button.place(x=3000, y=3000)
spanish_submit_button.flash()

german_submit_button = Button(main_gui, text="SUBMIT", command=german_learn_process, bg="white", width="9", height="2")
german_submit_button.config(font=("Lucida Sans", 8, "bold"))
german_submit_button.place(x=3000, y=3000)
german_submit_button.flash()

view_student_progress_button = Button(main_gui, text="LIST OF\nPROGRESS", command=view_student_progress, bg="white", width="12", height="3")
view_student_progress_button.config(font=("Lucida Sans", 8, "bold"))
view_student_progress_button.place(x=3000, y=3000)
view_student_progress_button.flash()

change_password_button = Button(main_gui, text="CHANGE\nPASSWORD", command=change_password, bg="white", width="12", height="3")
change_password_button.config(font=("Lucida Sans", 8, "bold"))
change_password_button.place(x=3000, y=3000)
change_password_button.flash()

add_questions_button = Button(main_gui, text="ADD\nQUESTIONS", command=add_questions, bg="white", width="12", height="3")
add_questions_button.config(font=("Lucida Sans", 8, "bold"))
add_questions_button.place(x=3000, y=3000)
add_questions_button.flash()

remove_questions_button = Button(main_gui, text="REMOVE\nQUESTIONS", command=remove_questions, bg="white", width="12", height="3")
remove_questions_button.config(font=("Lucida Sans", 8, "bold"))
remove_questions_button.place(x=3000, y=3000)
remove_questions_button.flash()

delete_user_button = Button(main_gui, text="DELETE\nUSER", command=delete_user, bg="white", width="12", height="3")
delete_user_button.config(font=("Lucida Sans", 8, "bold"))
delete_user_button.place(x=3000, y=3000)
delete_user_button.flash()

save_backup_button = Button(main_gui, text="SAVE\nBACKUP", command=save_backup, bg="white", width="12", height="3")
save_backup_button.config(font=("Lucida Sans", 8, "bold"))
save_backup_button.place(x=3000, y=3000)
save_backup_button.flash()

restore_backup_button = Button(main_gui, text="RESTORE\nBACKUP", command=restore_backup, bg="white", width="12", height="3")
restore_backup_button.config(font=("Lucida Sans", 8, "bold"))
restore_backup_button.place(x=3000, y=3000)
restore_backup_button.flash()

reset_password_button = Button(main_gui, text="RESET", command=reset_password_process, bg="white", width="7", height="2")
reset_password_button.config(font=("Lucida Sans", 8, "bold"))
reset_password_button.place(x=3000, y=3000)
reset_password_button.flash()

remove_user_button = Button(main_gui, text="REMOVE\nUSER", command=remove_user_process, bg="white", width="7", height="2")
remove_user_button.config(font=("Lucida Sans", 8, "bold"))
remove_user_button.place(x=3000, y=3000)
remove_user_button.flash()

module_german_continue_button = Button(main_gui, text="CONTINUE", command=german_module_selected, bg="white", width="9", height="2")
module_german_continue_button.config(font=("Lucida Sans", 8, "bold"))
module_german_continue_button.place(x=3000, y=3000)
module_german_continue_button.flash()

module_spanish_continue_button = Button(main_gui, text="CONTINUE", command=spanish_module_selected, bg="white", width="9", height="2")
module_spanish_continue_button.config(font=("Lucida Sans", 8, "bold"))
module_spanish_continue_button.place(x=3000, y=3000)
module_spanish_continue_button.flash()

add_questions_submit_button = Button(main_gui, text="CONTINUE", command=submit_question_set, bg="white", width="9", height="2")
add_questions_submit_button.config(font=("Lucida Sans", 8, "bold"))
add_questions_submit_button.place(x=3000, y=3000)
add_questions_submit_button.flash()

############################
# Initialising the Program #
############################

main_window()
main_gui.mainloop()
