import keyboard
import pythoncom
import win32com
import win32gui
from win10toast import ToastNotifier
from win32com.client import Dispatch

data = {}
toaster = ToastNotifier()


def on_window_set(key):
    window = win32gui.GetForegroundWindow()
    if window:
        if toaster.show_toast("Window Keybinds", f"Bound window to key: {key}", duration=2, threaded=True):
            data[key] = window


def on_window_activate(key):
    if key in data:
        window = data[key]
        pythoncom.CoInitialize()
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(window)


for i in range(10):
    keyboard.add_hotkey(f'ctrl+alt+{i}', on_window_set, args=[i])
    keyboard.add_hotkey(f'ctrl+{i}', on_window_activate, args=[i])

keyboard.wait()
