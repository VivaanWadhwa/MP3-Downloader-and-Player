import tkinter as tk        # python 3
from tkinter import ttk
from tkinter import font as tkfont
import time
import time as tm
import mysql.connector
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pygame
import os
import urllib.request
import re
from youtube_dl import YoutubeDL
import ffmpeg

mydb=mysql.connector.connect(
    host='remotemysql.com',
    user = 'JZcXqDAwAA',
    password = 'UgmORq8ou5',
    database = 'JZcXqDAwAA'
)

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("1000x800")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="bottom", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=2)
        container.grid_columnconfigure(0, weight=2)

        self.frames = {}
        for F in (StartPage, Login, MAIN, Register, GRAPH):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        StartPage.configure(self,bg="LemonChiffon2")
        label = tk.Label(self, text="WELCOME TO OUR APP", bg="steel blue", width="300", height="3", font=("ariel", 17)).pack()

        button1 = tk.Button(self, text="Login", height="4", width="30",bg="slate grey",
                            command=lambda: controller.show_frame("Login"))
        button2 = tk.Button(self, text="Register", height="4", width="30",bg="dark orchid",
                            command=lambda: controller.show_frame("Register"))
        button1.place(relx=0.35, rely=0.45, anchor="center")
        button2.place(relx=0.65, rely=0.45, anchor="center")

        # def main_account_screen():
        #     global main_screen
        #     main_screen = Tk()
        #     main_screen.geometry("1000x800")
        #     main_screen.title("Account Login")
        #     Label(text="Select Your Choice", bg="green", width="300", height="3", font=("ariel", 17)).pack()
        #     Label(text="").pack()
        #     Button1=tk.Button(self, text="Login", height="2", width="30", command=login).pack()
        #     Label(text="").pack()
        #     Button2=tk.Button(self, text="Register", height="2", width="30", command=register).pack()
        #
        #     button1.pack()
        #     button2.pack()

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="ENTER YOUR DETAILS BELOW", bg="lightblue", width="300", height="3", font=("ariel", 17)).pack()
        button2 = tk.Button(self, text="GO TO THIRD PAGE").pack()

        global progress_bar
        global password_verify
        global variable
        global username_login_entry, password_login_entry, timer
        # conn = mydb.cursor()
        # conn=sqlite3.connect(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\try.db")
        # cur=conn.cursor()
        variable="xxx"
        conn = mydb.cursor()
        conn.execute("SELECT username FROM trial;")
        usernames = conn.fetchall()
        options = []
        for username in usernames:
            options.append(username)
        print(options)

        variable = tk.StringVar()

        print (variable.get())

        drop = tk.OptionMenu(self, variable, *options)
        drop.place(relx=0.38, rely=0.4, anchor="center")

        # button = Button(login_screen, text="OK", command=ok)
        # button.pack()

        username_login_entry = tk.Label(self, text="Username:",font=("Helvetica",17))
        username_login_entry.place(relx=0.3, rely=0.4, anchor="center")


        password_verify = tk.StringVar()
        label=tk.Label(self, text="Password:",font=("Helvetica",17))
        label.place(relx=0.56, rely=0.4, anchor="center")

        password_login_entry = tk.Entry(self, textvariable=password_verify, show='*')
        password_login_entry.place(relx=0.7, rely=0.4, anchor="center")

        label=tk.Label(self, text="")
        label.place(relx=0.7, rely=0.4, anchor="center")

        # for i in range(16):
        #     label = tk.Label(self, bg="lightblue", width=1, height=1).place(x=(i + 22) * 22, y=350)
        #
        # self.update()
        #
        # self.playanimation()
        #
        # self.mainloop()

        progress_bar = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=400, mode='determinate')
        progress_bar.place(relx=0.5, rely=0.55, anchor="center")

        timer = tk.Label(self, text="")
        timer.pack()

        button= tk.Button(self, text="Login", height="2", width="30",
               command=lambda: [run_ProgressBar(), checklogin(), clock(), controller.show_frame("MAIN")])
        button.place(relx=0.5, rely=0.6, anchor="center")
        button = tk.Button(self, text="Go to the start page",height="2", width="30",
                           command=lambda: controller.show_frame("StartPage"))
        button.place(relx=0.5,rely=0.65,anchor="center")
        button1 = tk.Button(self, text="PROCEED TO THE GRAPH", height="2", width="30",
                            command=lambda: controller.show_frame("GRAPH"))
        button1.pack()

        def checklogin():
            global username_verify
            username_tup = variable.get()
            print (username_tup)
            username_verify = ""
            for letter in username_tup:
                if ord(letter) >= 65 and ord(letter) <= 91:
                    username_verify += letter
                elif ord(letter) >= 97 and ord(letter) <= 122:
                    username_verify += letter
                elif ord(letter) == 32:
                    username_verify += " "
            password_login_entry.config(textvariable=password_verify)
            # conn = sqlite3.connect(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\try.db")
            # cur = conn.curso(r)
            # conn.execute("select * from trial where username=? and password=?",(username_verify,password_verify.get()))
            conn = mydb.cursor()
            conn.execute("select * from trial where username=%s and password=%s",
                         (username_verify, password_verify.get()))
            row = conn.fetchmany(size=2)
            if len(row) != 0:
                username = row[0][0]
                label=tk.Label(self, text="welcome " + username).pack()
            else:
                user_not_found()

        global start_time
        global counter

        counter = 1
        start_time = int(tm.strftime("%M"))

        def clock():
            global counter
            current_time = int(tm.strftime("%M"))
            difference = current_time - start_time
            if difference<0:
                difference=current_time+(60-start_time)
            timer.config(text=difference)
            timer.after(60000, clock)
            conn = mydb.cursor()
            conn.execute(
                "create table if not exists GRAPH(S_no int(10) primary key auto_increment,user varchar(100),session int(10) not null,time_spent int(20))")

            while counter < 2:
                query = "select MAX(session) from GRAPH where user=%s"
                conn.execute(query, (username_verify,))
                f = conn.fetchone()
                if f[0]==None:
                    conn.execute("insert into GRAPH(user,session,time_spent) values(%s,%s,%s)", (username_verify, 1, 0))
                else:
                    conn.execute("insert into GRAPH(user,session,time_spent) values(%s,%s,%s)", (username_verify, int(f[0])+1, 0))
                counter += 1
            else:
                query = "select MAX(session) from GRAPH where user=%s"
                conn.execute(query, (username_verify,))
                f = conn.fetchone()
                print(difference)
                conn.execute("update GRAPH set time_spent=%s where user=%s and session=%s",
                             (difference, username_verify, f[0]))

            mydb.commit()
        #
        # def playanimation():
        #     for i in range(200):
        #         for j in range(16):
        #             tk.Label(self, bg="yellow", width=1,height=1).place(x=(j+22)*22,y=350)
        #             sleep(0.06)
        #             self.update_idletasks()
        #             tk.Label(self,bg="yellow",width=1,height=1).place(x=(j+22)*22,y=350)

        def run_ProgressBar():


            progress_bar['maximum'] = 100
            for i in range(0, 80):
                progress_bar['value'] = i
                time.sleep(0.005)
                progress_bar.update()
            time.sleep(1.5)
            for i in range(80, 100):
                progress_bar['value'] = i
                time.sleep(0.05)
                progress_bar.update()


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please enter details below").pack()
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage")).pack()
        def signup_database():

            global username1

            # conn=sqlite3.connect(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\try.db")
            # cur=conn.cursor()
            conn = mydb.cursor()
            conn.execute("create table if not exists trial(username text , password text)")
            # conn.execute("insert into trial VALUES (?,?)",(username_entry.get(),password_entry.get()))
            conn.execute("select username from trial")
            x = conn.fetchall()
            y = []
            for element_tuple in x:
                for element in element_tuple:
                    y.append(element)
            if username_entry.get() in y:
                label=tk.Label(self, text="Username already taken, try again.", fg="green",
                      font=("calibri", 11)).pack()
            else:
                conn.execute("insert into trial VALUES (%s,%s)", (username_entry.get(), password_entry.get()))
                label = tk.Label(self, text="Registration Success", fg="green", font=("calibri", 11)).pack()

            mydb.commit()

            username_entry.delete(0, END)
            password_entry.delete(0, END)

        global username, password, username_entry, password_entry

        username = tk.StringVar()
        password = tk.StringVar()

        username_lable = tk.Label(self, text="Username * ")
        username_lable.pack()
        username_entry = tk.Entry(self, textvariable=username)
        username_entry.pack()
        password_lable = tk.Label(self, text="Password * ")
        password_lable.pack()
        password_entry = tk.Entry(self, textvariable=password, show='*')
        password_entry.pack()

        button=tk.Button(self, text="Register", height="2", width="30", command= signup_database).pack()

class MAIN(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        global playingstatus, playingsong, playbtn, DownloadEntry, songtracks, queueflag, playlist
        queueflag = 0
        #self.root = parent
        #tk.Tk.wm_title("MusicPlayer")
        #self.winfo_geometry()
        pygame.init()
        pygame.mixer.init()
        track = tk.StringVar()
        status = tk.StringVar()
        button = tk.StringVar()
        downloadstatus = tk.StringVar()
        downloadedSong = tk.StringVar()
        downloadstatus.set("Download Songs")
        playingstatus = "stopped"
        playingsong = tk.StringVar()
        button.set("Play")

        # def skip(self):
        # Creating the Track Frames for Song label & status label
        trackframe = tk.LabelFrame(self,text="Song Track", font=("times new roman", 15, "bold"),
                                bg="Navyblue", fg="white", bd=5, relief=tk.GROOVE)
        trackframe.place(x=0, y=900, width=600, height=100)
        # Inserting Song Track Label
        songtrack = tk.Label(trackframe, textvariable=track, width=20,
                             font=("times new roman", 24, "bold")).grid(row=0, column=0, padx=10, pady=5)
        # Inserting Status Label
        trackstatus = tk.Label(trackframe, textvariable=status, font=("times new roman", 24, "bold")).grid(
            row=0, column=1, padx=10, pady=5)
        # Creating Button Frame
        buttonframe = tk.LabelFrame(self,font=("times new roman", 15, "bold"), bg="white", fg="white", bd=5)
        buttonframe.place(x=650 - 50, y=900, width=600, height=100)
        button = tk.Button(buttonframe, text="GO BACK", height="4", width="30", bg="dark orchid",
                           command=lambda: controller.show_frame("Login")).grid(row=10,column=9,padx=2,pady=10)
        # Inserting Play Button
        playbtn = tk.Button(buttonframe, textvariable=button, command=lambda:playsong(), width=10, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=10, column=5,
                                                                                              padx=2, pady=10)
        rewindbtn = tk.Button(buttonframe, text="Rewind", command=lambda:rewind(), width=10, height=1,
                           font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=10,
                                                                                                column=4,
                                                                                                padx=2, pady=10)
        # forwardbutton = Button(buttonframe,text = "Forward", command = self.skip, width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=10, column = 6, padx = 2, pady = 10)
        queuebutton = tk.Button(buttonframe, text="Queue", command=lambda:queue(), width=10, height=1,
                             font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=10,
                                                                                                  column=7,
                                                                                                  padx=2,
                                                                                                  pady=10)
        # Creating Playlist Frame
        songsframe = tk.LabelFrame(self,text="Song Playlist", font=("times new roman", 15, "bold"),
                                bg="grey", fg="white", bd=5, relief=tk.GROOVE)
        songsframe.place(x=0, y=0, width=850, height=900)
        # Inserting scrollbar
        scrol_y = tk.Scrollbar(songsframe, orient=tk.VERTICAL)
        # Inserting Playlist listbox

        playlist = tk.Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold",
                                selectmode=tk.SINGLE, font=("times new roman", 12, "bold"), bg="silver",
                                fg="navyblue", bd=5, relief=tk.GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrol_y.config(command=playlist.yview)
        playlist.pack(fill=tk.BOTH)
        # Changing Directory for fetching Songs
        # os.chdir(r"D:\Users\Vivaan Wadhwa\Documents\GitHub\CS-Project\Music")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            playlist.insert(tk.END, track)
        downloadframe = tk.LabelFrame(self,font=("times new roman", 15, "bold"), bg="silver", fg="grey",
                                   bd=5, relief=tk.GROOVE)
        downloadframe.place(x=850, y=0, height=900, width=350)
        DownloadLabel = tk.Label(downloadframe, textvariable=downloadstatus,
                              font=("times new roman", 24, "bold"), bg="silver").grid(row=0, column=0, padx=5,
                                                                                      pady=10)
        InstructionLabel = tk.Label(downloadframe,
                                 text="Enter Song name below and download. Add the name of the \nSinger/Band if there are multiple songs of the same name",
                                 bg="silver").grid(row=10, column=0, padx=0, pady=0)
        DownloadEntry = tk.Entry(downloadframe, textvariable=downloadedSong,
                              font=("times new roman", 12)).grid(row=13, column=0, padx=0, pady=10)
        DownloadBttn = tk.Button(downloadframe, text="Download!", command=lambda:downloadSong(),
                              font=("times new roman", 12))
        DownloadBttn.grid(row=16, column=0, padx=0, pady=10)

        def playsong():
            global playingsong
            global playingstatus
            print(playlist.get(playlist.curselection()))
            if playlist.get(playlist.curselection()) == playingsong:
                print(1)
                # unpause
                if playingstatus == "stopped":
                    print(2)
                    status.set("-Playing")
                    pygame.mixer.music.unpause()
                    playingstatus = "playing"
                    button.set("Pause")
                # pause
                else:
                    print(3)
                    status.set("-Paused")
                    pygame.mixer.music.pause()
                    playingstatus = "stopped"
                    button.set("Unpause")
            else:
                print(4)
                # play new song
                if playingstatus == "playing":
                    print(5)
                    track.set(self.playlist.get(playlist.curselection()))
                    status.set("-Playing")
                    pygame.mixer.music.load(self.playlist.get(playlist.curselection()))
                    pygame.mixer.music.play()
                    playingstatus = "playing"
                    button.set("Pause")
                    playingsong = self.playlist.get(playlist.curselection())
                # play first song
                else:
                    print(6)
                    #track.set(playlist.get(playlist.curselection()))
                    status.set("-Playing")
                    pygame.mixer.music.load(playlist.get(playlist.curselection()))
                    pygame.mixer.music.play()
                    playingsong = playlist.get(playlist.curselection())
                    playingstatus = "playing"
                    button.set("Pause")

        def queue():
            global queuedsongs
            queuedsongs = []
            queuedsongs.append(playlist.get(playlist.curselection()))
            print(queuedsongs)
            if queueflag == 0:
                pygame.mixer.music.queue(queuedsongs[0])
                queuedsongs.pop(0)
                print("Song queued")
                self.queueflag = 1
            else:
                pygame.mixer.music.set_endevent(queue())
                print("song will be queued")

        def shuffle():
            random.shuffle(queuedsongs)

        def rewind():
            pygame.mixer.music.rewind()

        def downloadSong():
            # Getting input from user and converting it to a format as "you+searched+this+"
            EntryText = downloadedSong.get()
            searchKeyword_temp = (EntryText).split()
            searchKeyword = ""
            for i in searchKeyword_temp:
                searchKeyword += i + "+"
            print (searchKeyword)
            # using urllib.request.open to get the html data of the youtube search page
            http = urllib.request.urlopen(("https://www.youtube.com/results?search_query=" + searchKeyword))
            # re.findall is used to find all the specific codes of the videos
            # http.read().decode() gives us a string with the raw html code of the site
            videoId = re.findall(r"watch\?v=(\S{11})", http.read().decode())
            videoURL = "https://www.youtube.com/watch?v=" + videoId[0]
            # YoutubeDl requires you to set a format code which is what file type you want to save it as
            audioDownloader = YoutubeDL({'format': 'bestaudio/best',
                                         'postprocessors': [{
                                             'key': 'FFmpegExtractAudio',
                                             'preferredcodec': 'mp3',
                                             'preferredquality': '192',
                                         }]})
            # Downloads the song in the folder containing the .py file. I have to change this will do
            audioDownloader.extract_info(videoURL)
            # os.chdir(r"D:\Users\Vivaan Wadhwa\Documents\GitHub\CS-Project\Music")
            # Fetching Songs
            songtracks = os.listdir()
            # Inserting Songs into Playlist
            for track in songtracks:
                self.playlist.insert(END, track)

class GRAPH(Login):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="YOUR SESSION VS TIME GRAPH:")
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("Login"))
        button3 = tk.Button(self, text="SHOW GRAPH",
                            command=lambda: graph())
        button1.pack()
        button2.pack()
        button3.pack()

        def graph():

            x=[]
            y=[]
            f=Figure(figsize=(5,5), dpi=100)
            a=f.add_subplot(111)

            conn = mydb.cursor()
            conn.execute("select session from GRAPH where user=%s", (username_verify,))

            for element in conn:
                x.append(element[0])

            conn.execute("select time_spent from GRAPH where user=%s", (username_verify,))
            for element in conn:
                y.append(element[0])

            print (x,y)
            a.plot(x,y)

            canvas= FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            print (username_verify)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
