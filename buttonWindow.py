from tkinter import *

window = Tk()
window.geometry("200x200")

# Creating the methods that does something when a button calls it


def btn1_Action():
    print("Greeting young one!")


def btn2_Action():
    print("Have a safe journey")


# Creating 2 buttons
btn1 = Button(window, text="Enter", command=btn1_Action)
btn2 = Button(window, text="Exit", command=btn2_Action)

# Placing the buttons on the tkinter window
btn1.pack()
btn2.pack()

mainloop()
