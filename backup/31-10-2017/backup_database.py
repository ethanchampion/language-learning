import datetime
import os
import sys
import shutil

def get_backup_directory(base_directory):
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    return base_directory.format(date)

def copy_files_to(srcdir, dstdir):
    for file in os.listdir(srcdir):
        file_path = os.path.join(srcdir, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dstdir)

def copy_files(dstdir,directory):
    copy_files_to(directory, dstdir)

def perform_backup(base_directory,directory):
    backup_directory = get_backup_directory(base_directory)
    try:
        os.makedirs(backup_directory)
    except WindowsError:
        quit
    copy_files(backup_directory,directory)

backup_directory = os.path.dirname(sys.argv[0])
directory = backup_directory
directory += '/'
backup_directory += '/backup/'
date = datetime.datetime.now().strftime('%d-%m-%Y')
backup_directory += date
perform_backup(backup_directory,directory)
