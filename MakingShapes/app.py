from tkinter import *

# creating window
window = Tk()

sizeOfCanvas = 500
# Creating canvas to draw on
myCanvas= Canvas(window,height=sizeOfCanvas,width=sizeOfCanvas)
# Adding the canvas onto the screen
myCanvas.pack()

# Drawing shapes onto myCanvas
rectangle1= myCanvas.create_rectangle(100,100,200,300,fill="blue",outline="brown")
square1=myCanvas.create_rectangle(30,30,40,40,fill="red",outline="green")
oval1=myCanvas.create_oval(100,100,300,200,fill="yellow",outline="black")
circle1=myCanvas.create_oval(30,30,80,80,fill="purple",outline="red")

mainloop()