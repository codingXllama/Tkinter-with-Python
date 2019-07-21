from random import *
from tkinter import *

canvasSize=500
window =Tk()
canvas= Canvas(window,width=canvasSize,height=canvasSize)
canvas.pack()
counter=5
while True:
    # the choices functions picks a random color from the list we passed it
    colors = choice(['red','pink','green','blue','yellow'])
    # creating a random x point
    x0=randint(0,canvasSize)
    # creating a random y point
    y0=randint(0,canvasSize)
    d=randint(0,canvasSize/5)
    # Drawingg the oval and filling it with the random colors
    canvas.create_oval(x0,y0,x0+d,y0+d,fill=colors)
    window.update()
    # counter=counter-1
    
    
    
    




mainloop()