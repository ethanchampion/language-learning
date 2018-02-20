from cx_Freeze import setup, Executable
import os

base = None

os.environ['TCL_LIBRARY'] = r'C:\Users\DT24\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\DT24\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

executables = [Executable("test.py", base=base)]

packages = ["time"]
options = {
    'build_exe': {
        'packages':packages,
    },

}

setup(
    name = "Memrize Program",
    options = options,
    version = "0.1",
    author = "Ethan",
    description = 'Memrize Program',
    executables = executables
)
