import tkinter as tk
import random 

#  +++++ FUNCTION BODY +++++

def PhraseGenerator():
    phraseList= ["Hello ","What's up ","Aloha ","Marhaba ","Salam ","halo "]
    # Getting the content/text inside the entryField1
    userName=str(entryFiled1.get())
    # returning a random phrase with the userName
    return phraseList[random.randint(0,len(phraseList)-1)] + userName 
    


def PhraseDisplay():
    displayContent=PhraseGenerator()
    
    #Creating the Text field
    # Storing the text into the master , which is assigned to our tk window
    displayField = tk.Text(master=window, height=10,width=30)
    displayField.grid(column=2,row=4)
    
    # Storing the contentValue INSIDE the contentToDisplay because it's contains the Text field (tk.Text)
    displayField.insert(tk.END,displayContent)
    



# +++++++ Window Settings ++++++

window = tk.Tk()  #creating the window
window.title("User Prompt APP")
window.geometry("600x600")



#Creaitng Title
title=tk.Label(text="Welcome to my User Prompt APP!",font=("Arial",20),fg="blue")
title.grid(column=2,row=0)

# Creating the prompt section
promptText=tk.Label(text="Enter your name: ")
promptText.grid(column=2,row=1)

# Creating the Entry Fields
entryFiled1= tk.Entry(window,fg="Red")
entryFiled1.grid(column=2,row=2)

# Creating the Submit Btn
sumbitBtn=tk.Button(text="Submit",bg="red",command=PhraseDisplay)
sumbitBtn.grid(column=2,row=3)


# Creating the mainloop
window.mainloop()
