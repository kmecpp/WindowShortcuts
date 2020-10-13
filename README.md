# WindowShortcuts
- Adds shortcut keys to assign certain windows to certain shortcut keys

# Permanent Installation
- Download main.py and put it in a permanent spot on your computer
- Shift right click on the file and click "Copy as path"
- Right click on the file and click "Create shortcut" in the menu
- Right click on the shortcut and click "Properties"
- Replace the "Target" field with "pythonw \<path\>" with \<path\> being the path that you copied in step 2
- Type "Windows Key + R", enter "shell:startup" and move your shortcut into that folder
- Right click on the shortcut or restart your computer

# Usage
- "ctrl + alt + \<number key\>" - Assigns the current window to the given number
- "ctrl + \<number key\>" - switch to the window assigned the given number

## TODO: 
- Add keybinds to open or switch to specific folders 
- Permanent keybinds that persist across restarts
- Disable conflicting existing keybinds
- Find a decent keybind library. Current one goes insane when using ctrl alt down, others are annoying or impossible to use with control keys