I have been able to get program windows to open with minimal issues (specifically calculator and notepad),
however I have been unsuccessful in any further interactions. Any tutorials do not work. I am unsure if this 
could be a compatability issue between versions or Windows, Python or pywinauto. I have tried to match the Python 
version to a Windows 11 tutorial but no luck. 

Almost all other scripts crash with the following error:
```
pywinauto.findbestmatch.MatchError: Could not find 'UntitledNotepad' in 'dict_keys([])'
```
Is this saying that the dict_list found is empty so the problem is with getting the list? Or is the name wrong?


The only other success I had was printing out the control identifiers:
```
app = Application(backend='uia').start('notepad.exe').connect(title='Untitled - Notepad', timeout=100)
app.UntitledNotepad.print_control_identifiers()
```
I must assume that there has been a change in naming or structure which is causing this issue, so hopefully the 
control identifiers or the inspect tool can help me find a solution.