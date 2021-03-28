from tkinter import *
import tkinter.messagebox as tkmsg
import os
from tkinter.filedialog import asksaveasfilename, askopenfilename


def new_file():
    global file
    root.title("Untitled -Notepad")
    file = None
    textarea.delete(1.0, END)


def open_file():
    global file
    # file = askopenfilename(title="Open File", filetypes=[("Text Files", ".txt"), ("All files", "*.*")])
    file = askopenfilename(initialdir="/Documents", title="Select File", defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All files", "*.*")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " -Notepad")
        textarea.delete(1.0, END)
        with open(file) as f:
            textarea.insert(1.0, f.read())


def save_file():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="untitled.txt", title="Save File", filetypes=[("Text Files", ".txt"), ("All files", "*.*")])

        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(textarea.get(1.0, END))
            root.title(os.path.basename(file + " -Notepad"))
    else:
        with open(file, "w") as f:
            f.write(textarea.get(1.0, END))
        root.title(os.path.basename(file + " -Notepad"))


def close():
    root.destroy()


def cut():
    textarea.event_generate("<<Cut>>")


def copy():
    textarea.event_generate("<<Copy>>")


def paste():
    textarea.event_generate("<<Paste>>")


def about():
    tkmsg.showinfo("Notepad", "Notepad Created By Nabin😀️")


if __name__ == '__main__':
    # Initializing Gui Window
    root = Tk()
    root.title("Untitled -Notepad")
    # change default tkinter icon it might not work in linux
    # root.wm_iconbitmap("notepad.ico")
    root.geometry("500x450")

    # Menu
    menuBar = Menu(root)

    # Menu Element FileMenu
    fileMenu = Menu(menuBar, tearoff=0)

    # Adding FileMenu Drop down options
    fileMenu.add_command(label="New", command=new_file)
    fileMenu.add_command(label="Open", command=open_file)
    fileMenu.add_command(label="Save", command=save_file)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=close)
    menuBar.add_cascade(label="Files", menu=fileMenu)

    # Adding EditMenu
    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu=editMenu)

    # HelpMenu
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About", command=about)
    menuBar.add_cascade(label="Help", menu=helpMenu)
    root.config(menu=menuBar)

    # Creating Textarea
    textarea = Text(root)
    textarea.pack(fill=BOTH, expand=True)

    file = None

    # Creating ScrollBar
    scrollBar = Scrollbar(textarea)
    scrollBar.pack(fill=Y, side=RIGHT)
    scrollBar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollBar.set)
    root.mainloop()
