import socket
import sys
from _thread import *
import speech_recognition as sr

host = ''
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for a connection.')
def threaded_client(conn):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        conn.send(str.encode('Say Something\n'))
        audio = r.listen(source)
    text=""
    text+=r.recognize_google(audio) 
    conn.send(str.encode(text))    
    while True:
        data = conn.recv(2048)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            conn.send(str.encode('Say Something\n'))
            audio = r.listen(source)
        text=""
        text+=r.recognize_google(audio) 
        conn.send(str.encode(text))    
    conn.close()


while True:

    conn, addr = s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))

    start_new_thread(threaded_client,(conn,))