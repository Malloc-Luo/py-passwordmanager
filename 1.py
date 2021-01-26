# -*- coding: utf-8 -*-

from __future__ import print_function
import ctypes, sys, os
import winreg


REG_PATH = r'.DEFAULT\Software\pymanager'

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    hkey = winreg.OpenKey(winreg.HKEY_USERS, r'.DEFAULT\Software')
    newkey = winreg.CreateKey(hkey, 'pyManager')
    # newkey = winreg.CreateKey(winreg.HKEY_USERS, REG_PATH)
    winreg.SetValue(newkey, "ValueName", 0, "ValueContent")
    print('set value successfully')
else:
    if sys.version_info[0] == 3:
        s = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        print(s)
    else:  #in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

