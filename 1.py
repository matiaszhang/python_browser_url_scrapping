import win32gui
from win32process import GetWindowThreadProcessId
from pywinauto.application import Application
import time

def is_browser(hwnd):
    flag = 0
    text = win32gui.GetWindowText(hwnd)
    if text.find("Google Chrome") >= 0:
        flag = 1
    elif text.find("Mozilla Firefox") >= 0:
        flag = 2
    elif text.find("Edge") >= 0:
        flag = 3
    elif text.find("Chromium") >= 0:
        flag = 4
    elif text.find("Opera") >= 0:
        flag = 5
    elif text.find("Brave") >= 0:
        flag = 6
    return flag

def get_active_browser_tab_url(browser_flag):
    # tid, pid = GetWindowThreadProcessId(browser_flag)
    tid, pid = GetWindowThreadProcessId(hwnd)
    app = Application(backend="uia").connect(process=pid, time_out=10)
    dlg = app.top_window()
    
    if browser_flag == 1:  # Chrome
        address_bar = "Address and search bar"
    elif browser_flag == 2:  # Firefox
        address_bar = "Search with Google or enter address"
    elif browser_flag == 3:  # Edge
        address_bar = "App bar"
    elif browser_flag == 4:  # Safari
        address_bar = "Address and search bar"
    elif browser_flag == 5:  # Opera
        address_bar = "Address field"
    elif browser_flag == 6:  # Brave
        address_bar = "Address and search bar"
    
    url = dlg.child_window(title=address_bar, control_type="Edit").get_value()
    return url

while True:
    hwnd = win32gui.GetForegroundWindow()
    browser_flag = is_browser(hwnd)
    if browser_flag:
        try:
            url = get_active_browser_tab_url(browser_flag)
            print(url)
        except Exception as e:
            print("Error: ", str(e))
            print("Cannot fetch URL from this tab.")
    time.sleep(2)