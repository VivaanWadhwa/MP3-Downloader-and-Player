import tkinter as tk
import os
from pygame import mixer
import mysql.connector
a,song=0,""
mixer.init()
global playing
playing = False
window=tk.Tk()
window.geometry('1920x1080')
sb=tk.Scrollbar(window)
sb.pack(side='right', fill='y')
lb=tk.Listbox(window,width=280,relief='flat',height=55)
lb.place(x=0,y=100)
lb.config(yscrollcommand = sb.set)
songs = os.listdir(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\Music")
for x in songs:
    lb.insert(a,x)
    a+=1
loadimagePlay=tk.PhotoImage(file=r"D:\Users\Vivaan\Documents\GitHub\CS-Project\play.png")
loadimagePause=tk.PhotoImage(file=r"D:\Users\Vivaan\Documents\GitHub\CS-Project\pause.png")

def clicked_play():
    global playing
    song = lb.get(lb.curselection())
    if playing == False:
        mixer.music.load(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\Music\%s"%song)
        mixer.music.play()
        playB.config(image = loadimagePause)
        playing = True
    else:
        mixer.music.pause()
        playB.config(image = loadimagePlay)
        playing = False
playB = tk.Button(
    window,
    image = loadimagePlay,
    background = 'white',
    command = clicked_play)
playB.place(x=1920/2-80,y=995)
window.mainloop()