#####################################
# Memrize Learning Languages System #
# --------------------------------- #
#      By Ethan Champion 13RKS      #
#       Made in Python 3.6.3.       #
#    Variable Style: Underscores    #
#####################################

# This is the main learn program which uses several other sub-programs

#############
# Libraries #
#############

# To import all of the basic Tkinter GUI Elements
from tkinter import *
# To import the more advanced Tkinter GUI Elements through TTK
from tkinter import ttk
# Imports SQLite3 to interact with databases through Python - Imports Connection Module
from sqlite3 import connect
# Imports random for the RandInt module to randomly select an integer
from random import randint
# Import the OS library to deal with files outside my program
import os
# Import the hashing algorithm library
from hashlib import sha512

#######################
# Leader Board System #
#######################


# Simple procedure to quit the leader board
def close_leader_board():
    # Import the leader board open bool
    global LEADER_BOARD_OPEN_BOOL
    # Set the leader board to closed
    LEADER_BOARD_OPEN_BOOL = False
    # Displace the leader board till the user wants to open it again
    leader_board_window.geometry("300x600+3000+3000")
    # Place the button to recall the leader board in the main screen
    leader_board_button.place(x=460, y=550)


# Procedure to refresh the leader board
def leader_board_refresh():
    # Import the leader board open bool
    global LEADER_BOARD_OPEN_BOOL
    # Simple Error Bypass
    try:
        # If the leader board is open
        if LEADER_BOARD_OPEN_BOOL:
            # Call the leader board function which acts as a refresh
            leader_board()
    # If the leader board boolean has not been defined yet
    except NameError:
        # Move on
        pass


# Main Leader board function
def leader_board():
    # Import the leader board open boolean
    global LEADER_BOARD_OPEN_BOOL
    # Set the leader board status to open
    LEADER_BOARD_OPEN_BOOL = True
    # Move the leader board on screen with padding in the y axis to ensure that there is no overlap in windows
    leader_board_window.geometry("800x200+2+603")
    # Create a close button on the leader board which calls close leader board procedure
    close_board = Button(leader_board_window, text="CLOSE", command=close_leader_board, bg="white", width="6",
                         height="1")
    # Add some settings to the button
    close_board.config(font=("Lucida Sans", 8, "bold"))
    # Place on screen 
    close_board.place(x=735, y=10)
    # Place the leader board information on screen
    leader_board_label.place(x=280, y=10)
    # Move the leader board button out of the way so that only one window can be opened at a time
    leader_board_button.place(x=3000, y=3000)
    # Create a Spanish progress array
    spanish_progress_list = []
    # Define a count variable
    i = 1
    # Create an array with two string variables
    new_row1 = [""] * 2
    # Add to the Spanish progress array the top line
    spanish_progress_list.append("SPANISH LEADER BOARD\n----------------------------------")
    # For item in the database, order by Spanish progress going in descending order for the first 5 people
    for row1 in connection.execute("SELECT username,teacher,admin,sprogress FROM LoginDetails ORDER BY sprogress "
                                   "DESC LIMIT 5"):
        # If the person is an Admin or a teacher
        if row1[1] == 1 or row1[2] == 1:
            # Move on
            pass
        # If the person is a student
        else:
            # Add the name of the student to the array
            new_row1[0] = row1[0]
            # Add the score of the student to the array
            new_row1[1] = str(row1[3])
            # Convert the array into a string
            row1 = str(new_row1)
            # Replace all unnecessary formatting symbols to nothing
            row1 = row1.replace("[", "")
            row1 = row1.replace("]", "")
            row1 = row1.replace("'", "")
            # Add a new line to the list
            spanish_progress_list.append("\n")
            # Add a count variable to the list i.e: 1. Ethan 20
            spanish_progress_list.append(str(i) + ": " + row1)
            # Increment the count variable
            i += 1
    # Join the list together
    spanish_progress_list = ''.join(spanish_progress_list)
    # Create a label for all the information gathered
    top_5_spanish = Label(leader_board_window, text=spanish_progress_list, font=("Lucida Sans", 10, "bold"), bd=3,
                          bg="orange", fg="white")
    # Place in the left middle of leader board
    top_5_spanish.place(x=50, y=70)
    # Create a German progress array
    german_progress_list = []
    # Set the counter back to 0
    i = 1
    # Create a new array with two string variables
    new_row2 = [""] * 2
    # Add a title to the German progress array
    german_progress_list.append("GERMAN LEADER BOARD\n-----------------------------------")
    # For item in the database ordered by their German progress in descending order with maximum 5 users
    for row2 in connection.execute("SELECT username,teacher,admin,gprogress FROM LoginDetails ORDER BY gprogress "
                                   "DESC LIMIT 5"):
        # If they are a teacher or an admin
        if row2[1] == 1 or row2[2] == 1:
            # Move on
            pass
        # If they are a student
        else:
            # Add their name to the array
            new_row2[0] = row2[0]
            # Add their score to the array
            new_row2[1] = str(row2[3])
            # Convert the array to a string
            row2 = str(new_row2)
            # Replace all unnecessary formatting symbols to nothing
            row2 = row2.replace("[", "")
            row2 = row2.replace("]", "")
            row2 = row2.replace("'", "")
            # Add a new line to the list
            german_progress_list.append("\n")
            # Add the count variable to the list i.e: 2. Bob 40
            german_progress_list.append(str(i) + ": " + row2)
            # Increment the count variable
            i += 1
    # Join the list together
    german_progress_list = ''.join(german_progress_list)
    # Create a label for the German leader board
    top_5_german = Label(leader_board_window, text=german_progress_list, font=("Lucida Sans", 10, "bold"), bd=3,
                         bg="orange", fg="white")
    # Place in middle of leader board
    top_5_german.place(x=310, y=70)
    # Create an Arcade progress array
    arcade_progress_list = []
    # Set the counter variable back to 1
    i = 1
    # Create an empty string array with two spaces
    new_row3 = [""] * 2
    # Add a title to the list
    arcade_progress_list.append("ARCADE LEADER BOARD\n-----------------------------------")
    # For item in database ordered by their arcade score in descending order with maximum five users
    for row3 in connection.execute("SELECT username,teacher,admin,ascore FROM LoginDetails ORDER BY ascore"
                                   " DESC LIMIT 5"):
        # If they are a teacher or an admin
        if row3[1] == 1 or row3[2] == 1:
            # Move on
            pass
        # If they are a student
        else:
            # Add their name to the array
            new_row3[0] = row3[0]
            # Add their arcade score
            new_row3[1] = str(row3[3])
            # Convert the array to a string
            row3 = str(new_row3)
            # Remove any formatting symbols for lack of a better method by replacing them with nothing
            row3 = row3.replace("[", "")
            row3 = row3.replace("]", "")
            row3 = row3.replace("'", "")
            # Add a new line to the list
            arcade_progress_list.append("\n")
            # Set a count variable i.e: 3. Phil 50
            arcade_progress_list.append(str(i) + ": " + row3)
            # Increment the counter variable
            i += 1
    # Join the list together
    arcade_progress_list = ''.join(arcade_progress_list)
    # Create a label with text inside
    top_5_arcade = Label(leader_board_window, text=arcade_progress_list, font=("Lucida Sans", 10, "bold"), bd=3,
                         bg="orange", fg="white")
    # Place on the right middle of the screen
    top_5_arcade.place(x=570, y=70)

################
# Login System #
################


# This is the function to display the register screen if the user clicks register
def initial_register():
    # Import the global tracker variable
    global HELP_SECTION_TRACKER
    # Set it to the first screen
    HELP_SECTION_TRACKER = 1
    # Call the help function
    help_storage()
    # Move labels and that are not needed out of the way for now
    username_taken_label.place(x=3000, y=3000)
    register_button.place(x=3000, y=3000)
    login_button.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    # Place the back button on screen so that they can return to the main menu
    back_welcome_button.place(x=299, y=550)
    # Place the username and password fields on screen so that they can enter their new username and passwords
    new_username_field.place(x=237, y=220)
    new_password_field.place(x=430, y=220)
    # Place the label to explain what the user has to do
    username_password_label.place(x=200, y=150)
    # Place the button to continue once they have typed in their username and passwords
    submit_register_button.place(x=365, y=220)
    # Bind the enter key to calling the function as an alternative to the button
    main_gui.bind('<Return>', submit_register_process)


# A bypass function due to the .bind function passing a variable and buttons not doing so
def submit_register_process(key):
    # Call the function without the key variable passed
    submit_register()


# The submit register procedure
def submit_register():
    # A check if both of the fields have something inside
    if new_username_field.get() and new_password_field.get():
        # Displace labels that may be on screen which are not of use
        registered_label.place(x=3000, y=3000)
        username_taken_label.place(x=3000, y=3000)
        username_length_label.place(x=3000, y=3000)
        password_error_label.place(x=3000, y=3000)
        # Set variables as the words inputted into the fields
        new_username = new_username_field.get()
        new_password = new_password_field.get()
        # Delete the fields from the start to the end in case something goes wrong and they have to re-input
        new_username_field.delete(0, END)
        new_password_field.delete(0, END)
        # Set the hashing algorithm to sha512 which is very secure
        current_hash = sha512()
        # Create a hash with the new password encoded in utf-8 which converts it to a byte list of characters
        current_hash.update(new_password.encode('utf-8'))
        # Set a variable to the hex digest of that long list of bytes
        password_hash = current_hash.hexdigest()
        # A temporary array for the procedure
        temp = [""]
        # For row in the database where the username is the same as the inputted one
        for row in connection.execute("SELECT * FROM LoginDetails WHERE username = ?", (new_username,)):
            # Add it to the temporary array
            temp = row
        # If the first item is empty, i.e: nothing was found in the database so the username is not taken
        if temp[0] == "":
            # Next, if the username is less than 3 characters or more than 10
            if len(new_username) < 3 or len(new_username) > 10:
                # Display an error as the username length may affect aspects of the program
                username_length_label.place(x=100, y=265)
            # Or if the length of the password is less than 5
            elif len(new_password) < 5:
                # Display an error as it is not secure
                password_error_label.place(x=70, y=265)
            # Or if the password has no capital letters
            elif new_password == new_password.lower():
                # Then display an error as it is not secure
                password_error_label.place(x=70, y=265)
            # If all of these pass
            else:
                # Display a message that the user has been logged in, from there the user can go back and log in
                registered_label.place(x=190, y=265)
                # Insert into the database the new username and password with all the default fields
                connection.execute("INSERT INTO LoginDetails(username,password,teacher,admin,sprogress,gprogress,"
                                   "ascore) VALUES (?,?,0,0,0,0,0)", (new_username, password_hash,))
                # Commit the changes to the database so that it is saved forever
                connection.commit()
        # If the username was taken
        else:
            # Display the username taken error message
            username_taken_label.place(x=190, y=265)


# This is the function to display the login screen once the user clicks the login button
def initial_login():
    # Import the global section tracker
    global HELP_SECTION_TRACKER
    # Set it to the second screen
    HELP_SECTION_TRACKER = 2
    # Call the function to display the help message if the window is open
    help_storage()
    # Places labels and buttons that are not necessary off of the screen temporarily
    login_button.place(x=3000, y=3000)
    register_button.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    # Places the submit button
    submit_login_button.place(x=365, y=220)
    # Places the back button on screen so that the user can return to the main menu
    back_welcome_button.place(x=299, y=550)
    # Places the login fields for the user to type in their username and password
    login_username_field.place(x=237, y=220)
    login_password_field.place(x=430, y=220)
    # Places the label to show them what they should do
    username_password_label.place(x=200, y=150)
    # Binds the enter key to calling submit login
    main_gui.bind('<Return>', submit_login_process)


# This is a bypass for the binding function, as it returns a key so this bypasses this
def submit_login_process(key):
    # Calls the login function
    submit_login()


# This is the login procedure
def submit_login():
    # Global login details defined
    global LOGIN_USERNAME
    global LOGIN_PASSWORD
    # Global progress variables defined
    global SPROGRESS
    global GPROGRESS
    # If both of the fields have words inside
    if login_username_field.get() and login_password_field.get():
        # This sets the global variables to the inputted username and password
        LOGIN_USERNAME = login_username_field.get()
        LOGIN_PASSWORD = login_password_field.get()
        # This clears the two fields in case there are any error messages
        login_password_field.delete(0, END)
        login_username_field.delete(0, END)
        # Sets the hashing algorithm to sha512 which is very secure
        current_hash = sha512()
        # Hash their login password and turn it into byte format with encode utf-8
        current_hash.update(LOGIN_PASSWORD.encode('utf-8'))
        # Set the password hash to the newly created hash
        password_hash = current_hash.hexdigest()
        # Creates a temporary array for later use
        temp = ()
        # For row in the database where the username and password are the same as the ones inputted
        for row in connection.execute("SELECT * FROM LoginDetails WHERE username = ? AND password = ?",
                                      (LOGIN_USERNAME, password_hash)):
            # Add each item to the array
            temp += row
        # Create a check variable which will remain an array
        temp_check = temp
        # Converts the old variable to a string
        temp = str(temp)
        # Checks if the array was empty i.e: If the login details were incorrect
        if temp == "()":
            # Move unnecessary labels out of the way
            logging_in_label.place(x=3000, y=3000)
            # Display an error message
            login_error_label.place(x=190, y=265)
        # Or if the array's teacher field was true
        elif temp_check[3] == 1:
            # Calls the teacher system as they are a teacher
            teacher_system()
        # Or if the array's admin field is true
        elif temp_check[4] == 1:
            # Call the admin system
            admin_system()
        # If they are a student 
        else:
            # Set their progress to a string
            SPROGRESS = ""
            # Get the Spanish progress of the student
            for row in connection.execute("SELECT sprogress FROM LoginDetails WHERE username = ? AND password = ?",
                                          (LOGIN_USERNAME, password_hash)):
                # Set the variable to the progress
                SPROGRESS = row
            # Set the other global variable to string
            GPROGRESS = ""
            # Get the German progress of the student
            for row in connection.execute("SELECT gprogress FROM LoginDetails WHERE username = ? AND password = ?",
                                          (LOGIN_USERNAME, password_hash)):
                # Set the variable to the progress
                GPROGRESS = row
            # Set the variables to the first item due to an SQLite3 formatting problem
            SPROGRESS = SPROGRESS[0]
            GPROGRESS = GPROGRESS[0]
            # Place error messages off screen in case they originally got login details wrong
            login_error_label.place(x=3000, y=3000)
            # Place the logging in label to inform the user that they have got their password right
            logging_in_label.place(x=190, y=265)
            # Call the login system function
            login_system()


# Simple procedure to create a Spanish question set combobox
def create_spanish_combo_box():
    # Define a new global variable
    global SPANISH_MODULE_COMBOBOX
    # Create a temporary empty array
    spanish_question_sets = []
    # For item in the question set database
    for item in question_connection.execute("SELECT * FROM QuestionSets"):
        # If the item is Spanish
        if item[2] == 1:
            # Add to the array the name of it
            spanish_question_sets.append(item[1])
    # Set the default option to a Tkinter String Variable in the main window
    spanish_module_default = StringVar(main_gui)
    # Simple Error Bypass
    try:
        # Sets the default to the first question set
        spanish_module_default.set(spanish_question_sets[0])
    # If there are no question sets
    except IndexError:
        # Set the default to none found
        spanish_module_default.set("No Spanish question sets found.")
    # Creates a global combobox with default value and other values inside
    SPANISH_MODULE_COMBOBOX = ttk.Combobox(main_gui, textvariable=spanish_module_default, values=spanish_question_sets,
                                           width=60)
    # Set the state to read only to avoid user's typing into box
    SPANISH_MODULE_COMBOBOX.state(['readonly'])
    # Move out of the way for now
    SPANISH_MODULE_COMBOBOX.place(x=3000, y=3000)


# Simple procedure to create a German question set combobox
def create_german_combo_box():
    # Define a new global variable
    global GERMAN_MODULE_COMBOBOX
    # Create a temporary array
    german_question_sets = []
    # For item in the question set database
    for item in question_connection.execute("SELECT * FROM QuestionSets"):
        # If the German field is true
        if item[3] == 1:
            # Add to the array the name of the question set
            german_question_sets.append(item[1])
    # Create a Tkinter string variable in the main window
    german_module_default = StringVar(main_gui)
    # Simple Error Bypass
    try:
        # Set the default to the first value
        german_module_default.set(german_question_sets[0])
    # If there are no values
    except IndexError:
        # Set the default to no questions found
        german_module_default.set("No question sets found.")
    # Creates a global combobox with default value and other values inside
    GERMAN_MODULE_COMBOBOX = ttk.Combobox(main_gui, textvariable=german_module_default, values=german_question_sets,
                                          width=60)
    # Set the state to read only
    GERMAN_MODULE_COMBOBOX.state(['readonly'])
    # Place it out of the way for now
    GERMAN_MODULE_COMBOBOX.place(x=3000, y=3000)


# Simple procedure to create an ID combobox for the teachers
def create_id_combo_box():
    # Define a new global variable
    global ID_MODULE_COMBOBOX
    # Create an empty array
    id_question_sets = []
    # For item in the database
    for item in question_connection.execute("SELECT * FROM QuestionSets"):
        # Add to the array their ID and name
        temp_array = [item[0], item[1]]
        # Add to the array
        id_question_sets.append(temp_array)
    # Create a Tkinter string variable in the main gui
    id_module_default = StringVar(main_gui)
    # Simple bypass error
    try:
        # Try setting the default value to the first one
        id_module_default.set(id_question_sets[0])
    # If there is no items in database
    except IndexError:
        # Set default to null
        id_module_default.set("No question sets found.")
    # Create a new combobox with text and values previously defined
    ID_MODULE_COMBOBOX = ttk.Combobox(main_gui, textvariable=id_module_default, values=id_question_sets, width=60)
    # Set the state to read only
    ID_MODULE_COMBOBOX.state(['readonly'])
    # Place off screen for now
    ID_MODULE_COMBOBOX.place(x=3000, y=3000)


# This is the main menu function which is called initially and when logging out
def main_window():
    # Imports the combobox's so that the program can move them
    global SPANISH_MODULE_COMBOBOX
    global GERMAN_MODULE_COMBOBOX
    global ID_MODULE_COMBOBOX
    # Imports the help section tracker
    global HELP_SECTION_TRACKER
    # Imports the booleans which narrows down where in the program they have been as an optimisation
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    # Defines where in the program they are for the help section procedure
    HELP_SECTION_TRACKER = 0
    # Calls the procedure
    help_storage()
    # Sets the global tracker variables
    ARCADE_MODE_BOOL = False
    SPANISH_MODE_BOOL = False
    # Puts the slogo on top in the middle
    slogo_label.place(x=205, y=10)
    # Moves the login button on screen
    login_button.place(x=410, y=220)
    # Moves the register button on screen
    register_button.place(x=300, y=220)
    # Puts the initial choice label on screen
    initial_choice_label.place(x=300, y=150)
    # Moves all the unnecessary labels, buttons and fields out of the screen
    logout_button.place(x=3000, y=3000)
    registered_label.place(x=3000, y=3000)
    logging_in_label.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    back_learn_button.place(x=3000, y=3000)
    german_zone_label.place(x=3000, y=3000)
    new_username_field.place(x=3000, y=3000)
    new_password_field.place(x=3000, y=3000)
    welcome_back_label.place(x=3000, y=3000)
    spanish_zone_label.place(x=3000, y=3000)
    remove_user_button.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    back_teacher_button.place(x=3000, y=3000)
    german_learn_button.place(x=3000, y=3000)
    leader_board_button.place(x=3000, y=3000)
    spanish_learn_entry.place(x=3000, y=3000)
    submit_login_button.place(x=3000, y=3000)
    add_questions_field.place(x=3000, y=3000)
    back_welcome_button.place(x=3000, y=3000)
    reset_password_field.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    login_username_field.place(x=3000, y=3000)
    login_password_field.place(x=3000, y=3000)
    spanish_learn_button.place(x=3000, y=3000)
    password_error_label.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    username_length_label.place(x=3000, y=3000)
    teacher_section_label.place(x=3000, y=3000)
    spanish_arcade_button.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    reset_password_button.place(x=3000, y=3000)
    submit_register_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    username_password_label.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)
    german_arcade_start_button.place(x=3000, y=3000)
    spanish_arcade_start_button.place(x=3000, y=3000)
    view_student_progress_button.place(x=3000, y=3000)
    module_german_continue_button.place(x=3000, y=3000)
    module_spanish_continue_button.place(x=3000, y=3000)
    # First Bypass
    try:
        # If the German module combobox has been defined then move it
        GERMAN_MODULE_COMBOBOX.place(x=3000, y=3000)
    # If it is not defined
    except NameError:
        # Move on
        pass
    # Second Bypass
    try:
        # If the Spanish module combobox has been defined then move it
        SPANISH_MODULE_COMBOBOX.place(x=3000, y=3000)
    # If it is not defined yet
    except NameError:
        # Move on
        pass
    
################
# Login System #
################


# This is the login system function for when they have logged in
def login_system():
    # Imports the help section tracker global variable
    global HELP_SECTION_TRACKER
    # Sets the screen to the third
    HELP_SECTION_TRACKER = 3
    # Calls the function
    help_storage()
    # Places the log out button which calls the main menu function on click
    logout_button.place(x=225, y=550)
    # Places the welcome back label in top middle
    welcome_back_label.place(x=205, y=10)
    # Places the German learn button
    german_learn_button.place(x=410, y=200)
    # Places the leader board button in the bottom
    leader_board_button.place(x=460, y=550)
    # Places the Spanish learn button
    spanish_learn_button.place(x=300, y=200)
    # Places buttons and fields not needed out of the way
    slogo_label.place(x=3000, y=3000)
    logging_in_label.place(x=3000, y=3000)
    submit_login_button.place(x=3000, y=3000)
    back_welcome_button.place(x=3000, y=3000)
    login_password_field.place(x=3000, y=3000)
    login_username_field.place(x=3000, y=3000)
    username_password_label.place(x=3000, y=3000)


# Procedure to display combobox for when user clicks Spanish
def spanish_modules():
    # Create the Spanish combobox
    create_spanish_combo_box()
    # Import the combobox variable
    global SPANISH_MODULE_COMBOBOX
    # Import the help section tracker
    global HELP_SECTION_TRACKER
    # Set the screen to the fourth
    HELP_SECTION_TRACKER = 4
    # Call the help section tracker in case window is open
    help_storage()
    # Move the back button on screen in case they want to return
    back_learn_button.place(x=299, y=550)
    # Move the Spanish combobox previously created to the middle
    SPANISH_MODULE_COMBOBOX.place(x=220, y=200)
    # Move the Spanish zone label to the top to show the user where they are
    spanish_zone_label.place(x=205, y=10)
    # Move the continue button on screen for when they select a module
    module_spanish_continue_button.place(x=620, y=200)
    # Move unnecessary items out of the way
    welcome_back_label.place(x=3000, y=3000)
    spanish_learn_button.place(x=3000, y=3000)
    german_learn_button.place(x=3000, y=3000)


# Function for when a Spanish module is selected
def spanish_module_selected():
    # Import the global Spanish Combobox
    global SPANISH_MODULE_COMBOBOX
    # Define a new global variable
    global SPANISH_MODULE
    # Import the current path
    global DIRECTORY
    # If the combobox has a question set selected
    if SPANISH_MODULE_COMBOBOX.get():
        # Set the previously defined variable to the item selected
        SPANISH_MODULE = SPANISH_MODULE_COMBOBOX.get()
        # Change all spaces to underscores and make it all lowercase
        SPANISH_MODULE = SPANISH_MODULE.replace(" ", "_").lower()
        # Add a file extension to the end for when finding the file
        SPANISH_MODULE += ".txt"
        # Bypass a back slash error
        SPANISH_MODULE = DIRECTORY + r"\questions\\" + SPANISH_MODULE
        # Call the Spanish Learn function
        spanish_learn()


# Special characters in the Spanish alphabet
def o_accent():
    # Whenever it is called add the special character on the end
    spanish_learn_entry.insert(END, "ó")


# Special characters in the Spanish alphabet
def i_accent():
    # Whenever it is called add the special character on the end
    spanish_learn_entry.insert(END, "í")


# Special characters in the Spanish alphabet
def e_accent():
    # Whenever it is called add the special character on the end
    spanish_learn_entry.insert(END, "é")


# Special characters in the Spanish alphabet
def a_accent():
    # Whenever it is called add the special character on the end
    spanish_learn_entry.insert(END, "á")


# Special characters in the Spanish alphabet
def u_accent():
    # Whenever it is called add the special character on the end
    spanish_learn_entry.insert(END, "ú")


# Special characters in the Spanish alphabet
def n_accent():
    # Whenever it is called add the special character on the end
    spanish_learn_entry.insert(END, "ñ")


# Special characters in the German alphabet
def scharfes():
    # Whenever it is called add the special character on the end
    german_learn_entry.insert(END, "ß")


# Special characters in the German alphabet
def u_umlaut():
    # Whenever it is called add the special character on the end
    german_learn_entry.insert(END, "ü")


# Special characters in the German alphabet
def a_umlaut():
    # Whenever it is called add the special character on the end
    german_learn_entry.insert(END, "ä")


# Special characters in the Spanish alphabet
def upside_down_question_mark():
    # Whenever it is called add the special character on the end
    spanish_learn_entry.insert(END, "¿")


# Spanish learn function for when the user selects the language and module
def spanish_learn():
    # Import all global variables needed
    global SCORE_TRACKER
    global SPANISH_MODULE
    global ARCADE_SELECTED
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global SPANISH_LEARN_COUNT
    global SPANISH_LEARN_SCORE
    global SPANISH_SCORE_COUNT
    global MODULE_COUNT_TRACKER
    global HELP_SECTION_TRACKER
    global SPANISH_MODULE_COMBOBOX
    # Set the tracker to 0
    MODULE_COUNT_TRACKER = 0
    # Simple Error Bypass
    try:
        # Open the file previously selected in read mode as variable f
        with open(SPANISH_MODULE) as f:
            # Set everything inside to the variable contents
            contents = f.read()
            # Split the contents wherever there is a comma in the file
            contents = contents.split(",")
            # For item in the contents
            for item in contents:
                # Add one to the tracker
                MODULE_COUNT_TRACKER += 1
        # Set that the user is not in arcade mode
        ARCADE_MODE_BOOL = False
        # Set that the user is in Spanish section
        SPANISH_MODE_BOOL = True
        # Set the score tracker to 0
        SCORE_TRACKER = 0
        # Set the boolean if arcade was selected to 0
        ARCADE_SELECTED = 0
        # Set the screen that the user is on to the fifth
        HELP_SECTION_TRACKER = 5
        # Call the help section function
        help_storage()
        # Set the score to 0
        SPANISH_SCORE_COUNT = 0
        # Set the learn count to 1
        SPANISH_LEARN_COUNT = 1
        # Set the learn score to 0
        SPANISH_LEARN_SCORE = 0
        # Place the arcade button in the middle
        spanish_arcade_button.place(x=410, y=200)
        # Place the learn mode button to the middle
        spanish_learn_mode_button.place(x=293, y=200)
        # Move unnecessary items out of the way
        SPANISH_MODULE_COMBOBOX.place(x=3000, y=3000)
        module_spanish_continue_button.place(x=3000, y=3000)
    # If the question set has not been found
    except FileNotFoundError:
        # Move all items out of the way
        SPANISH_MODULE_COMBOBOX.place(x=3000, y=3000)
        module_spanish_continue_button.place(x=3000, y=3000)
        # Call the modules function again
        spanish_modules()


# Function which is called when the user selects German
def german_modules():
    # Create the German combobox
    create_german_combo_box()
    # Import the combobox variable
    global GERMAN_MODULE_COMBOBOX
    # Import the help section tracker
    global HELP_SECTION_TRACKER
    # Set the screen to the fourth
    HELP_SECTION_TRACKER = 4
    # Call the help section function
    help_storage()
    # Place the german zone label to the top middle
    german_zone_label.place(x=205, y=10)
    # Place the back button on the bottom in case they want to return
    back_learn_button.place(x=299, y=550)
    # Place the combobox in the middle
    GERMAN_MODULE_COMBOBOX.place(x=220, y=200)
    # Place the continue button on screen for when they have selected a module
    module_german_continue_button.place(x=620, y=200)
    # Place unnecessary items out of the way
    welcome_back_label.place(x=3000, y=3000)
    german_learn_button.place(x=3000, y=3000)
    spanish_learn_button.place(x=3000, y=3000)


# Procedure when the user has selected a module
def german_module_selected():
    # Import the global combobox
    global GERMAN_MODULE_COMBOBOX
    # Define a German module global variable
    global GERMAN_MODULE
    # If the combobox has an item selected
    if GERMAN_MODULE_COMBOBOX.get():
        # Set the new variable to the item inside
        GERMAN_MODULE = GERMAN_MODULE_COMBOBOX.get()
        # Replace all spaces with underscores and make it all lowercase
        GERMAN_MODULE = GERMAN_MODULE.replace(" ", "_").lower()
        # Add the file extension to the end
        GERMAN_MODULE += ".txt"
        # Bypass a back slash error
        GERMAN_MODULE = DIRECTORY + r"\questions\\" + GERMAN_MODULE
        # Call the German learn function
        german_learn()


# Function called once both the module and language has been chosen
def german_learn():
    # Import all global variables needed
    global GERMAN_MODULE
    global SCORE_TRACKER
    global ARCADE_SELECTED
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global GERMAN_LEARN_COUNT
    global GERMAN_LEARN_SCORE
    global GERMAN_SCORE_COUNT
    global HELP_SECTION_TRACKER
    global MODULE_COUNT_TRACKER
    global GERMAN_MODULE_COMBOBOX
    # Set the tracker to 0
    MODULE_COUNT_TRACKER = 0
    # Simple Error Bypass
    try:
        # Open the file previously selected in read mode as variable f
        with open(GERMAN_MODULE) as f:
            # Set everything inside to the variable contents
            contents = f.read()
            # Split the contents wherever there is a comma in the file
            contents = contents.split(",")
            # For item in the contents
            for item in contents:
                # Add one to the tracker
                MODULE_COUNT_TRACKER += 1
        # Set that the user is not in arcade mode
        ARCADE_MODE_BOOL = False
        # Set that the user is in German section
        SPANISH_MODE_BOOL = False
        # Set the score tracker to 0
        SCORE_TRACKER = 0
        # Set the boolean if arcade was selected to 0
        ARCADE_SELECTED = 0
        # Set the screen that the user is on to the fifth
        HELP_SECTION_TRACKER = 5
        # Call the help section function
        help_storage()
        # Set the score to 0
        GERMAN_SCORE_COUNT = 0
        # Set the learn count to 1
        GERMAN_LEARN_COUNT = 1
        # Set the learn score to 0
        GERMAN_LEARN_SCORE = 0
        # Place the arcade button in the middle
        german_arcade_button.place(x=410, y=200)
        # Place the learn mode button to the middle
        german_learn_mode_button.place(x=293, y=200)
        # Move unnecessary items out of the way
        GERMAN_MODULE_COMBOBOX.place(x=3000, y=3000)
        module_german_continue_button.place(x=3000, y=3000)
    # If the question set has not been found
    except FileNotFoundError:
        # Move all items out of the way
        GERMAN_MODULE_COMBOBOX.place(x=3000, y=3000)
        module_german_continue_button.place(x=3000, y=3000)
        # Call the modules function again
        german_modules()


# Redirect if the user presses enter instead of a button
def spanish_redirect_mode(key):
    # Call the direct function without the variable passed through
    spanish_learn_mode()


# This is the Spanish Learn mode function which creates questions
def spanish_learn_mode():
    # Import all global variables needed
    global SPANISH_MODULE
    global HELP_SECTION_TRACKER
    global SPANISH_LEARN_ANSWER
    global MODULE_COUNT_TRACKER
    global SPANISH_LEARN_QUESTION
    global SPANISH_INCORRECT_ANSWER
    global SPANISH_LEARN_QUESTION_NEW
    # Set the screen to the fifth
    HELP_SECTION_TRACKER = 5
    # Call the help function
    help_storage()
    # Simple Error Bypass
    try:
        # Move the incorrect answer message from before out of the way
        SPANISH_INCORRECT_ANSWER.place(x=3000, y=3000)
    # If no error message created
    except NameError:
        # Move on
        pass
    # Move all special characters on screen
    o_accent_button.place(x=320, y=300)
    n_accent_button.place(x=350, y=300)
    e_accent_button.place(x=410, y=300)
    i_accent_button.place(x=440, y=300)
    a_accent_button.place(x=470, y=300)
    u_accent_button.place(x=290, y=300)
    upside_down_question_mark_button.place(x=380, y=300)
    # Move the submit button on screen
    spanish_submit_button.place(x=350, y=400)
    # Move all unnecessary items out of the way
    logout_button.place(x=3000, y=3000)
    spanish_zone_label.place(x=3000, y=3000)
    spanish_arcade_button.place(x=3000, y=3000)
    spanish_continue_button.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)
    # Create the string for which question they are on
    question_count = "Question Number " + str(SPANISH_LEARN_COUNT) + "."
    # Create the string for their current score
    current_score = "Your current score is: " + str(SPANISH_LEARN_SCORE)
    # Open's the module file in read mode as f
    with open(SPANISH_MODULE) as f:
        # Set the contents of the file to contents
        contents = f.read()
        # Split the contents each time a comma is found
        contents = contents.split(",")
    # Create a random number between 0 and the total amount of words
    random_number = randint(0, MODULE_COUNT_TRACKER)
    # Simple Error Bypass
    try:
        # Set the question to the word corresponding to the random number
        SPANISH_LEARN_QUESTION = contents[random_number]
        # If the random number is even
        if random_number % 2 == 0:
            # The answer is the next item
            SPANISH_LEARN_ANSWER = contents[random_number+1]
            # Create the question string
            even_question = question_count + "\n\n" + current_score + "\n\n\n\n" + SPANISH_LEARN_QUESTION
            # Add informative stuff
            even_question += "\n\nType the Spanish for the English above and press Enter:"
            # Make the question into a label with the text
            SPANISH_LEARN_QUESTION_NEW = Label(main_gui, text=even_question, font=("Lucida Sans", 10, "bold"), bd=3,
                                               bg="orange", fg="white")
            # Place in the middle
            SPANISH_LEARN_QUESTION_NEW.place(x=200, y=100)
        # If the random number is odd
        else:
            # The answer is the previous item
            SPANISH_LEARN_ANSWER = contents[random_number-1]
            # Create the question
            odd_question = question_count + "\n\n" + current_score + "\n\n\n\n" + SPANISH_LEARN_QUESTION
            # Add stuff to it
            odd_question += "\n\nType the English for the Spanish above and press Enter:"
            # Create a label with the text inside
            SPANISH_LEARN_QUESTION_NEW = Label(main_gui, text=odd_question, font=("Lucida Sans", 10, "bold"), bd=3,
                                               bg="orange", fg="white")
            # Place it in the middle
            SPANISH_LEARN_QUESTION_NEW.place(x=200, y=100)
        # Place the entry box below the question
        spanish_learn_entry.place(x=275, y=250)
        # Bind enter to calling the process
        main_gui.bind('<Return>', spanish_learn_process_bypass)
    # If there is an error with the question
    except IndexError:
        # Another Error Bypass
        try:
            # Try moving the question out of the way
            SPANISH_LEARN_QUESTION_NEW.place(x=3000, y=3000)
        # If the question had not yet been defined 
        except NameError:
            # Pass
            pass
        # Pass
        pass
        # Call the learn mode function to restart
        spanish_learn_mode()


# A bypass function to get around Tkinter's variable passing with bind()
def spanish_learn_process_bypass(key):
    # Call the function without the key passed through
    spanish_learn_process()


# The process when the user submits their answer
def spanish_learn_process():
    # Import the global variables
    global STREAK_LABEL
    global SCORE_TRACKER
    global ARCADE_SELECTED
    global SPANISH_LEARN_SCORE
    global SPANISH_LEARN_COUNT
    global SPANISH_LEARN_ANSWER
    global SPANISH_LEARN_QUESTION
    global SPANISH_INCORRECT_ANSWER
    # If the entry box has an answer inside
    if spanish_learn_entry.get():
        # Place unnecessary items out of the way
        o_accent_button.place(x=3000, y=3000)
        n_accent_button.place(x=3000, y=3000)
        e_accent_button.place(x=3000, y=3000)
        i_accent_button.place(x=3000, y=3000)
        a_accent_button.place(x=3000, y=3000)
        u_accent_button.place(x=3000, y=3000)
        spanish_submit_button.place(x=3000, y=3000)
        SPANISH_LEARN_QUESTION_NEW.place(x=3000, y=3000)
        upside_down_question_mark_button.place(x=3000, y=3000)
        # Simple Error Bypass
        try:
            # Move the streak label out of the way
            STREAK_LABEL.place(x=3000, y=3000)
        # If they have no streak
        except NameError:
            # Move on
            pass
        # Set their answer to the item in the entry box
        their_answer = spanish_learn_entry.get()
        # Delete everything found inside the entry box for next question
        spanish_learn_entry.delete(0, END)
        # Add one to the counter
        SPANISH_LEARN_COUNT += 1
        # If their answer is the same as the actual answer (both lowercase) 
        if their_answer.lower() == SPANISH_LEARN_ANSWER.lower():
            # Add one to the score tracker
            SCORE_TRACKER += 1
            # If the score tracker is between 3 and 10
            if 3 <= SCORE_TRACKER < 10:
                # Create a streak label with their current streak
                STREAK_LABEL = Label(main_gui, text="STREAK!\n" + str(SCORE_TRACKER) + "\nDouble points!",
                                     font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
                # Place on screen
                STREAK_LABEL.place(x=330, y=450)
                # Add two to the user's score
                SPANISH_LEARN_SCORE += 2
            # Or if the score tracker is more than 10
            elif SCORE_TRACKER >= 10:
                # Create a streak label with their current streak
                STREAK_LABEL = Label(main_gui, text="STREAK!\n" + str(SCORE_TRACKER) + "\nTriple points!",
                                     font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
                # Place on scree
                STREAK_LABEL.place(x=330, y=450)
                # Add three to the user's score
                SPANISH_LEARN_SCORE += 3
            # If their score is less than 3
            else:
                # Add one to their score
                SPANISH_LEARN_SCORE += 1
            # Select the Spanish progress for the user
            connection_cursor.execute("SELECT sprogress FROM LoginDetails WHERE username=?", (LOGIN_USERNAME,))
            # Fetch the first score that comes up
            past_score = connection_cursor.fetchone()
            # Set the new score to one more that the prior - Streaks discounted
            new_score = past_score[0] + 1
            # Update the database with the new progress
            connection.execute("UPDATE LoginDetails SET sprogress = ? WHERE username = ?", (new_score, LOGIN_USERNAME,))
            # Save to database
            connection.commit()
            # Refresh leader board
            leader_board_refresh()
            # Call the learn mode function
            spanish_learn_mode()
        # If their answer is wrong
        else:
            # Set the score tracker to 0
            SCORE_TRACKER = 0
            # If it is arcade mode
            if ARCADE_SELECTED == 1:
                # Call the learn mode again due to no error messages
                spanish_learn_mode()
            # Or if it is learn mode
            else:
                # Place the entry out of the way
                spanish_learn_entry.place(x=3000, y=3000)
                # Create a label for the incorrect answer
                SPANISH_INCORRECT_ANSWER = Label(main_gui, text="Incorrect answer.\n\nThe question was:\n" +
                                                                SPANISH_LEARN_QUESTION + "\n\nYou typed in:\n" +
                                                                their_answer + "\n\nThe correct answer was:\n" +
                                                                SPANISH_LEARN_ANSWER +
                                                                "\n\nPress continue to carry on.",
                                                 font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
                # Place on screen
                SPANISH_INCORRECT_ANSWER.place(x=300, y=100)
                # Place the continue button for when they have finished reading
                spanish_continue_button.place(x=365, y=320)
                # Bind the enter key to returning to learn mode
                main_gui.bind('<Return>', spanish_redirect_mode)


# Simple redirection due to an error
def german_redirect_mode(key):
    # Call the function without the variable passed through
    german_learn_mode()


# German Learn mode function for creating questions
def german_learn_mode():
    # Import all global variables needed
    global GERMAN_MODULE
    global GERMAN_LEARN_ANSWER
    global HELP_SECTION_TRACKER
    global MODULE_COUNT_TRACKER
    global GERMAN_LEARN_QUESTION
    global GERMAN_INCORRECT_ANSWER
    global GERMAN_LEARN_QUESTION_NEW
    # Move special characters on screen
    a_umlaut_button.place(x=380, y=300)
    scharfes_button.place(x=350, y=300)
    u_umlaut_button.place(x=410, y=300)
    # Place the submit button on screen
    german_submit_button.place(x=350, y=400)
    # Move unnecessary items off screen
    logout_button.place(x=3000, y=3000)
    german_zone_label.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    german_continue_button.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)
    # Set the screen to the fifth
    HELP_SECTION_TRACKER = 5
    # Call the help function
    help_storage()
    # Simple Error Bypass
    try:
        # Move the incorrect answer message out of the way
        GERMAN_INCORRECT_ANSWER.place(x=3000, y=3000)
    # If no error message
    except NameError:
        # Move on
        pass
    # Create the question number string
    question_count = "Question Number " + str(GERMAN_LEARN_COUNT) + "."
    # Create the current score string
    current_score = "Your current score is: " + str(GERMAN_LEARN_SCORE)
    # With opening of the question set in read mode as f
    with open(GERMAN_MODULE) as f:
        # Copy the contents to variable contents
        contents = f.read()
        # Split it wherever there is a comma
        contents = contents.split(",")
    # Create a random number between 0 and the count tracker
    random_number = randint(0, MODULE_COUNT_TRACKER)
    # Simple Error Bypass
    try:
        # Set the question to the word associated with the random number
        GERMAN_LEARN_QUESTION = contents[random_number]
        # If the random number was even
        if random_number % 2 == 0:
            # The answer is the next word
            GERMAN_LEARN_ANSWER = contents[random_number+1]
            # Create the question
            even_question = question_count + "\n\n" + current_score + "\n\n\n\n" + GERMAN_LEARN_QUESTION
            # Add some stuff to the end
            even_question += "\n\nType the English for the German above and press Enter:"
            # Create a label with the text inside
            GERMAN_LEARN_QUESTION_NEW = Label(main_gui, text=even_question, font=("Lucida Sans", 10, "bold"), bd=3,
                                              bg="orange", fg="white")
            # Place in the middle of the screen
            GERMAN_LEARN_QUESTION_NEW.place(x=200, y=100)
        # If the random number was odd
        else:
            # The answer is the previous one
            GERMAN_LEARN_ANSWER = contents[random_number-1]
            # Create the question
            odd_question = question_count + "\n\n" + current_score + "\n\n\n\n" + GERMAN_LEARN_QUESTION
            # Add stuff to the end
            odd_question += "\n\nType the German for the English above and press Enter:"
            # Create a label with the question inside
            GERMAN_LEARN_QUESTION_NEW = Label(main_gui, text=odd_question, font=("Lucida Sans", 10, "bold"), bd=3,
                                              bg="orange", fg="white")
            # Place in the middle of the screen
            GERMAN_LEARN_QUESTION_NEW.place(x=200, y=100)
        # Place the entry box in the middle below the question
        german_learn_entry.place(x=275, y=250)
        # Bind the enter key to calling the process
        main_gui.bind('<Return>', german_learn_process_bypass)
    # If there was an error with the question
    except IndexError:
        # In case there is an error inside the error
        try:
            # Try moving the question out of the way
            GERMAN_LEARN_QUESTION.place(x=3000, y=3000)
        # If there was an error moving the question
        except NameError:
            # Move on
            pass
        # Move on
        pass
        # Actually move on now to the learn mode function again
        german_learn_mode()


# Function to bypass the key issue
def german_learn_process_bypass(key):
    # Call the actual process
    german_learn_process()


# Process once an answer has been made
def german_learn_process():
    # Import global variables
    global STREAK_LABEL
    global SCORE_TRACKER
    global ARCADE_SELECTED
    global ARCADE_MODE_BOOL
    global GERMAN_LEARN_SCORE
    global GERMAN_LEARN_COUNT
    global GERMAN_LEARN_QUESTION
    global GERMAN_INCORRECT_ANSWER
    # Place all of the special buttons out of the way
    scharfes_button.place(x=3000, y=3000)
    u_umlaut_button.place(x=3000, y=3000)
    a_umlaut_button.place(x=3000, y=3000)
    german_submit_button.place(x=3000, y=3000)
    GERMAN_LEARN_QUESTION_NEW.place(x=3000, y=3000)
    # If there is something in the entry
    if german_learn_entry.get():
        # Simple Error Bypass
        try:
            # Place the streak label out of the way
            STREAK_LABEL.place(x=3000, y=3000)
        # If there is no streak
        except NameError:
            # Move on
            pass
        # Create a variable which contains what they typed as their answer
        their_answer = german_learn_entry.get()
        # Delete everything in the field
        german_learn_entry.delete(0, END)
        # Add one to German learn count
        GERMAN_LEARN_COUNT += 1
        # If their answer is equal to the actual answer
        if their_answer.lower() == GERMAN_LEARN_ANSWER.lower():
            # Then add one to the score tracker
            SCORE_TRACKER += 1
            # If the score tracker is more than 3 and less than 10
            if 3 <= SCORE_TRACKER < 10:
                # Make a streak label
                STREAK_LABEL = Label(main_gui, text="STREAK!\n" + str(SCORE_TRACKER) + "\nDouble points!",
                                     font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
                # Place it in the middle bottom
                STREAK_LABEL.place(x=330, y=450)
                # Add two to the score
                GERMAN_LEARN_SCORE += 2
            # If the score is 10 or more
            elif SCORE_TRACKER >= 10:
                # Make a streak label
                STREAK_LABEL = Label(main_gui, text="STREAK!\n" + str(SCORE_TRACKER) + "\nTriple points!",
                                     font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
                # Place it in the middle bottom
                STREAK_LABEL.place(x=330, y=450)
                # Add three to the score
                GERMAN_LEARN_SCORE += 3
            # If less than 3 score
            else:
                # Add one to the score
                GERMAN_LEARN_SCORE += 1
            # If they are not in arcade mode
            if not ARCADE_MODE_BOOL:
                # Select the user's German progress
                connection_cursor.execute("SELECT gprogress FROM LoginDetails WHERE username=?", (LOGIN_USERNAME,))
                # Past score is the first item
                past_score = connection_cursor.fetchone()
                # New score is past score plus one
                new_score = past_score[0] + 1
                # Update the user's German progress
                connection.execute("UPDATE LoginDetails SET gprogress = ? WHERE username = ?", (new_score,
                                                                                                LOGIN_USERNAME,))
                # Save changes to the database
                connection.commit()
                # Call the German learn mode function for next question
                german_learn_mode()
            # If they are in arcade mode
            else:
                # Call German learn mode as no need to add score
                german_learn_mode()
        # If their answer is wrong
        else:
            # Set the score tracker back to 0
            SCORE_TRACKER = 0
            # If they are in arcade mode
            if ARCADE_SELECTED == 1:
                # Send them back to German learn mode for next question as they do not need incorrect answer message
                german_learn_mode()
            # If they are in learn mode
            else:
                # Move unnecessary items out of the way
                german_learn_entry.place(x=3000, y=3000)
                # Create an incorrect answer label with the correct answer inside
                GERMAN_INCORRECT_ANSWER = Label(main_gui, text="Incorrect answer.\n\nThe question was:\n" +
                                                               GERMAN_LEARN_QUESTION + "\n\nYou typed in:\n" +
                                                               their_answer + "\n\nThe correct answer was:\n" +
                                                               GERMAN_LEARN_ANSWER + "\n\nPress continue to carry on.",
                                                font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
                # Place it in the middle
                GERMAN_INCORRECT_ANSWER.place(x=300, y=100)
                # Place the continue button for when they are done with the incorrect answer
                german_continue_button.place(x=365, y=320)
                # Bind enter key with sending them back to the learn mode as well
                main_gui.bind('<Return>', german_redirect_mode)


# Spanish arcade mode function if they select arcade mode and Spanish
def spanish_arcade():
    # Import global variables
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global ARCADE_SELECTED
    # Set Arcade mode to true
    ARCADE_MODE_BOOL = True
    # Set Spanish Mode to true
    SPANISH_MODE_BOOL = True
    # Set arcade selected to 1
    ARCADE_SELECTED = 1
    # Call the help storage function
    help_storage()
    # Move the start button on screen
    spanish_arcade_start_button.place(x=360, y=300)
    # Move unnecessary items out of the way
    spanish_zone_label.place(x=3000, y=3000)
    spanish_arcade_button.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)


# German arcade mode function if they select arcade mode and German
def german_arcade():
    # Import global variables
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global ARCADE_SELECTED
    # Set arcade mode to true
    ARCADE_MODE_BOOL = True
    # Set Spanish mode to false
    SPANISH_MODE_BOOL = False
    # Set arcade mode to 1
    ARCADE_SELECTED = 1
    # Call the help storage function
    help_storage()
    # Move the start button on screen
    german_arcade_start_button.place(x=360, y=300)
    # Move the unnecessary items out of the way
    german_zone_label.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)


# Spanish timer function for arcade mode
def spanish_arcade_mode():
    # Define the timer global variable
    global ARCADE_TIMER
    # Call the help storage
    help_storage()
    # Move unnecessary items out of the way
    spanish_arcade_start_button.place(x=3000, y=3000)
    # Call the learn mode function for questions
    spanish_learn_mode()
    # Set the timer variable to 60
    ARCADE_TIMER = 60
    # Begin the countdown function
    countdown()
    # After 1 minute + 0.5 seconds for delays call the main learn function
    main_gui.after(60500, main_learn)


# Countdown function
def countdown():
    # Import global variables
    global ARCADE_TIMER
    global TIMER_COUNTER
    # If the timer is about to end or still has time left
    if ARCADE_TIMER >= -1:
        # Simple Error Bypass
        try:
            # Move the timer out of the way
            TIMER_COUNTER.place(x=3000, y=3000)
        # If there is no timer
        except NameError:
            # Move on
            pass
        # If the timer has seconds left
        if ARCADE_TIMER >= 0:
            # Create the timer label
            timer_label = str(ARCADE_TIMER) + " Seconds Left!"
            # Make it into a label with the previous text
            TIMER_COUNTER = Label(main_gui, text=timer_label, font=("Lucida Sans", 10, "bold"), bd=3, bg="orange",
                                  fg="white")
            # Place the timer at the bottom
            TIMER_COUNTER.place(x=330, y=340)
            # Minus one from the timer
            ARCADE_TIMER -= 1
            # After one second recall the function until it has stopped
            main_gui.after(1000, countdown)


# German timer function for arcade mode
def german_arcade_mode():
    # Define the timer global variable
    global ARCADE_TIMER
    # Call the help storage
    help_storage()
    # Move unnecessary items out of the way
    german_arcade_start_button.place(x=3000, y=3000)
    # Call the learn mode function for questions
    german_learn_mode()
    # Set the timer variable to 60
    ARCADE_TIMER = 60
    # Begin the countdown function
    countdown()
    # After 1 minute + 0.5 seconds for delays call the main learn function
    main_gui.after(60500, main_learn)


# This is the main menu for when the user has logged in
def main_learn():
    # Import all of the global variables
    global ARCADE_MODE_BOOL
    global SPANISH_MODE_BOOL
    global SPANISH_LEARN_SCORE
    global GERMAN_LEARN_SCORE
    global HELP_SECTION_TRACKER
    global ARCADE_TIMER
    global GERMAN_INCORRECT_ANSWER
    global SPANISH_INCORRECT_ANSWER
    # If they are in arcade mode
    if ARCADE_MODE_BOOL:
        # If they are in Spanish mode
        if SPANISH_MODE_BOOL:
            # Get the arcade score for the user logged in
            connection_cursor.execute("SELECT ascore FROM LoginDetails WHERE username=?", (LOGIN_USERNAME,))
            # Get the first item found
            past_score = connection_cursor.fetchone()
            # If the past score is less than their most recent score
            if past_score[0] < SPANISH_LEARN_SCORE:
                # Update the arcade score with the higher achieved score
                connection.execute("UPDATE LoginDetails SET ascore = ? WHERE username = ?",
                                   (SPANISH_LEARN_SCORE, LOGIN_USERNAME,))
                # Save all changes
                connection.commit()
        # If they are not in spanish mode
        else:
            # Get the arcade score for the user logged in
            connection_cursor.execute("SELECT ascore FROM LoginDetails WHERE username=?", (LOGIN_USERNAME,))
            # Get the first item found
            past_score = connection_cursor.fetchone()
            # If the past score is less than their most recent score
            if past_score[0] < GERMAN_LEARN_SCORE:
                # Update the arcade score with the higher achieved score
                connection.execute("UPDATE LoginDetails SET ascore = ? WHERE username = ?",
                                   (GERMAN_LEARN_SCORE, LOGIN_USERNAME,))
                # Save all changes
                connection.commit()
    # Set the help screen to 3
    HELP_SECTION_TRACKER = 3
    # Call the help storage function
    help_storage()
    # Simple bypass error
    try:
        # Try setting the timer to -1 meaning it will be over
        ARCADE_TIMER = -1
    # If the arcade timer has not been made yet
    except NameError:
        # Move on
        pass
    # Unbind the return key so that no functions are called when it is pressed
    main_gui.unbind("<Return>")
    # Move the logout button back on screen so that they can log out
    logout_button.place(x=225, y=550)
    # Move the welcome label to the middle
    welcome_back_label.place(x=205, y=10)
    # Move the German learn button on screen
    german_learn_button.place(x=410, y=200)
    # Move the Spanish learn button on screen
    spanish_learn_button.place(x=300, y=200)
    # Move all unnecessary items out of the way
    o_accent_button.place(x=3000, y=3000)
    i_accent_button.place(x=3000, y=3000)
    n_accent_button.place(x=3000, y=3000)
    e_accent_button.place(x=3000, y=3000)
    u_accent_button.place(x=3000, y=3000)
    a_accent_button.place(x=3000, y=3000)
    a_umlaut_button.place(x=3000, y=3000)
    scharfes_button.place(x=3000, y=3000)
    u_umlaut_button.place(x=3000, y=3000)
    back_learn_button.place(x=3000, y=3000)
    german_zone_label.place(x=3000, y=3000)
    spanish_zone_label.place(x=3000, y=3000)
    german_learn_entry.place(x=3000, y=3000)
    spanish_learn_entry.place(x=3000, y=3000)
    back_welcome_button.place(x=3000, y=3000)
    german_submit_button.place(x=3000, y=3000)
    german_arcade_button.place(x=3000, y=3000)
    spanish_submit_button.place(x=3000, y=3000)
    spanish_arcade_button.place(x=3000, y=3000)
    german_continue_button.place(x=3000, y=3000)
    spanish_continue_button.place(x=3000, y=3000)
    german_learn_mode_button.place(x=3000, y=3000)
    spanish_learn_mode_button.place(x=3000, y=3000)
    german_arcade_start_button.place(x=3000, y=3000)
    spanish_arcade_start_button.place(x=3000, y=3000)
    module_german_continue_button.place(x=3000, y=3000)
    module_spanish_continue_button.place(x=3000, y=3000)
    upside_down_question_mark_button.place(x=3000, y=3000)
    # First error bypass
    try:
        # Try moving the German module combobox out of the way
        GERMAN_MODULE_COMBOBOX.place(x=3000, y=3000)
    # If the combobox has not been created
    except NameError:
        # Move on
        pass
    # Second error bypass
    try:
        # Try moving the Spanish module combobox out of the way
        SPANISH_MODULE_COMBOBOX.place(x=3000, y=3000)
    # If the combobox has not been created
    except NameError:
        # Move on
        pass
    # Third error bypass
    try:
        # Try moving Spanish specific learn mode items out of the way
        SPANISH_LEARN_QUESTION_NEW.place(x=3000, y=3000)
    # If they did not select Spanish learn mode
    except NameError:
        # Move on
        pass
    # Fourth error bypass
    try:
        # Try moving the German specific learn mode items out of the way
        GERMAN_LEARN_QUESTION_NEW.place(x=3000, y=3000)
    # If they did not select German learn mode
    except NameError:
        # Move on
        pass
    # Fifth error bypass
    try:
        # Try moving the Spanish incorrect answer message out of the way
        SPANISH_INCORRECT_ANSWER.place(x=3000, y=3000)
    # If they did not get anything wrong
    except NameError:
        # Move on
        pass
    # Sixth error bypass
    try:
        # Try moving the German incorrect answer message out of the way
        GERMAN_INCORRECT_ANSWER.place(x=3000, y=3000)
    # If they did not get anything wrong
    except NameError:
        # Move on
        pass
    # Seventh error bypass
    try:
        # Try moving the streak label out of the way
        STREAK_LABEL.place(x=3000, y=3000)
    # If they did not have a streak
    except NameError:
        # Move on
        pass


# Logout procedure
def logout():
    # Move the leader board out of the screen
    leader_board_window.geometry("300x600+3000+3000")
    # Call the main menu function
    main_window()


# Quit function
def quit_function():
    # Destroy the super window which will also destroy the others
    main_gui.destroy()

################
# Admin System #
################


# Admin main menu
def admin_system():
    pass

##################
# Teacher System #
##################


# View the student progress function
def view_student_progress():
    # Import the global variables
    global HELP_SECTION_TRACKER
    global VIEW_STUDENT_PROGRESS_LABEL
    # Set the help window to 7
    HELP_SECTION_TRACKER = 7
    # Call the help storage function
    help_storage()
    # Place the back teacher button on screen
    back_teacher_button.place(x=299, y=550)
    # Displace all unnecessary items
    logout_button.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    view_student_progress_button.place(x=3000, y=3000)
    # Create an empty array for the view student progress list
    view_student_progress_list = []
    # Create an array with 5 slots for strings
    new_row = [""] * 5
    # Add a title to the list
    view_student_progress_list.append("LIST OF STUDENTS\n------------------------------------------------------------"
                                      "------------------------------------------------------------------------------"
                                      "--------------------------------------------------------\nNAME  -  SPANISH "
                                      "PROGRESS  -  GERMAN PROGRESS  -  ARCADE SCORE\n")
    # For item in the database
    for row in connection.execute("SELECT id,username,teacher,admin,sprogress,gprogress,ascore FROM LoginDetails"):
        # If they are a teacher or an admin
        if row[2] == 1 or row[3] == 1:
            # Ignore them
            pass
        # If they are a student
        else:
            # Set the first item to the id of the student
            new_row[0] = str(row[0])
            # Set the second item to the name of the student
            new_row[1] = str(row[1])
            # Set the third item to the Spanish Progress
            new_row[2] = str(row[4])
            # Set the fourth item to the German Progress
            new_row[3] = str(row[5])
            # Set the fifth item to the arcade score
            new_row[4] = str(row[6])
            # Convert to string
            row = str(new_row)
            # Remove all formatting from the array for lack of a better method
            row = row.replace("[", "")
            row = row.replace("]", "")
            row = row.replace("'", "")
            # Add a new line to the list
            view_student_progress_list.append("\n")
            # Add the row to the list
            view_student_progress_list.append(row)
    # Join the list together
    view_student_progress_list = ''.join(view_student_progress_list)
    # Create a label with the list of students
    VIEW_STUDENT_PROGRESS_LABEL = Label(main_gui, text=view_student_progress_list, font=("Lucida Sans", 10, "bold"),
                                        bd=3, bg="orange", fg="white")
    # Place on screen in the top middle
    VIEW_STUDENT_PROGRESS_LABEL.place(x=10, y=110)


# Change password function
def change_password():
    # Import the global variables
    global HELP_SECTION_TRACKER
    global RESET_PASSWORD_LABEL
    # Set the window to 8
    HELP_SECTION_TRACKER = 8
    # Call the help storage function
    help_storage()
    # Place the id field on screen
    id_field.place(x=237, y=240)
    # Place the back button on screen
    back_teacher_button.place(x=299, y=550)
    # Place the reset password field on screen
    reset_password_field.place(x=430, y=240)
    # Place the reset password button on screen
    reset_password_button.place(x=365, y=240)
    # Move unnecessary items off the screen
    logout_button.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    view_student_progress_button.place(x=3000, y=3000)
    # Create a list of text for the label
    reset_password_list = "RESET USER PASSWORD\n\nStep 1: View list of students in other section.\nStep 2: Get the" \
                          " user ID of the student.\nStep 3: Enter the ID and the new password.\nStep 4: Click" \
                          " finalize and their password will have been reset.\n\nID:                                " \
                          "           PASSWORD:"
    # Create the label with the text inside
    RESET_PASSWORD_LABEL = Label(main_gui, text=reset_password_list, font=("Lucida Sans", 10, "bold"), bd=3,
                                 bg="orange", fg="white")
    # Place the reset password label on screen
    RESET_PASSWORD_LABEL.place(x=190, y=110)


# The process to reset a user's password
def reset_password_process():
    # Import the global variables
    global RESET_PASSWORD_LABEL
    global DONE_RESET_LABEL
    # If both of the fields have been inputted
    if reset_password_field.get() and id_field.get():
        # Retrieve the id
        id_reset = id_field.get()
        # Retrieve the password
        reset_password = reset_password_field.get()
        # Remove everything in the fields
        reset_password_field.delete(0, END)
        id_field.delete(0, END)
        # Create a temporary list
        temp = ()
        # Set the hashing algorithm to sha512
        current_hash = sha512()
        # Encode the password and turn it into byte format
        current_hash.update(reset_password.encode('utf-8'))
        # Set the hash to the variable
        password_hash = current_hash.hexdigest()
        # For item in the database with the same id
        for row in connection.execute("SELECT * FROM LoginDetails WHERE id = ?", id_reset):
            # Add to the list
            temp += row
        # Convert old one to string
        temp = str(temp)
        # If the list is empty
        if temp == "()":
            # Move on
            pass
        # If the user has been found
        else:
            # Move all unnecessary items out of the way
            id_field.place(x=3000, y=3000)
            reset_password_field.place(x=3000, y=3000)
            RESET_PASSWORD_LABEL.place(x=3000, y=3000)
            reset_password_button.place(x=3000, y=3000)
            # Update the new password 
            connection.execute("UPDATE LoginDetails SET password = ? WHERE id = ?", (password_hash, id_reset))
            # Save all changes
            connection.commit()
            # Create the text for the label
            done_reset_text = "Password has been reset."
            # Create the label with the text
            DONE_RESET_LABEL = Label(main_gui, text=done_reset_text, font=("Lucida Sans", 10, "bold"), bd=3,
                                     bg="orange", fg="white")
            # Place the label
            DONE_RESET_LABEL.place(x=310, y=200)


# This is the add questions function
def add_questions():
    # Import library
    import subprocess
    # Import global variables
    global ADD_QUESTIONS_LABEL
    global HELP_SECTION_TRACKER
    # Set the window to the ninth
    HELP_SECTION_TRACKER = 9
    # Call the help storage function
    help_storage()
    # Move the back button on screen
    back_teacher_button.place(x=299, y=550)
    # Move the add questions buttons and fields on screen
    add_questions_field.place(x=261, y=302)
    add_questions_submit_button.place(x=550, y=300)
    add_questions_german_checkbutton.place(x=508, y=300)
    add_questions_spanish_checkbutton.place(x=429, y=300)
    # Move unnecessary items out of the window
    logout_button.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    view_student_progress_button.place(x=3000, y=3000)
    # Create the text to go in the label
    add_questions_list = "ADD QUESTIONS\n\nStep 1. Type the words in the text file that opened. The format is" \
                         " translated word then English\nversion. E.G: hola,hello,buenos dias,good day. Continue in" \
                         " this manner. Make sure that the words are\ncapitalized, as it will not make the file look" \
                         " nicer.\nStep 2. Save the file with all lower case and wherever there is a space use an" \
                         " underscore. E.G: spanish_basics1.\nStep 3. Type the name of the text file in the first" \
                         " field. Wherever there is an underscore change\nit back to a space and also capitalize the" \
                         " first letter of the words.\nStep 4. Check the relevant checkbox. If the language is" \
                         " spanish or german then check the right one.\nIf not simply type the name of the language." \
                         " E.G: Latin\n\nName of question set    Spanish?    German?"
    # Create the label with the text inside
    ADD_QUESTIONS_LABEL = Label(main_gui, text=add_questions_list, font=("Lucida Sans", 10, "bold"), bd=3, bg="orange",
                                fg="white")
    # Place the label on screen
    ADD_QUESTIONS_LABEL.place(x=20, y=110)
    # Open up notepad
    subprocess.Popen(["notepad.exe"])


# The process to add question sets
def submit_question_set():
    # Import global variables
    global ADD_QUESTIONS_LABEL
    global DONE_ADD_QUESTIONS_LABEL
    # If name field has been inputted and either the Spanish module or the German module checkbutton has been clicked
    if add_questions_field.get() and ((spanish_module_add.get() and not german_module_add.get()) or
                                      (german_module_add.get() and not spanish_module_add.get())):
        # Set the name of the question set
        name = add_questions_field.get()
        # Set whether Spanish checkbox is ticked
        spanish = spanish_module_add.get()
        # Set whether German checkbox is ticked
        german = german_module_add.get()
        # Save to database the name and 1 or 0 for Spanish and German fields
        question_connection.execute("INSERT INTO QuestionSets(name,spanish,german) VALUES (?,?,?)",
                                    (name, spanish, german))
        # Save all changes
        question_connection.commit()
        # Create text for a label
        done_add_questions_text = "QUESTIONS HAVE BEEN\nADDED"
        # Create the label with the text
        DONE_ADD_QUESTIONS_LABEL = Label(main_gui, text=done_add_questions_text, font=("Lucida Sans", 10, "bold"),
                                         bd=3, bg="orange", fg="white")
        # Place on screen
        DONE_ADD_QUESTIONS_LABEL.place(x=310, y=200)
        # Move all unnecessary items out of the way
        ADD_QUESTIONS_LABEL.place(x=3000, y=3000)
        add_questions_field.place(x=3000, y=3000)
        add_questions_submit_button.place(x=3000, y=3000)
        add_questions_german_checkbutton.place(x=3000, y=3000)
        add_questions_spanish_checkbutton.place(x=3000, y=3000)


# Function to remove question sets
def remove_questions():
    # Import global variables
    global ID_MODULE_COMBOBOX
    global HELP_SECTION_TRACKER
    global REMOVE_QUESTIONS_LABEL
    # Set the help section to 10
    HELP_SECTION_TRACKER = 10
    # Call the help storage function
    help_storage()
    # Create an id combobox
    create_id_combo_box()
    # Move the id combobox on screen
    ID_MODULE_COMBOBOX.place(x=200, y=300)
    # Move the fields and buttons on screen
    id_questions_field.place(x=340, y=245)
    back_teacher_button.place(x=299, y=550)
    remove_questions_continue_button.place(x=500, y=240)
    # Move all unnecessary items out of the way
    logout_button.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    view_student_progress_button.place(x=3000, y=3000)
    # Create the text for the label
    remove_questions_list = "REMOVE QUESTIONS\n\nStep 1. Look at the corresponding ID in the drop down box.\n" \
                            "Step 2. Enter the ID below then click remove.\n\n\n\nID:"
    # Create the label with the text
    REMOVE_QUESTIONS_LABEL = Label(main_gui, text=remove_questions_list, font=("Lucida Sans", 10, "bold"), bd=3,
                                   bg="orange", fg="white")
    # Move the remove questions label on screen
    REMOVE_QUESTIONS_LABEL.place(x=190, y=110)


# This is the remove question sets process
def remove_questions_process():
    # If the id question field has something inside
    if id_questions_field.get():
        # Set the variable to whatever was inside
        id_entered = id_questions_field.get()
        # Remove everything in the field
        id_questions_field.delete(0, END)
        # Create a temporary list
        temp = ()
        # For item in the database where the id is the same as the one entered
        for row in question_connection.execute("SELECT * FROM QuestionSets WHERE id = ?", (id_entered,)):
            # Add the items to the list
            temp += row
        # Convert the old variable to string
        temp = str(temp)
        # If the list is empty i.e: no question set with corresponding id
        if temp == "()":
            # Move on
            pass
        # If there was a question set found
        else:
            # Import global variables
            global ID_MODULE_COMBOBOX
            global DONE_QUESTIONS_LABEL
            global REMOVE_QUESTIONS_LABEL
            # Delete the question set with the same id
            question_connection.execute("DELETE FROM QuestionSets WHERE id = (?)", (id_entered,))
            # Save all changes
            question_connection.commit()
            # Move all unnecessary items out of the way
            id_questions_field.place(x=3000, y=3000)
            ID_MODULE_COMBOBOX.place(x=3000, y=3000)
            REMOVE_QUESTIONS_LABEL.place(x=3000, y=3000)
            remove_questions_continue_button.place(x=3000, y=3000)
            # Create the text for the label
            done_questions_text = "QUESTION SET\nHAS BEEN REMOVED"
            # Create the label with the text inside
            DONE_QUESTIONS_LABEL = Label(main_gui, text=done_questions_text, font=("Lucida Sans", 10, "bold"), bd=3,
                                         bg="orange", fg="white")
            # Move the label on screen
            DONE_QUESTIONS_LABEL.place(x=310, y=200) 


# Delete user function
def delete_user():
    # Import global variables
    global DELETE_USER_LABEL
    global HELP_SECTION_TRACKER
    # Set the help section screen to 11
    HELP_SECTION_TRACKER = 11
    # Call the help storage function
    help_storage()
    # Move the id delete field on screen
    id_delete_field.place(x=237, y=230)
    # Move the buttons on screen
    remove_user_button.place(x=375, y=230)
    back_teacher_button.place(x=299, y=550)
    # Move all unnecessary items out of the way
    logout_button.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    view_student_progress_button.place(x=3000, y=3000)
    # Create the text for the label
    delete_user_list = "DELETE USER\n\nStep 1: Go back to the view list of students and get the id of the student " \
                       "to remove.\nStep 2: Go back here and enter the id.\nStep 3: Click finalize and the user will " \
                       "be deleted.\n"
    # Create the label for the text
    DELETE_USER_LABEL = Label(main_gui, text=delete_user_list, font=("Lucida Sans", 10, "bold"), bd=3, bg="orange",
                              fg="white")
    # Move the label on screen
    DELETE_USER_LABEL.place(x=100, y=110)


# Delete user process
def remove_user_process():
    # Import all global variables
    global DONE_REMOVE_LABEL
    global DELETE_USER_LABEL
    # If the id field has an id inside
    if id_field.get():
        # Set the variable to the text inside
        id_reset = id_field.get()
        # Remove all from the field
        id_field.delete(0, END)
        # Create a temporary list
        temp = ()
        # For item in the database where the id is the same as the one inputted
        for row in connection.execute("SELECT * FROM LoginDetails WHERE id = ?", (id_reset,)):
            # Add item to the list
            temp += row
        # Convert old variable to string
        temp = str(temp)
        # If the list is empty
        if temp == "()":
            # Move on
            pass
        # If there was a question set found 
        else:
            # Move all unnecessary items out of the way
            id_field.place(x=3000, y=3000)
            DELETE_USER_LABEL.place(x=3000, y=3000)
            remove_user_button.place(x=3000, y=3000)
            reset_password_field.place(x=3000, y=3000)
            reset_password_button.place(x=3000, y=3000)
            # Remove the question set with the same id
            connection.execute("DELETE FROM LoginDetails WHERE id = ?", (id_reset,))
            # Save all changes
            connection.commit()
            # Create the text to let the user know it has been removed
            done_remove_text = "USER HAS BEEN\nREMOVED"
            # Create the label for the text
            DONE_REMOVE_LABEL = Label(main_gui, text=done_remove_text, font=("Lucida Sans", 10, "bold"), bd=3,
                                      bg="orange", fg="white")
            # Place the label on screen
            DONE_REMOVE_LABEL.place(x=310, y=200) 


# Save backup function
def save_backup():
    # Import all necessary libraries
    from backup_database import perform_backup
    import datetime
    import sys
    # Import global variable
    global DONE_BACKUP_LABEL
    global HELP_SECTION_TRACKER
    # Set the help section tracker to 12
    HELP_SECTION_TRACKER = 12
    # Call the help storage function
    help_storage()
    # Move the back teacher button on screen
    back_teacher_button.place(x=299, y=550)
    # Move all unnecessary items out of the way
    logout_button.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    view_student_progress_button.place(x=3000, y=3000)
    # Create the text for the backup done function
    done_backup_text = "BACKUP HAS BEEN MADE."
    # Create the label with the text inside
    DONE_BACKUP_LABEL = Label(main_gui, text=done_backup_text, font=("Lucida Sans", 10, "bold"), bd=3, bg="orange",
                              fg="white")
    # Place the label on screen
    DONE_BACKUP_LABEL.place(x=340, y=200)
    # Set the backup directory to the path with the file inside
    backup_directory = os.path.dirname(sys.argv[0])
    # Set the directory to the directory just found
    directory = backup_directory
    # Add a back slash to the directory
    directory += '/'
    # Add backup to the directory name to go to that folder
    backup_directory += '/backup/'
    # Set the date to the current date
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    # Add the date to the backup directory
    backup_directory += date
    # Perform backup with the backup directory and the current directory
    perform_backup(backup_directory, directory)


# Restore backup function
def restore_backup():
    # Import the global variables
    global HELP_SECTION_TRACKER
    # Set the help section tracker to 13
    HELP_SECTION_TRACKER = 13
    # Call the help storage function
    help_storage()
    # Move the back teacher button on screen
    back_teacher_button.place(x=299, y=550)
    # Move all unnecessary items out of the way
    logout_button.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    delete_user_button.place(x=3000, y=3000)
    save_backup_button.place(x=3000, y=3000)
    add_questions_button.place(x=3000, y=3000)
    username_taken_label.place(x=3000, y=3000)
    initial_choice_label.place(x=3000, y=3000)
    restore_backup_button.place(x=3000, y=3000)
    change_password_button.place(x=3000, y=3000)
    remove_questions_button.place(x=3000, y=3000)
    view_student_progress_button.place(x=3000, y=3000)
    # Set the current directory to the current directory
    current_directory = os.path.dirname(sys.argv[0])
    # Convert to a string
    directory = str(current_directory)
    # Open the current file in file explorer
    os.startfile(directory)
    # Set the help directory to the current plus the help text file
    help_directory = directory + "\\restore_backup_help.txt"
    # Open the help text in notepad
    os.startfile(help_directory)
    # Set the backup directory to the backup folder
    backup_directory = directory + "\\backup"
    # Open the backup directory in file explorer
    os.startfile(backup_directory)
    # Call the quit function to soft quit the program
    quit_function()
    # Quit the whole of Python
    exit()


# Main menu for teachers
def teacher_system():
    # Import all global variables needed
    global DONE_RESET_LABEL
    global DONE_BACKUP_LABEL
    global DELETE_USER_LABEL
    global DONE_REMOVE_LABEL
    global ID_MODULE_COMBOBOX
    global ADD_QUESTIONS_LABEL
    global HELP_SECTION_TRACKER
    global DONE_QUESTIONS_LABEL
    global RESET_PASSWORD_LABEL
    global REMOVE_QUESTIONS_LABEL
    global DONE_ADD_QUESTIONS_LABEL
    global VIEW_STUDENT_PROGRESS_LABEL
    # Set the help window to the sixth
    HELP_SECTION_TRACKER = 6
    # Call the help storage function
    help_storage()
    # Move the logout button on screen
    logout_button.place(x=225, y=550)
    # Move all the function buttons on screen as well as informative teacher label
    delete_user_button.place(x=450, y=250)
    save_backup_button.place(x=300, y=300)
    teacher_section_label.place(x=225, y=10)
    initial_choice_label.place(x=300, y=130)
    add_questions_button.place(x=250, y=250)
    restore_backup_button.place(x=400, y=300)
    change_password_button.place(x=300, y=200)
    remove_questions_button.place(x=350, y=250)
    view_student_progress_button.place(x=400, y=200)
    # Move all unnecessary items out of the way
    id_field.place(x=3000, y=3000)
    slogo_label.place(x=3000, y=3000)
    id_delete_field.place(x=3000, y=3000)
    logging_in_label.place(x=3000, y=3000)
    login_error_label.place(x=3000, y=3000)
    id_questions_field.place(x=3000, y=3000)
    remove_user_button.place(x=3000, y=3000)
    back_teacher_button.place(x=3000, y=3000)
    submit_login_button.place(x=3000, y=3000)
    back_welcome_button.place(x=3000, y=3000)
    add_questions_field.place(x=3000, y=3000)
    back_teacher_button.place(x=3000, y=3000)
    reset_password_field.place(x=3000, y=3000)
    login_username_field.place(x=3000, y=3000)
    login_password_field.place(x=3000, y=3000)
    reset_password_button.place(x=3000, y=3000)
    username_password_label.place(x=3000, y=3000)
    add_questions_submit_button.place(x=3000, y=3000)
    remove_questions_continue_button.place(x=3000, y=3000)
    add_questions_german_checkbutton.place(x=3000, y=3000)
    add_questions_spanish_checkbutton.place(x=3000, y=3000)
    # First error bypass
    try:
        # Move add questions stuff out of the way
        ADD_QUESTIONS_LABEL.place(x=3000, y=3000)
        DONE_ADD_QUESTIONS_LABEL.place(x=3000, y=3000)
    # If they are not in the add questions section
    except NameError:
        # Move on
        pass
    # Second error bypass
    try:
        # Move the reset password stuff out of the way
        RESET_PASSWORD_LABEL.place(x=3000, y=3000)
        DONE_RESET_LABEL.place(x=3000, y=3000)
    # If they are not in the reset password section
    except NameError:
        # Move on
        pass
    # Third error bypass
    try:
        # Move the view student progress label out of the way
        VIEW_STUDENT_PROGRESS_LABEL.place(x=3000, y=3000)
    # If they are not in the view student progress section
    except NameError:
        # Move on
        pass
    # Fourth error bypass
    try:
        # Move the backup labels out of the way
        DONE_BACKUP_LABEL.place(x=3000, y=3000)
    # If they are not in the backup section
    except NameError:
        # Move on
        pass
    # Fifth error bypass
    try:
        # Move the delete user labels out of the way
        DELETE_USER_LABEL.place(x=3000, y=3000)
        DONE_REMOVE_LABEL.place(x=3000, y=3000)
    # If they are not in the delete user section
    except NameError:
        # Move on
        pass
    # Sixth error bypass
    try:
        # Move the question set labels out of the way
        REMOVE_QUESTIONS_LABEL.place(x=3000, y=3000)
        ID_MODULE_COMBOBOX.place(x=3000, y=3000)
        DONE_QUESTIONS_LABEL.place(x=3000, y=3000)
    # If they are not in the question set section
    except NameError:
        # Move on
        pass

###############
# Help System #
###############


# Help function to display help message once help_storage has checked if the window is open
def help_function():
    # Imports the global variables needed for the function
    global HELP_TEXT_LABEL
    global HELP_SECTION_TRACKER
    global HELP_WINDOW_OPEN_BOOL
    # Sets the help window open boolean to true if not already to track when it is open
    HELP_WINDOW_OPEN_BOOL = True
    # Sets the Help Window dimensions with packing to avoid overlap from main program
    help_window.geometry("300x600+803+2")
    # Creates a close button which calls the function close() on click
    close_button = Button(help_window, text="CLOSE", command=close, bg="white", width="6", height="1")
    close_button.config(font=("Lucida Sans", 8, "bold"))
    # Places the close button at the bottom middle of the help window
    close_button.place(x=130, y=550)
    # Try/except statement in case the label has not already been made
    try:
        # Places the current label out of the way so as not to overlap with the new one
        HELP_TEXT_LABEL.place(x=3000, y=3000)
    # If there is a name error, i.e: not made yet
    except NameError:
        # Then continue on in the function
        pass
    # Place the help window label at the top middle
    help_label.place(x=47, y=10)
    # Place the help button which was on the main gui out of the way so as to avoid multiple help windows
    help_button.place(x=3000, y=3000)
    # If the user is in the main menu
    if HELP_SECTION_TRACKER == 0:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''You are currently in the main menu. In
this section you have two choices. You
can either login if you already have an
account, or you can register by clicking
the corresponding button. Please note
you will have to remember your
password. Once you have done this you
will be able to login. At the bottom you
should also see buttons to quit the
application, go back if you need to, and
on this window close the help window.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the user is in the register section
    elif HELP_SECTION_TRACKER == 1:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''You are currently in the register section.
In this section you have two boxes to
fill. Your username that will be displayed
on leader boards, and password which
you will have to remember. When you
have filled these in simply press SUBMIT
and you will be taken to the login
section and your account
has been made.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the user is in the login section
    elif HELP_SECTION_TRACKER == 2:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''You are currently in the login section.
In this section you have to enter your
username you originally chose and the
password as well. If you forget your
password ask your teacher to reset it.
Once you have filled it in click SUBMIT or
press enter and you will sign in.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        HELP_TEXT_LABEL.place(x=10, y=100)
    elif HELP_SECTION_TRACKER == 3:
        HELP_TEXT_LABEL = Label(help_window, text='''You have logged in successfully.
Now in this section you have to choose
what language you are going to be
learning or practicing. You will now
also be able to see a leader board
button at the bottom which displays
the top 5 learners of each class.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the user is choosing a module
    elif HELP_SECTION_TRACKER == 4:
        # Display the relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''You now have a choice of which module
of your language you will choose. The
program provides three basic ones or
you can choose from the drop down
menu modules that your teacher has
added. Simply click the rectangle and it
will provide you which the options.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the user has chosen a module
    elif HELP_SECTION_TRACKER == 5:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''Now that you have chosen a module you
are now presented with two options.
The first mode is learn mode where you
can spend as long as you want to
practice the words. You will be told
where you went wrong so that you can
improve. The other mode is arcade mode
which has a 60 second timer and you do
not receive any feedback to make it as
quick as possible.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # These are now for teachers, if the teacher is in the main teacher menu
    elif HELP_SECTION_TRACKER == 6:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''You are now in the teacher section.
In this section you have 7 options to
choose from.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the teacher is in the list progress module
    elif HELP_SECTION_TRACKER == 7:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''This is a basic module which you
can use to see the ids of each student.
You will be able to use this when
changing user passwords and when
deleting users.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the teacher is in the change password module
    elif HELP_SECTION_TRACKER == 8:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''This is the change password module.
You should use the list progress button
on the previous section to check the id
of the student you want to reset their
password.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the teacher is in the add questions module
    elif HELP_SECTION_TRACKER == 9:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''This is the add questions function.
You should see a notepad opened up on
your screen. Follow the on screen
instructions and make sure to only
select either spanish or german.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the teacher is in the remove questions function
    elif HELP_SECTION_TRACKER == 10:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''This is the remove questions
function. Like with other functions
simply follow the instructions and
select the id of the question set
that you would like to remove. Type
it in and then submit. It will
automatically be removed.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the teacher is in the delete user function
    elif HELP_SECTION_TRACKER == 11:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''This is the delete user function.
This will delete any user in the
database. Simply find the user's ID
and enter it. Then submit and it
will be deleted.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the teacher is in the save backup section
    elif HELP_SECTION_TRACKER == 12:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''This is the save backup function.
This will save a backup automatically
so that nothing is lost in the
database. Make sure to do this
regularly.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)
    # If the teacher somehow fails to close the program and the help window is still open
    elif HELP_SECTION_TRACKER == 13:
        # Display relevant help text
        HELP_TEXT_LABEL = Label(help_window, text='''This is the restore backup
function. This will open lots of
things but it is pretty easy.
Essentially read the notepad
that has been opened.''', font=("Lucida Sans", 10, "bold"), bd=3, bg="orange", fg="white")
        # Place the text in the center below the header
        HELP_TEXT_LABEL.place(x=10, y=100)


# A procedure to check whether the Help Window is open
def help_storage():
    # First imports the boolean as a global variable
    global HELP_WINDOW_OPEN_BOOL
    # Uses Try/Except statement to avoid expected errors if Boolean is not defined yet in the program
    try:
        # If the help window is open
        if HELP_WINDOW_OPEN_BOOL:
            # Then call the help function
            help_function()
    # If there is a name error
    except NameError:
        # Then continue in the program
        pass


# This defines the module close which closes the help window
def close():
    # Imports the global variable help window open boolean
    global HELP_WINDOW_OPEN_BOOL
    # Sets the boolean to false as it will now be closed
    HELP_WINDOW_OPEN_BOOL = False
    # Displaces the help window due to the lack of a better method
    help_window.geometry("300x600+3000+3000")
    # Places the help button back to the main gui so that the help window can be opened again
    help_button.place(x=405, y=550)
    
#######################
# SQLite3 connections #
#######################


# If the login details file is not found
if not os.path.isfile('login_details.db'):
    # Imports my own library to create the Login Details database
    from database_creation import create
    # Call the function
    create()

# If the question sets file is not found
if not os.path.isfile('question_sets.db'):
    # Imports my own library to create the Question Sets database
    from question_database_creation import create1
    # Call the function
    create1()

# Set the login details connection
connection = connect('login_details.db')
# Create a cursor for the database
connection_cursor = connection.cursor()

# Set the question sets connection
question_connection = connect('question_sets.db')
# Create a cursor for the connection
question_connection_cursor = question_connection.cursor()

###################
# Windows Go Here #
###################

# Set the window to a Tkinter module
main_gui = Tk()
# Set the title at the top
main_gui.title("Memrize  -  By Ethan Champion")
# Set the window size
main_gui.geometry("800x600+2+2")
# Set the background to orange
main_gui.configure(background="orange")
# Make it not resizable
main_gui.resizable(0, 0)
# Set it so they can't resize
main_gui.overrideredirect(True)
# Move it to front immediately
main_gui.lift()

# Set the help window to a top level version of the main window
help_window = Toplevel(main_gui)
# Set the title at the top
help_window.title("Help Window")
# Set the window size
help_window.geometry("300x600+3000+3000")
# Set the background to orange
help_window.configure(background="orange")
# Make it not resizable
help_window.resizable(0, 0)
# Set it so they can't resize
help_window.overrideredirect(True)

# Set the leader board window to a top level version of the main window
leader_board_window = Toplevel(main_gui)
# Set the title at the top
leader_board_window.title("Leader board")
# Set the window size
leader_board_window.geometry("500x600+3000+3000")
# Set the background to orange
leader_board_window.configure(background="orange")
# Make it not resizable
leader_board_window.resizable(0, 0)
# Set it so they can't resize
leader_board_window.overrideredirect(True)

##################
# Labels Go Here #
##################

global DIRECTORY
DIRECTORY = os.path.dirname(sys.argv[0])

# Sets the photo path
photo_path = DIRECTORY + r"\images\slogo.gif"
# Defines the Photo to put on image
slogo_image = PhotoImage(file=photo_path)
# Creates label with that image
slogo_label = Label(main_gui, image=slogo_image)
# Places label in right place
slogo_label.place(x=205, y=10)

# Sets the photo path
photo_path = DIRECTORY + r"\images\options.gif"
# Defines the Photo to put on image
initial_choice_image = PhotoImage(file=photo_path)
# Creates label with that image
initial_choice_label = Label(main_gui, image=initial_choice_image)
# Places label in right place
initial_choice_label.place(x=300, y=150)

# Sets the photo path
photo_path = DIRECTORY + r"\images\teacher_section.gif"
# Defines the Photo to put on image
teacher_section_image = PhotoImage(file=photo_path)
# Creates label with that image
teacher_section_label = Label(main_gui, image=teacher_section_image)
# Places label in right place
teacher_section_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\username_password.gif"
# Defines the Photo to put on image
username_password_image = PhotoImage(file=photo_path)
# Creates label with that image
username_password_label = Label(main_gui, image=username_password_image)
# Places label in right place
username_password_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\help_page.gif"
# Defines the Photo to put on image
help_image = PhotoImage(file=photo_path)
# Creates label with that image
help_label = Label(help_window, image=help_image)
# Places label in right place
help_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\leader_board.gif"
# Defines the Photo to put on image
leader_board_image = PhotoImage(file=photo_path)
# Creates label with that image
leader_board_label = Label(leader_board_window, image=leader_board_image)
# Places label in right place
leader_board_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\username_taken.gif"
# Defines the Photo to put on image
username_taken_image = PhotoImage(file=photo_path)
# Creates label with that image
username_taken_label = Label(main_gui, image=username_taken_image)
# Places label in right place
username_taken_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\username_length.gif"
# Defines the Photo to put on image
username_length_image = PhotoImage(file=photo_path)
# Creates label with that image
username_length_label = Label(main_gui, image=username_length_image)
# Places label in right place
username_length_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\password_error.gif"
# Defines the Photo to put on image
password_error_image = PhotoImage(file=photo_path)
# Creates label with that image
password_error_label = Label(main_gui, image=password_error_image)
# Places label in right place
password_error_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\logging_in.gif"
# Defines the Photo to put on image
logging_in_image = PhotoImage(file=photo_path)
# Creates label with that image
logging_in_label = Label(main_gui, image=logging_in_image)
# Places label in right place
logging_in_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\registered.gif"
# Defines the Photo to put on image
registered_image = PhotoImage(file=photo_path)
# Creates label with that image
registered_label = Label(main_gui, image=registered_image)
# Places label in right place
registered_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\login_error.gif"
# Defines the Photo to put on image
login_error_image = PhotoImage(file=photo_path)
# Creates label with that image
login_error_label = Label(main_gui, image=login_error_image)
# Places label in right place
login_error_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\welcome_back.gif"
# Defines the Photo to put on image
welcome_back_image = PhotoImage(file=photo_path)
# Creates label with that image
welcome_back_label = Label(main_gui, image=welcome_back_image)
# Places label in right place
welcome_back_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\spanish_zone.gif"
# Defines the Photo to put on image
spanish_zone_image = PhotoImage(file=photo_path)
# Creates label with that image
spanish_zone_label = Label(main_gui, image=spanish_zone_image)
# Places label in right place
spanish_zone_label.place(x=3000, y=3000)

# Sets the photo path
photo_path = DIRECTORY + r"\images\german_zone.gif"
# Defines the Photo to put on image
german_zone_image = PhotoImage(file=photo_path)
# Creates label with that image
german_zone_label = Label(main_gui, image=german_zone_image)
# Places label in right place
german_zone_label.place(x=3000, y=3000)

###################
# Entries go here #
###################

# Set the field to an Entry box
new_username_field = Entry(main_gui)
# Place in right place
new_username_field.place(x=3000, y=3000)

# Set the field to an Entry box and only show * when user types
new_password_field = Entry(main_gui, show="*")
# Place in right place
new_password_field.place(x=3000, y=3000)

# Set the field to an Entry box
login_username_field = Entry(main_gui)
# Place in right place
login_username_field.place(x=3000, y=3000)

# Set the field to an Entry box and only show * when user types
login_password_field = Entry(main_gui, show="*")
# Place in right place
login_password_field.place(x=3000, y=3000)

# Set the field to an Entry box
spanish_learn_entry = Entry(main_gui, width=40)
# Place in right place
spanish_learn_entry.place(x=3000, y=3000)

# Set the field to an Entry box
german_learn_entry = Entry(main_gui, width=40)
# Place in right place
german_learn_entry.place(x=3000, y=3000)

# Set the field to an Entry box
id_field = Entry(main_gui)
# Place in right place
id_field.place(x=3000, y=3000)

# Set the field to an Entry box
id_delete_field = Entry(main_gui)
# Place in right place
id_delete_field.place(x=3000, y=3000)

# Set the field to an Entry box
id_questions_field = Entry(main_gui)
# Place in right place
id_questions_field.place(x=3000, y=3000)

# Set the field to an Entry box
reset_password_field = Entry(main_gui)
# Place in right place
reset_password_field.place(x=3000, y=3000)

# Set the field to an Entry box
add_questions_field = Entry(main_gui)
# Place in right place
add_questions_field.place(x=3000, y=3000)

# Create a Tkinter Integer variable
spanish_module_add = IntVar()
# Create a check button with that variable
add_questions_spanish_checkbutton = Checkbutton(main_gui, variable=spanish_module_add, bg="orange")
# Place in right place
add_questions_spanish_checkbutton.place(x=3000, y=3000)

# Create a Tkinter Integer variable
german_module_add = IntVar()
# Create a check button with that variable
add_questions_german_checkbutton = Checkbutton(main_gui, variable=german_module_add, bg="orange")
# Place in right place
add_questions_german_checkbutton.place(x=3000, y=3000)

###################
# Buttons go here #
###################

# Define the button with the right text that calls a function/procedure
quit_button = Button(main_gui, text="QUIT", command=quit_function, bg="white", width="5", height="1")
# Set the default config options
quit_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
quit_button.place(x=352, y=550)
# Make it pop out
quit_button.flash()

# Define the button with the right text that calls a function/procedure
help_button = Button(main_gui, text="HELP", command=help_function, bg="white", width="5", height="1")
# Set the default config options
help_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
help_button.place(x=405, y=550)
# Make it pop out
help_button.flash()

# Define the button with the right text that calls a function/procedure
back_welcome_button = Button(main_gui, text="BACK", command=main_window, bg="white", width="5", height="1")
# Set the default config options
back_welcome_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
back_welcome_button.place(x=3000, y=3000)
# Make it pop out
back_welcome_button.flash()

# Define the button with the right text that calls a function/procedure
back_learn_button = Button(main_gui, text="BACK", command=main_learn, bg="white", width="5", height="1")
# Set the default config options
back_learn_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
back_learn_button.place(x=3000, y=3000)
# Make it pop out
back_learn_button.flash()

# Define the button with the right text that calls a function/procedure
back_teacher_button = Button(main_gui, text="BACK", command=teacher_system, bg="white", width="5", height="1")
# Set the default config options
back_teacher_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
back_teacher_button.place(x=3000, y=3000)
# Make it pop out
back_teacher_button.flash()

# Define the button with the right text that calls a function/procedure
register_button = Button(main_gui, text="REGISTER", command=initial_register, bg="white", width="9", height="2")
# Set the default config options
register_button.config(font=("Lucida Sans", 12, "bold"))
# Place in right place
register_button.place(x=300, y=220)
# Make it pop out
register_button.flash()

# Define the button with the right text that calls a function/procedure
login_button = Button(main_gui, text="LOGIN", command=initial_login, bg="white", width="8", height="2")
# Set the default config options
login_button.config(font=("Lucida Sans", 12, "bold"))
# Place in right place
login_button.place(x=410, y=220)
# Make it pop out
login_button.flash()

# Define the button with the right text that calls a function/procedure
submit_register_button = Button(main_gui, text="SUBMIT", command=submit_register, bg="white", width="7", height="2")
# Set the default config options
submit_register_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
submit_register_button.place(x=3000, y=3000)
# Make it pop out
submit_register_button.flash()

# Define the button with the right text that calls a function/procedure
submit_login_button = Button(main_gui, text="SUBMIT", command=submit_login, bg="white", width="7", height="2")
# Set the default config options
submit_login_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
submit_login_button.place(x=3000, y=3000)
# Make it pop out
submit_login_button.flash()

# Define the button with the right text that calls a function/procedure
spanish_learn_button = Button(main_gui, text="SPANISH", command=spanish_modules, bg="white", width="9", height="2")
# Set the default config options
spanish_learn_button.config(font=("Lucida Sans", 12, "bold"))
# Place in right place
spanish_learn_button.place(x=3000, y=3000)
# Make it pop out
spanish_learn_button.flash()

# Define the button with the right text that calls a function/procedure
german_learn_button = Button(main_gui, text="GERMAN", command=german_modules, bg="white", width="9", height="2")
# Set the default config options
german_learn_button.config(font=("Lucida Sans", 12, "bold"))
# Place in right place
german_learn_button.place(x=3000, y=3000)
# Make it pop out
german_learn_button.flash()

# Define the button with the right text that calls a function/procedure
spanish_learn_mode_button = Button(main_gui, text="LEARN MODE", command=spanish_learn_mode, bg="white", width="12",
                                   height="3")
# Set the default config options
spanish_learn_mode_button.config(font=("Lucida Sans", 10, "bold"))
# Place in right place
spanish_learn_mode_button.place(x=3000, y=3000)
# Make it pop out
spanish_learn_mode_button.flash()

# Define the button with the right text that calls a function/procedure
spanish_arcade_button = Button(main_gui, text="ARCADE MODE", command=spanish_arcade, bg="white", width="14", height="3")
# Set the default config options
spanish_arcade_button.config(font=("Lucida Sans", 10, "bold"))
# Place in right place
spanish_arcade_button.place(x=3000, y=3000)
# Make it pop out
spanish_arcade_button.flash()

# Define the button with the right text that calls a function/procedure
german_learn_mode_button = Button(main_gui, text="LEARN MODE", command=german_learn_mode, bg="white", width="12",
                                  height="3")
# Set the default config options
german_learn_mode_button.config(font=("Lucida Sans", 10, "bold"))
# Place in right place
german_learn_mode_button.place(x=3000, y=3000)
# Make it pop out
german_learn_mode_button.flash()

# Define the button with the right text that calls a function/procedure
german_arcade_button = Button(main_gui, text="ARCADE MODE", command=german_arcade, bg="white", width="14", height="3")
# Set the default config options
german_arcade_button.config(font=("Lucida Sans", 10, "bold"))
# Place in right place
german_arcade_button.place(x=3000, y=3000)
# Make it pop out
german_arcade_button.flash()

# Define the button with the right text that calls a function/procedure
spanish_arcade_start_button = Button(main_gui, text="START", command=spanish_arcade_mode, bg="white", width="7",
                                     height="2")
# Set the default config options
spanish_arcade_start_button.config(font=("Lucida Sans", 10, "bold"))
# Place in right place
spanish_arcade_start_button.place(x=3000, y=3000)
# Make it pop out
spanish_arcade_start_button.flash()

# Define the button with the right text that calls a function/procedure
german_arcade_start_button = Button(main_gui, text="START", command=german_arcade_mode, bg="white", width="7",
                                    height="2")
# Set the default config options
german_arcade_start_button.config(font=("Lucida Sans", 10, "bold"))
# Place in right place
german_arcade_start_button.place(x=3000, y=3000)
# Make it pop out
german_arcade_start_button.flash()

# Define the button with the right text that calls a function/procedure
leader_board_button = Button(main_gui, text="LEADER-BOARD", command=leader_board, bg="white", width="13",
                             height="1")
# Set the default config options
leader_board_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
leader_board_button.place(x=3000, y=3000)
# Make it pop out
leader_board_button.flash()

# Define the button with the right text that calls a function/procedure
logout_button = Button(main_gui, text="LOGOUT", command=logout, bg="white", width="8", height="1")
# Set the default config options
logout_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
logout_button.place(x=3000, y=3000)
# Make it pop out
logout_button.flash()

# Define the button with the right text that calls a function/procedure
spanish_continue_button = Button(main_gui, text="CONTINUE", command=spanish_learn_mode, bg="white", width="9",
                                 height="2")
# Set the default config options
spanish_continue_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
spanish_continue_button.place(x=3000, y=3000)
# Make it pop out
spanish_continue_button.flash()

# Define the button with the right text that calls a function/procedure
german_continue_button = Button(main_gui, text="CONTINUE", command=german_learn_mode, bg="white", width="9",
                                height="2")
# Set the default config options
german_continue_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
german_continue_button.place(x=3000, y=3000)
# Make it pop out
german_continue_button.flash()

# Define the button with the right text that calls a function/procedure
remove_questions_continue_button = Button(main_gui, text="CONTINUE", command=remove_questions_process, bg="white",
                                          width="9", height="2")
# Set the default config options
remove_questions_continue_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
remove_questions_continue_button.place(x=3000, y=3000)
# Make it pop out
remove_questions_continue_button.flash()

# Define the button with the right text that calls a function/procedure
o_accent_button = Button(main_gui, text="ó", command=o_accent, bg="white", width="2", height="1")
# Set the default config options
o_accent_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
o_accent_button.place(x=3000, y=3000)
# Make it pop out
o_accent_button.flash()

# Define the button with the right text that calls a function/procedure
i_accent_button = Button(main_gui, text="í", command=i_accent, bg="white", width="2", height="1")
# Set the default config options
i_accent_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
i_accent_button.place(x=3000, y=3000)
# Make it pop out
i_accent_button.flash()

# Define the button with the right text that calls a function/procedure
e_accent_button = Button(main_gui, text="é", command=e_accent, bg="white", width="2", height="1")
# Set the default config options
e_accent_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
e_accent_button.place(x=3000, y=3000)
# Make it pop out
e_accent_button.flash()

# Define the button with the right text that calls a function/procedure
upside_down_question_mark_button = Button(main_gui, text="¿", command=upside_down_question_mark, bg="white", width="2",
                                          height="1")
# Set the default config options
upside_down_question_mark_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
upside_down_question_mark_button.place(x=3000, y=3000)
# Make it pop out
upside_down_question_mark_button.flash()

# Define the button with the right text that calls a function/procedure
n_accent_button = Button(main_gui, text="ñ", command=n_accent, bg="white", width="2", height="1")
# Set the default config options
n_accent_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
n_accent_button.place(x=3000, y=3000)
# Make it pop out
n_accent_button.flash()

# Define the button with the right text that calls a function/procedure
u_accent_button = Button(main_gui, text="ú", command=u_accent, bg="white", width="2", height="1")
# Set the default config options
u_accent_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
u_accent_button.place(x=3000, y=3000)
# Make it pop out
u_accent_button.flash()

# Define the button with the right text that calls a function/procedure
a_accent_button = Button(main_gui, text="á", command=a_accent, bg="white", width="2", height="1")
# Set the default config options
a_accent_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
a_accent_button.place(x=3000, y=3000)
# Make it pop out
a_accent_button.flash()

# Define the button with the right text that calls a function/procedure
a_umlaut_button = Button(main_gui, text="ä", command=a_umlaut, bg="white", width="2", height="1")
# Set the default config options
a_umlaut_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
a_umlaut_button.place(x=3000, y=3000)
# Make it pop out
a_umlaut_button.flash()

# Define the button with the right text that calls a function/procedure
u_umlaut_button = Button(main_gui, text="ü", command=u_umlaut, bg="white", width="2", height="1")
# Set the default config options
u_umlaut_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
u_umlaut_button.place(x=3000, y=3000)
# Make it pop out
u_umlaut_button.flash()

# Define the button with the right text that calls a function/procedure
scharfes_button = Button(main_gui, text="ß", command=scharfes, bg="white", width="2", height="1")
# Set the default config options
scharfes_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
scharfes_button.place(x=3000, y=3000)
# Make it pop out
scharfes_button.flash()

# Define the button with the right text that calls a function/procedure
spanish_submit_button = Button(main_gui, text="SUBMIT", command=spanish_learn_process, bg="white", width="9",
                               height="2")
# Set the default config options
spanish_submit_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
spanish_submit_button.place(x=3000, y=3000)
# Make it pop out
spanish_submit_button.flash()

# Define the button with the right text that calls a function/procedure
german_submit_button = Button(main_gui, text="SUBMIT", command=german_learn_process, bg="white", width="9", height="2")
# Set the default config options
german_submit_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
german_submit_button.place(x=3000, y=3000)
# Make it pop out
german_submit_button.flash()

# Define the button with the right text that calls a function/procedure
view_student_progress_button = Button(main_gui, text="LIST OF\nPROGRESS", command=view_student_progress, bg="white",
                                      width="12", height="3")
# Set the default config options
view_student_progress_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
view_student_progress_button.place(x=3000, y=3000)
# Make it pop out
view_student_progress_button.flash()

# Define the button with the right text that calls a function/procedure
change_password_button = Button(main_gui, text="CHANGE\nPASSWORD", command=change_password, bg="white", width="12",
                                height="3")
# Set the default config options
change_password_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
change_password_button.place(x=3000, y=3000)
# Make it pop out
change_password_button.flash()

# Define the button with the right text that calls a function/procedure
add_questions_button = Button(main_gui, text="ADD\nQUESTIONS", command=add_questions, bg="white", width="12",
                              height="3")
# Set the default config options
add_questions_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
add_questions_button.place(x=3000, y=3000)
# Make it pop out
add_questions_button.flash()

# Define the button with the right text that calls a function/procedure
remove_questions_button = Button(main_gui, text="REMOVE\nQUESTIONS", command=remove_questions, bg="white", width="12",
                                 height="3")
# Set the default config options
remove_questions_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
remove_questions_button.place(x=3000, y=3000)
# Make it pop out
remove_questions_button.flash()

# Define the button with the right text that calls a function/procedure
delete_user_button = Button(main_gui, text="DELETE\nUSER", command=delete_user, bg="white", width="12", height="3")
# Set the default config options
delete_user_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
delete_user_button.place(x=3000, y=3000)
# Make it pop out
delete_user_button.flash()

# Define the button with the right text that calls a function/procedure
save_backup_button = Button(main_gui, text="SAVE\nBACKUP", command=save_backup, bg="white", width="12", height="3")
# Set the default config options
save_backup_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
save_backup_button.place(x=3000, y=3000)
# Make it pop out
save_backup_button.flash()

# Define the button with the right text that calls a function/procedure
restore_backup_button = Button(main_gui, text="RESTORE\nBACKUP", command=restore_backup, bg="white", width="12",
                               height="3")
# Set the default config options
restore_backup_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
restore_backup_button.place(x=3000, y=3000)
# Make it pop out
restore_backup_button.flash()

# Define the button with the right text that calls a function/procedure
reset_password_button = Button(main_gui, text="RESET", command=reset_password_process, bg="white", width="7",
                               height="2")
# Set the default config options
reset_password_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
reset_password_button.place(x=3000, y=3000)
# Make it pop out
reset_password_button.flash()

# Define the button with the right text that calls a function/procedure
remove_user_button = Button(main_gui, text="REMOVE\nUSER", command=remove_user_process, bg="white", width="7",
                            height="2")
# Set the default config options
remove_user_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
remove_user_button.place(x=3000, y=3000)
# Make it pop out
remove_user_button.flash()

# Define the button with the right text that calls a function/procedure
module_german_continue_button = Button(main_gui, text="CONTINUE", command=german_module_selected, bg="white", width="9",
                                       height="2")
# Set the default config options
module_german_continue_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
module_german_continue_button.place(x=3000, y=3000)
# Make it pop out
module_german_continue_button.flash()

# Define the button with the right text that calls a function/procedure
module_spanish_continue_button = Button(main_gui, text="CONTINUE", command=spanish_module_selected, bg="white",
                                        width="9", height="2")
# Set the default config options
module_spanish_continue_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
module_spanish_continue_button.place(x=3000, y=3000)
# Make it pop out
module_spanish_continue_button.flash()

# Define the button with the right text that calls a function/procedure
add_questions_submit_button = Button(main_gui, text="CONTINUE", command=submit_question_set, bg="white", width="9",
                                     height="2")
# Set the default config options
add_questions_submit_button.config(font=("Lucida Sans", 8, "bold"))
# Place in right place
add_questions_submit_button.place(x=3000, y=3000)
# Make it pop out
add_questions_submit_button.flash()

############################
# Initialising the Program #
############################

# Call the main window function
main_window()
# Start the main loop of the Tkinter window
main_gui.mainloop()
