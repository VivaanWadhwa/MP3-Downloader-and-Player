import tkinter as tk
import os
from pygame import mixer
import mysql.connector
# mydb=mysql.connector.connect(
#     host='remotemysql.com',
#     username = 'HtuP1mmwZ4',
#     password = 'QbvpkZsOwM',
#     database = 'HtuP1mmwZ4'
# )

def initialise():
    mixer.init()
    global songs,loadimagePlay,loadimagePause,playing
    songs = os.listdir(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\Music")
    playing = False
    # conn=mydb.cursor()
    # conn.execute("insert into Blobtable (ImageName, varBinaryData) select 'image1', BulkColumn from openrowset (Bulk r'D:\Users\Vivaan\Documents\GitHub\CS-Project\play.png', SINGLE_BLOB) AS varBinaryData;")
    # mydb.commit()

def mainscreen():
    a=0
    playedonce = False
    page_1 = tk.Tk()
    page_1.geometry('1920x1080')
    sb = tk.Scrollbar(page_1)
    sb.pack(side='right', fill='y')
    lb = tk.Listbox(page_1,width=280,relief='flat',height=55)
    lb.place(x=0,y=100)
    lb.config(yscrollcommand = sb.set)
    for x in songs:
        lb.insert(a,x)
        a+=1
    loadimagePlay = tk.PhotoImage(file=r"D:\Users\Vivaan\Documents\GitHub\CS-Project\play.png")
    loadimagePause = tk.PhotoImage(file=r"D:\Users\Vivaan\Documents\GitHub\CS-Project\pause.png")
    def clicked():
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
                page_1,
                background = 'white',
                command = clicked,
                image = loadimagePlay
                )
    
    playB.place(x=1920/2-80,y=995)
    page_1.mainloop()

initialise()
mainscreen()

# a,song=0,""
# global playing
# playing = False
# songs = os.listdir(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\Music")
# for x in songs:
#     lb.insert(a,x)
#     a+=1
# loadimagePlay = tk.PhotoImage(file=r"D:\Users\Vivaan\Documents\GitHub\CS-Project\play.png")
# loadimagePause = tk.PhotoImage(file=r"D:\Users\Vivaan\Documents\GitHub\CS-Project\pause.png")

# def clicked_play():
#     global playing
#     song = lb.get(lb.curselection())
#     if playing == False:
#         mixer.music.load(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\Music\%s"%song)
#         mixer.music.play()
#         playB.config(image = loadimagePause)
#         playing = True
#     else:
#         mixer.music.pause()
#         playB.config(image = loadimagePlay)
#         playing = False
# 