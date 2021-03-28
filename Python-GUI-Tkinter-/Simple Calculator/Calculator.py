from tkinter import *


def calc(event):
    # global screen_value
    text = event.widget.cget("text")
    if text == "=":
        if screen_value.get().isdigit():
            value = int(screen_value.get())
        else:
            try:
                value = eval(screen_value.get())
            except Exception as e:
                print(e)
                value = "Error!!!"

        screen_value.set(value)
        screen.update()
    elif text == "C":
        screen_value.set("")
    else:
        # pass
        screen_value.set(screen_value.get() + text)
        screen.update()


# Window initializing

root = Tk()
root.title("Calculator By Nabin")
root.geometry("400x600")
root.resizable(0, 0)

# Show screen

screen_value = StringVar()
screen_value.set("")
screen = Entry(root, textvariable=screen_value, font="lucid 27 bold")
screen.pack(pady=10, padx=4)

# Frame To put buttons
frameOne = Frame(root, width=360, height=520, bg="gray").pack()

# Buttons
btn = Button(frameOne, text="9", font="lucid 26 bold")
btn.place(x=70, y=100)
btn.bind("<Button-1>", calc)
btn = Button(frameOne, text="8", font="lucid 26 bold")
btn.place(x=180, y=100)
btn.bind("<Button-1>", calc)
btn = Button(frameOne, text="7", font="lucid 26 bold")
btn.place(x=290, y=100)
btn.bind("<Button-1>", calc)

btn = Button(frameOne, text="6", font="lucid 26 bold")
btn.place(x=70, y=220)
btn.bind("<Button-1>", calc)
btn = Button(frameOne, text="5", font="lucid 26 bold")
btn.place(x=180, y=220)
btn.bind("<Button-1>", calc)
btn = Button(frameOne, text="4", font="lucid 26 bold")
btn.place(x=290, y=220)
btn.bind("<Button-1>", calc)

btn = Button(frameOne, text="3", font="lucid 26 bold")
btn.place(x=70, y=320)
btn.bind("<Button-1>", calc)
btn = Button(frameOne, text="2", font="lucid 26 bold")
btn.place(x=180, y=320)
btn.bind("<Button-1>", calc)
btn = Button(frameOne, text="1", font="lucid 26 bold")
btn.place(x=290, y=320)
btn.bind("<Button-1>", calc)

btn = Button(frameOne, text="-", padx=16, font="lucid 26 bold")
btn.place(x=70, y=420)
btn.bind("<Button-1>", calc)
btn = Button(frameOne, text="*", padx=16, font="lucid 26 bold")
btn.place(x=180, y=420)
btn.bind("<Button-1>", calc)
btn = Button(frameOne, text="/", padx=16, font="lucid 26 bold")
btn.place(x=290, y=420)
btn.bind("<Button-1>", calc)

btn = Button(frameOne, text="C", font="lucid 26 bold")
btn.place(x=70, y=510)
btn.bind("<Button-1>", calc)
btn = Button(frameOne, text="+", font="lucid 26 bold")
btn.place(x=180, y=510)
btn.bind("<Button-1>", calc)
btn = Button(frameOne, text="=", font="lucid 26 bold")
btn.place(x=290, y=510)
btn.bind("<Button-1>", calc)

# mainloop GUI
root.mainloop()
