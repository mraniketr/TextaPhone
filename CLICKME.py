import sys
import os
from tkinter import*
root = Tk()


def handsfree():
    os.system('py handsfree.py')

def textonly():
    os.system('py textonly.py')


root.geometry('500x500')
root.title("Registration Form")
label_0 = Label(root, text="Select Mode",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
Button(root, text='handsfree',width=20,bg='brown',fg='white',command= handsfree).place(x=180,y=280)
Button(root, text='Text Only',width=20,bg='brown',fg='white',command= textonly).place(x=180,y=320)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
