from tkinter import *

window = Tk()
window.geometry("300x300")

# Changing the background color of the window
window.config(background="black")

# Creating the methods that does something when a button calls it


def btn1_Action():
    print("Greeting young one!")


def btn2_Action():
    print("Have a safe journey")


# Creating Label

title=Label(window,text="Welcome young one!",font="Arial",padx=10,pady=20)
title.pack()
# Creating 2 buttons
btn1 = Button(window, text="Enter", command=btn1_Action)
btn2 = Button(window, text="Exit", command=btn2_Action)

# img Btn
# imgBtn = PhotoImage(file="1.jpg")
# Placing the buttons on the tkinter window
# btn1.pack()
btn1.place(bordermode=OUTSIDE, height=50,
           width=100, x=100, y=80)
btn2.place(bordermode=INSIDE, height=50, width=100, x=100, y=150)

# imgBtn.Place()

mainloop()
