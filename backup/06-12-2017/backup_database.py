# Import all necessary libraries
import datetime
import os
import sys
import shutil

# Called by main function to add date to string
def get_backup_directory(base_directory):
    # Sets the date to the current time
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    # Returns the new backup directory
    return base_directory.format(date)

# Procedure to copy files from one location to the other
def copy_files_to(srcdir, dstdir):
    # For file found in the current directory
    for file in os.listdir(srcdir):
        # Set the file path to the directory plus the file name
        file_path = os.path.join(srcdir, file)
        # If the file is not found in the new directory
        if os.path.isfile(file_path):
            # Copy the file over
            shutil.copy(file_path, dstdir)

# Procedure to swap variables and call correct function
def copy_files(dstdir,directory):
    # Call the correct function with variables swapped
    copy_files_to(directory, dstdir)

# Main function that is called, takes parameters base directory then directory
def perform_backup(base_directory,directory):
    # Sets the backup directory to the directory outputted from get backup directory function
    backup_directory = get_backup_directory(base_directory)
    # Simple error bypass
    try:
        # Try to make a directory in the path previously created
        os.makedirs(backup_directory)
    # If there are any Windows errors E.G: Not enough priveledge or folder already found etc.
    except WindowsError:
        # Quit the function
        quit
    # Copy all files from directory to backup directory
    copy_files(backup_directory,directory)

# In case teachers run this program seperately from main program:

# Set the backup directory to the current one
backup_directory = os.path.dirname(sys.argv[0])
# Set the directory to the backup one
directory = backup_directory
# Add a / to current directory
directory += '/'
# Add backup to new directory
backup_directory += '/backup/'
# Get the date
date = datetime.datetime.now().strftime('%d-%m-%Y')
# Add the date to backup directory
backup_directory += date
# Perform the backup like before
perform_backup(backup_directory,directory)
