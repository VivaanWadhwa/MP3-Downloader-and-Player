from tkinter import *
import pygame
import os
import urllib.request
import re
from youtube_dl import YoutubeDL
import random
root = Tk()
class Musicplayer(Tk):
    def __init__(self,root):
        global playingstatus,playingsong,playbtn,DownloadEntry,songtracks,queueflag
        self.queueflag = 0
        self.root = root
        self.root.title("MusicPlayer")
        self.root.geometry("1200x1000")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()
        self.button = StringVar()
        self.downloadstatus = StringVar()
        self.downloadedSong = StringVar()
        self.downloadstatus.set("Download Songs")
        self.playingstatus = "stopped"
        self.playingsong = StringVar()
        self.button.set("Play")
        # Creating the Track Frames for Song label & status label
        trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="Navyblue",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=900,width=600,height=100)
        # Inserting Song Track Label
        songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold")).grid(row=0,column=0,padx=10,pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold")).grid(row=0,column=1,padx=10,pady=5)
        # Creating Button Frame
        buttonframe = LabelFrame(self.root,font=("times new roman",15,"bold"),bg="white",fg="white",bd=5)
        buttonframe.place(x=650-50,y=900,width=600,height=100)
        # Inserting Play Button
        playbtn = Button(buttonframe,textvariable=self.button,command=self.playsong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row = 10,column=5,padx=2,pady=10)
        rewindbtn = Button(buttonframe,text = "Rewind", command = self.rewind, width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row = 10, column=4, padx=2,pady=10)
        # forwardbutton = Button(buttonframe,text = "Forward", command = self.skip, width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=10, column = 6, padx = 2, pady = 10)
        queuebutton = Button(buttonframe, text = "Queue", command = self.queue,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row = 10, column=7, padx=2,pady=10)
        # Creating Playlist Frame
        songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=0,y=0,width=850,height=900)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir(r"D:\Users\Vivaan Wadhwa\Documents\GitHub\CS-Project\Music")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END,track)
        downloadframe = LabelFrame(self.root,font=("times new roman",15,"bold"),bg="silver",fg="grey",bd=5, relief = GROOVE)
        downloadframe.place(x = 850, y = 0,height = 900, width=350)
        DownloadLabel = Label(downloadframe, textvariable = self.downloadstatus, font=("times new roman",24,"bold"),bg = "silver").grid(row=0,column=0,padx=5,pady=10)
        InstructionLabel = Label(downloadframe, text = "Enter Song name below and download. Add the name of the \nSinger/Band if there are multiple songs of the same name",bg = "silver").grid(row=10,column=0,padx=0,pady=0)
        DownloadEntry = Entry(downloadframe,textvariable = self.downloadedSong, font = ("times new roman",12)).grid(row = 13, column = 0,padx=0,pady=10)
        DownloadBttn = Button(downloadframe, text = "Download!",command = self.downloadSong, font = ("times new roman",12))
        DownloadBttn.grid(row = 16, column = 0 , padx=0, pady=10)
        backbutton = Button(buttonframe, text="GO BACK", width=10, height=1,
                             font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=10,
                                                                                                  column=10,
                                                                                                  padx=2,
                                                                                                  pady=10)
    def playsong(self):
        if self.playlist.get(ACTIVE) == self.playingsong:
            print (1)
            # unpause
            if self.playingstatus == "stopped":
                print (2)
                self.status.set("-Playing")
                pygame.mixer.music.unpause()
                self.playingstatus = "playing"
                self.button.set("Pause")
            # pause
            else:
                print (3)
                self.status.set("-Paused")
                pygame.mixer.music.pause()
                self.playingstatus = "stopped"
                self.button.set("Unpause")
        else:
            print (4)
            # play new song
            if self.playingstatus == "playing":
                print (5)
                self.track.set(self.playlist.get(ACTIVE))
                self.status.set("-Playing")
                pygame.mixer.music.load(self.playlist.get(ACTIVE))
                pygame.mixer.music.play()
                self.playingstatus = "playing"
                self.button.set("Pause")
                self.playingsong = self.playlist.get(ACTIVE)
            # play first song
            else:
                print (6)
                self.track.set(self.playlist.get(ACTIVE))
                self.status.set("-Playing")
                pygame.mixer.music.load(self.playlist.get(ACTIVE))
                pygame.mixer.music.play()
                self.playingsong = self.playlist.get(ACTIVE)
                self.playingstatus="playing"
                self.button.set("Pause")
                
    def queue(self):
        global queuedsongs
        queuedsongs = []
        queuedsongs.append(self.playlist.get(ACTIVE))
        print (queuedsongs)
        if self.queueflag == 0:
            pygame.mixer.music.queue(queuedsongs[0])
            queuedsongs.pop(0)
            print ("Song queued")
            self.queueflag = 1
        else:
            pygame.mixer.music.set_endevent(self.queue())
            print ("song will be queued")

    def shuffle(self):
        random.shuffle(queuedsongs)
    def rewind(self):
        pygame.mixer.music.rewind()
    def downloadSong(self):
        # Getting input from user and converting it to a format as "you+searched+this+"
        EntryText = self.downloadedSong.get()
        searchKeyword_temp = (EntryText).split()
        searchKeyword = ""
        for i in searchKeyword_temp:
            searchKeyword += i+"+"
        # using urllib.request.open to get the html data of the youtube search page
        http = urllib.request.urlopen(("https://www.youtube.com/results?search_query=" + searchKeyword))
        # re.findall is used to find all the specific codes of the videos
        # http.read().decode() gives us a string with the raw html code of the site
        videoId = re.findall(r"watch\?v=(\S{11})", http.read().decode())
        videoURL = "https://www.youtube.com/watch?v=" + videoId[0]
        # YoutubeDl requires you to set a fromat code which is what file type you want to save it as
        audioDownloader = YoutubeDL({'format':'bestaudio/best',
                                    'postprocessors': [{
                                    'key': 'FFmpegExtractAudio',
                                    'preferredcodec': 'mp3',
                                    'preferredquality': '192',
                                     }]})
        # Downloads the song in the folder containing the .py file. I have to change this will do
        audioDownloader.extract_info(videoURL)
        os.chdir(r"D:\Users\Vivaan Wadhwa\Documents\GitHub\CS-Project\Music")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END,track)
Musicplayer(root)
root.mainloop()
