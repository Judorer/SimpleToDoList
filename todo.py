import tkinter
import pystray
from PIL import Image, ImageTk

array = []

class checkbox():
    def __init__(self, text):
        self.text = text
        self = tkinter.Checkbutton(root, justify="left", text=self.text, command = lambda : forget(self))
        self.pack(side=tkinter.TOP, anchor=tkinter.NW)
        array.append(self)



root = tkinter.Tk()
root.title("Simple To-Do List")
root.iconphoto(False, tkinter.PhotoImage(file='icon.png'))
root.attributes('-topmost', True)

bool = tkinter.BooleanVar()
bool.set(True)

bool1 = tkinter.BooleanVar()
bool1.set(True)



root.resizable(width=False, height=False)
root.resizable(0, 0)

def exit_window(icon, item):
    icon.stop()
    root.destroy()

def show_window(icon, item):
    icon.stop()
    root.after(0, root.deiconify())

def hide_window():
    if bool1.get():
        root.withdraw()
        image = Image.open("icon.ico")
        menu=pystray.Menu(pystray.MenuItem('Exit', exit_window), pystray.MenuItem('Show', show_window, default=True))
        icon = pystray.Icon("name", image, "title", menu)
        icon.run()
    else:
        root.destroy()


def add_task(text='', event=None):
    text = txt_input.get()
    if text:
        checkbox(text)
    txt_input.delete(0, 'end')

def reset_all():
    for i in array:
        i.pack_forget()
    array.clear()
    txt_input.delete(0, 'end')

def forget(self):
    self.pack_forget()
    array.remove(self)
frame1 = tkinter.Frame(root)
frame2 = tkinter.Frame(root)

def checking():
    if bool.get():
        root.attributes('-topmost', True)
    else:
        root.attributes('-topmost', False)


menubar = tkinter.Menu(root)
settings = tkinter.Menu(menubar, tearoff=0)

checker = settings.add_checkbutton(label="Always Shown", onvalue=1, offvalue=0, variable=bool, command=checking)
tray = settings.add_checkbutton(label="Minimize to Tray", onvalue=1, offvalue=0, variable=bool1)
menubar.add_cascade(label="Settings", menu=settings)
menubar.add_command(label="Exit", command=root.quit)

txt_input = tkinter.Entry(frame1,width=44)
txt_input.grid(row=0, column=0)

btn_add_task = tkinter.Button(frame1, text="Add", justify="left", command=add_task, width=37)
btn_add_task.grid(row=1, column=0)

btn_reset_task = tkinter.Button(frame1, justify="left", text="Reset", command=reset_all, width=37)
btn_reset_task.grid(row=2, column=0)

frame1.pack(side=tkinter.TOP, anchor=tkinter.NW)

root.bind('<Return>', add_task)

root.protocol("WM_DELETE_WINDOW", hide_window)

root.config(menu=menubar)
root.mainloop()
