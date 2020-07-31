import sys
import os
from tkinter import*
root = Tk()

def handsfree():
    os.system('py handsfree.py')

def textonly():
    os.system('py textonly.py')

def info():
    os.system('python -m webbrowser -t "https://www.google.com"')

root.geometry('500x500')
root.title("TEXTAPHONE")
label_0 = Label(root, text="Select Mode",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
Button(root, text='HANDSFREE',height=10,width=20,bg='brown',fg='white',command= handsfree).place(x=180,y=150)
Button(root, text='TEXT ONLY',height=10,width=20,bg='brown',fg='white',command= textonly).place(x=180,y=320)
Button(root, text='Info',bg='brown',fg='white',command= info).place(x=450,y=450)
root.mainloop()
