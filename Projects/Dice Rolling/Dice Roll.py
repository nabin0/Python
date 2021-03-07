import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()

# Root View Data Initialization
root.geometry("400x600")
root.title("Welcome To Nabin's Dice Game")

# images
photos = ["die1.png", "die2.png", "die3.png", "die4.png", "die5.png", "die6.png"]

image = ImageTk.PhotoImage(Image.open(random.choice(photos)))

label1 = tkinter.Label(root, image=image)
label1.pack(expand=True)


def roll_dice():
    image = ImageTk.PhotoImage(Image.open(random.choice(photos)))
    # Updating Image
    label1.configure(image=image)
    # This line Keeps reference to the image
    label1.image = image


# Button For Roll_dice()

btn1 = tkinter.Button(root, text="Click Me", command=roll_dice)
btn1.pack(expand=True)

root.mainloop()
