import tkinter as tk
import os
from pygame import mixer
import mysql.connector
import UploadSong

mydb=mysql.connector.connect(
    host='remotemysql.com',
    username = 'HtuP1mmwZ4',
    password = 'QbvpkZsOwM',
    database = 'HtuP1mmwZ4'
)

def initialise():
    global songs,loadimagePlay,loadimagePause,playing
    playing = False

def mainscreen():
    global songbefore,playedonce
    a,songbefore=0,""
    playedonce = False
    page_1 = tk.Tk()
    page_1.geometry('1920x1080')
    sb = tk.Scrollbar(page_1)
    sb.pack(side='right', fill='y')
    lb = tk.Listbox(page_1,width=280,relief='flat',height=55)
    lb.place(x=0,y=100)
    lb.config(yscrollcommand = sb.set)
    songs=UploadSong.getsongs()
    for x in songs:
        lb.insert(a,x[0])
        a+=1
    loadimagePlay = tk.PhotoImage(file=r"D:\Users\Vivaan\Documents\GitHub\CS-Project\play.png")
    loadimagePause = tk.PhotoImage(file=r"D:\Users\Vivaan\Documents\GitHub\CS-Project\pause.png")
    loadimagequeue = tk.PhotoImage(file=r"D:\Users\Vivaan\Documents\GitHub\CS-Project\queue.png")
    def clicked_play():
        song = lb.get(lb.curselection())
        global playing,playedonce,songbefore
        if song != songbefore:
            playing = False
            playedonce = False
        else:
            # pass
            UploadSong.unload()
        songbefore=song
        if playing == False:
            if playedonce == False:
                UploadSong.read(song)
                playB.config(image = loadimagePause)
                playedonce = True
                playing = True
            else:
                UploadSong.unpause()
                playing = True
                playB.config(image = loadimagePause)
        else:
            UploadSong.pause()
            playB.config(image = loadimagePlay)
            playing = False
    playB = tk.Button(
                page_1,
                background = 'white',
                command = clicked_play,
                image = loadimagePlay
                )
    def clicked_queue():
        lb.get(lb.curselection())
        while mixer.music.get_busy() == False:
            pass
        else:
            clicked_play()
    queueB = tk.Button(
        background = 'white',
        command = clicked_queue,
        image = loadimagequeue
    )
    playB.place(x=1920/2-80,y=995)
    queueB.place(x=1920/2-10,y=995)
    page_1.mainloop()

initialise()
mainscreen()



