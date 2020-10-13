import os
import shutil
from pathlib import Path

import winshell

AHK_FILE = 'WindowShortcuts.ahk'
MAIN_FILE = 'main.py'

startup = Path(winshell.startup())
AHK_DEST = startup / AHK_FILE
MAIN_DEST = startup / 'window_shortcuts.pyw'

shutil.copy(AHK_FILE, AHK_DEST)
shutil.copy(MAIN_FILE, MAIN_DEST)
os.chdir(str(startup))
os.startfile(str(MAIN_DEST))
os.startfile(str(AHK_DEST))
