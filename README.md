# SimpleToDoList V0.5

Extremely barebones thing bcuz I couldnt find an todolist with the like 2 features I want on the internet so made my own ig

# Can:
- Plan with checklists
- Always have priorty over other applications (excluding fullscreen ones like games, etc). This means the application will always stay on top so you can always see what you need to do i guess.
[This is also toggleable in menu]
- Close to System Tray (enabled by default, make sure to click "Exit" to actually quit or disable the system tray option in the menu)
- Save tasks when program is closed

# Can't:
- Make super complex daily plans with 50 projects happening simultaneously, this is supposed to be simple for the average person
- resize window L
- most likely will only work properly on Windows because i havent tested on any other platform SORRY!



compile command: pyinstaller --noconfirm --onedir --windowed --icon "icon.ico" --add-data "icon.ico;." --add-data "icon.png;." --add-data "save.TXT;." --hidden-import "pystray._win32" "todo.py"
