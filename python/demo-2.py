"""
This files demonstrates using the menu of an untitled Notepad file using PyWinAuto, a Python library that allows Windows UI Automation.

Warning: 
The program WILL throw an error if:
- An instance of Notepad is already open
- Opened Notepad file is NOT a blank untitled file.

Environment:
- VS Code 1.84.2
- Python 3.10.6
- PyWinAuto 0.6.8
"""

from pywinauto.application import Application
import time
from pywinauto import timings
from pywinauto import ElementNotFoundError


# timings.Timings.slow()

try:
    # Start Notepad using UIA
    app = Application(backend='uia').start('notepad.exe')
    time.sleep(1) # Allow time for Notepad to start

    # Connect to the Notepad window
    notepad_app = app.window(title_re='Untitled - Notepad')

    # Print the identifiers to the console
    # notepad_app.UntitledNotepad.print_control_identifiers()
    
    # Save the file
    notepad_app.menu_select("File->Save") # Takes the path to the menu item, separated by '->', allows spaces

    # Work out error/exception handling
    print("\nsuccess!")
except timings.TimeoutError as exc:
    print("\nTimeout issues:", exc)
except ElementNotFoundError as en:
    print("\nElement not found:", en)
except Exception as e:
    print("\nOther exception:", e)
