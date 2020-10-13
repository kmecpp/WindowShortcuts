import shutil
from pathlib import Path

import winshell

AHK_FILE = 'WindowShortcuts.ahk'

startup = Path(winshell.startup())
shutil.copy(AHK_FILE, startup / AHK_FILE)
# TODO: Create windows shortcut
