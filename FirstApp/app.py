import tkinter as tk

# Creating the window
window = tk.Tk()

# Creating a window title
window.title("First Application")

# Creating the window size
window.geometry("400x400")

# creating the LABEL
title = tk.Label(text="Welcome to my First Tkinter APP!",
                 font=("Times New Roman", 20))
# Placing the title on the window you can use pack,place, or grid
# title.place(x=10, y=20)
# title.pack()
title.grid(column=0, row=0)

# Creating buttons
btn1 = tk.Button(text="click here", bg="red")
# placing the btn1 under the title so we .grid() on the btn instead of .pack
btn1.grid(column=0, row=1)

# Creating the Entry field- a blank box where user can input content inside
entryField1 = tk.Entry()
entryField1.grid(column=0, row=2)

# running the window, mainloop runs everything inside the window
window.mainloop()
