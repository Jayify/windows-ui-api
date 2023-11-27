"""
This files demonstrates writing to a blank untitled Notepad file using PyWinAuto, a Python library that allows Windows UI Automation.

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

try:
    # Start Notepad using UIA
    app = Application(backend='uia').start('notepad.exe')
    time.sleep(1) # Allow time for Notepad to start

    # Connect to the Notepad window
    notepad_app = app.connect(title_re='Untitled - Notepad', timeout=10)

    # Print the identifiers to the console
    # notepad_app.UntitledNotepad.print_control_identifiers()

    # Type some text into Notepad
    notepad_app.UntitledNotepad.Document.type_keys("Hey look it works!", with_spaces = True)

    # Work out error/exception handling
    print("\nsuccess!")
except timings.TimeoutError as exc:
    print("\nTimeout issues:", exc)
except ElementNotFoundError as en:
    print("\nElement not found:", en)
except Exception as e:
    print("\nOther exception:", e)
