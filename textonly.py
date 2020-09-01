from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from PIL import ImageTk ,Image

import pickle
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

c=0

new_model = tf.keras.models.load_model('saved_model\my_model')
model=new_model


def nlp(msg1):
    sentiment=""
    predictions = model.predict(tf.expand_dims(msg1, 0))
    if(predictions>=0.5):
        sentiment='Positive'
    else:
        sentiment='Negative'
    return sentiment

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break

def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    global c
    if(c==0):
        client_socket.send(bytes(msg, "utf8"))
        my_msg.set("")  # Clears input field.
        c=c+1
    else:
        mood=nlp(msg)
        msg2=msg+"("+mood+")"
        my_msg.set("")  # Clears input field.
        client_socket.send(bytes(msg2, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()
top = tkinter.Tk()
top.title("TextaPhone")

sendphoto = ImageTk.PhotoImage(Image.open ("SEND.png") )

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=30, width=70, yscrollcommand=scrollbar.set, bd =3 )
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg,  bd =5, width=50)
entry_field.bind("<Return>", send)
entry_field.pack(side = tkinter.LEFT, padx=50)
send_button = tkinter.Button(top, text="Send", command=send, image = sendphoto, bd=0)
send_button.pack()
top.protocol("WM_DELETE_WINDOW", on_closing)


#----Now comes the sockets part----
HOST = '127.0.0.1'
PORT = '33000'
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

tkinter.mainloop()  # Starts GUI execution.