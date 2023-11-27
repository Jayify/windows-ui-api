"""
This files demonstrates the navigation of File Explorer using PyWinAuto, a Python library that allows Windows UI Automation.

Warning: 
The program may throw an error if:
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
    # Start File Explorer using UIA
    app = Application(backend='uia').start('explorer.exe')
    time.sleep(1) # Allow time for program to start

    # Connect to the File Explorer window
    explorer_app = app.connect(title_re='Desktop 1', timeout=10)
    
    # Print the identifiers to the console
    # explorer_app.print_control_identifiers()


    # ERROR: Unable to form connection, timeout error
    

    # End program
    print("\nsuccess!")
# Work out error/exception handling
except timings.TimeoutError as exc:
    print("\nTimeout issues:", exc)
except ElementNotFoundError as en:
    print("\nElement not found:", en)
except Exception as e:
    print("\nOther exception:", e)

