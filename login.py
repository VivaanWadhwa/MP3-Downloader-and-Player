from tkinter import *
import os
import time
from tkinter.ttk import Progressbar
import sqlite3
import mysql.connector
username_verify = ""
mydb=mysql.connector.connect(
    host='remotemysql.com',
    username = 'HtuP1mmwZ4',
    password = 'QbvpkZsOwM',
    database = 'HtuP1mmwZ4'
)
def register():
    global register_screen

    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username,password,username_entry,password_entry

    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = signup_database).pack()

def login():
    global login_screen,progress_bar
    global password_verify
    global variable

    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_login_entry,password_login_entry
    # conn = mydb.cursor()
    # conn=sqlite3.connect(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\try.db")
    # cur=conn.cursor()
    conn = mydb.cursor()
    conn.execute("SELECT username FROM trial;")

    options =[]
    for username in conn.fetchall():
        options.append(username)
    print (options)

    variable = StringVar()
    variable.set("Username")

    drop=OptionMenu(login_screen,variable,options[0],*options)
    drop.pack()

    # button = Button(login_screen, text="OK", command=ok)
    # button.pack()

    username_login_entry = Label(login_screen, text="")
    username_login_entry.pack()

    Label(login_screen,).pack()

    password_verify = StringVar()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable = password_verify, show= '*')
    password_login_entry.pack()

    Label(login_screen, text="").pack()

    progress_bar=Progressbar(login_screen, orient = HORIZONTAL,length = 100, mode = 'determinate')
    progress_bar.pack()

    Button(login_screen, text="Login", width=10, height=1, command =lambda:[run_ProgressBar(),checklogin()]).pack()   

# def ok():
#     global username_verify
#     username_tup = variable.get()
#     username_verify = ""
#     for letter in username_tup:
#         if ord(letter) >= 65 and ord(letter) <= 91:
#             username_verify += letter
#         elif ord(letter) >= 97 and ord(letter) <= 122:
#             username_verify += letter


def signup_database():

    # conn=sqlite3.connect(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\try.db")
    # cur=conn.cursor()
    conn=mydb.cursor()
    conn.execute("create table if not exists trial(username text , password text)")
    # conn.execute("insert into trial VALUES (?,?)",(username_entry.get(),password_entry.get()))
    conn.execute("insert into trial VALUES (%s,%s)",(username_entry.get(),password_entry.get()))
    mydb.commit()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def checklogin():
    global username_verify
    username_tup = variable.get()
    username_verify = ""
    for letter in username_tup:
        if ord(letter) >= 65 and ord(letter) <= 91:
            username_verify += letter
        elif ord(letter) >= 97 and ord(letter) <= 122:
            username_verify += letter
    password_login_entry.config(textvariable = password_verify)
    # conn = sqlite3.connect(r"D:\Users\Vivaan\Documents\GitHub\CS-Project\try.db")
    # cur = conn.curso(r)
    # conn.execute("select * from trial where username=? and password=?",(username_verify,password_verify.get()))
    conn = mydb.cursor()
    conn.execute("select * from trial where username=%s and password=%s",(username_verify,password_verify.get()))
    row = conn.fetchmany(size=2)
    if len(row) != 0:
        username = row[0][0]
        Label(login_screen,text="welcome "+username).pack()
    else:
        user_not_found()

def run_ProgressBar():

    progress_bar['maximum']=100
    for i in range(0,80):
        progress_bar['value']=i
        time.sleep(0.005)  
        progress_bar.update()
    time.sleep(1)
    for i in range(80,100):
        progress_bar['value']=i
        time.sleep(0.005)
        progress_bar.update()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1000x800")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="green", width="300", height="3", font=("ariel", 17)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    main_screen.mainloop()

main_account_screen()