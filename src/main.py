import time
import traceback
from pathlib import Path

import pythoncom
import win32com
import win32gui
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from win32com.client import Dispatch

data = {}
# toaster = ToastNotifier()


def activate_window(key):
    if key in data:
        window = data[key]
        pythoncom.CoInitialize()
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(window)


def set_window(key):
    window = win32gui.GetForegroundWindow()
    if window:
        # if toaster.show_toast("Window Keybinds", f"Bound window to key: {key}", duration=2, threaded=True):
        data[key] = window


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        with open(event.src_path) as f:
            msg = f.read().strip()
            if not msg:
                return
            try:
                parts = msg.split()
                action = parts[0]
                key = int(parts[1])
                if action == 'a':
                    activate_window(key)
                elif action == 's':
                    set_window(key)
            except:
                traceback.print_exc()


if __name__ == "__main__":
    Path('data').mkdir(exist_ok=True)
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, 'data')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
