from tkinter import *
import random



# ++ FUNCTIONS 

def generateRandom():
    # clearing the textField
    # print("fly")
    displayField.delete(0.0,END)
    # print("why")
    # Inserting a random Value into the textField
    # print("bye")
    displayField.insert(END,random.randint(0,6))
    # print("hi")
    



# ++++ WINDOW SETTINGS +++
window=Tk()
window.title("Dice Roller")
window.geometry("400x400")
window.config(bg="black")


# ++ TITLE
title=Label(window,text="Your Random Number is: ",bg="black",fg="white",font=("Arial",15))
title.place(x=90,y=50)


#Creating the Display Screen that shows the ranodm number
displayField=Text(window,width=4,height=2)
displayField.tag_configure("center",justify='center')
# displayField.insert('end','tag-center')
# displayField.tag_add("center",1.0,"end")
displayField.place(x=175,y=120)



#   ++++ Creating the buttons
btn1=Button(window,text="GET RANDOM NUMBER",foreground="blue",command=generateRandom)
btn1.place(x=100,y=200)


















#mainloop
mainloop()