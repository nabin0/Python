from tkinter import *
from datetime import datetime

root = Tk()

# GUI Initialization
root.geometry("300x300")
root.title("MadLib By Nabin")
Label(root, text="Welcome!!", font="arial 20 bold").pack()
Label(root, text="Choose Any One OF Following", font="arial 15 bold").pack()


# MadLibs
def madlib_one():
    maleName = input("Enter The Name Of A Male: ")
    femaleName = input("Enter The Name Of A Female: ")
    thingName = input("Enter The Name Of A Thing: ")
    occuption = input("Enter The Occupation: ")
    resturant = input("Enter The Name Of An Resturant: ")
    shape = input("Enter Any shape Name: ")
    emotion = input("Enter A Emotion: ")
    verb = input("Enter A Verb: ")
    bodyPart = input("Enter A Name Of Body Part: ")
    adjective = input("Enter A Name Of Adjectives: ")

    print(f"{maleName} is a normal {occuption}. Then, one ay, a {thingName} explodes, causing a {thingName} to blow up, and nearby {thingName} erupts into a {shape} of flames."
          f" {maleName} realizes that he is being chased by the government, who is trying to {verb} him. While on the run, he teams up with an increadibly attractive woman named {femaleName}"
          f"who has an increadible {bodyPart}. She may be from the streets, but she can {verb} like nobody's business. The duo decide to turn the tables on their pursurs"
          f"by blowing up a {thingName}, which triggers a chain reaction, causing the local {thingName} , {resturant} to expolde. Then yhe bad guys helicopter gets {verb}"
          f"by piece of {thingName} from when the {thingName} exploded, and the helicopter explodes and falls onto a {thingName}, causing it to {verb}, which shoots"
          f"a fireball straight into heart of {thingName} and destroys the bad guy leader. Everything is {adjective} and the two decide that such a {adjective}"
          f"ordeal has caused them to fall in {emotion} with each other. They decide to celebrate by {verb}ing on the {thingName}, and they even managed to use"
          f"a {thingName} frm the beginning of the movie, to {verb} the whole story together.")


def madlib_two():
    name = input("Enter Your Name: ")
    idNo = input("Enter Your ID: ")
    grade = input("Enter Your Grade: ")
    favTeacher = input("Enter Name Of Favorite Teacher: ")

    name = input("Enter Your Name: ")
    idNo = input("Enter Your ID: ")
    grade = input("Enter Your Grade: ")
    favTeacher = input("Enter Name Of Favorite Teacher: ")
    college = input("Enter Your College Name: ")
    dateNow = datetime.now()

    print(f"\t\t Date: {dateNow} \n\n\n"
          f" Your Name: {name} \n"
          f" Your College Name: {college} \n"
          f" Your ID: {idNo} \n"
          f" Your Fav. Teacher: {favTeacher} \n"
          f" Your Grade is: {grade}")


def madlib_three():
    print("HAHAHA No Content Available Here...")

# Buttons

Button(root, text="Ganster Story", font="comicsansms 12 bold", command=madlib_one, padx=30, pady=20).pack()
Button(root, text="College Data View", font="comicsansms 12 bold",command=madlib_two, padx=30, pady=20).pack()
Button(root, text="Click Here", font="comicsansms 12 bold",command=madlib_three, padx=30, pady=20).pack()
root.mainloop()
