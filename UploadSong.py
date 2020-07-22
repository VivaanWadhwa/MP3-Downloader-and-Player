from tkinter import *
import mysql.connector
import pymysql
from playsound import playsound

def convert(filename):
    with open (filename,'rb') as file:
        binarydata=file.read()
    print (binarydata)
    return(binarydata)

def upload(name,file):
    print ("inserting song into songs table")
    try:
        connection=mysql.connector.connect(host='remotemysql.com',
                                            username = 'HtuP1mmwZ4',
                                            password = 'QbvpkZsOwM',
                                            database = 'HtuP1mmwZ4')

        cursor=connection.cursor()

        insertion_query="""insert into songs (name,file_blob) values (%s,%s)"""

        upload_song=convert(file)

        insert_blob_tuple=(name,upload_song)

        result=cursor.execute(insertion_query,insert_blob_tuple)

        connection.commit()

        print ("uploaded!")
    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def write(data):
    with open('s.mp3', 'wb') as file:
        file.write(data)

def read(song_name):
    connection = pymysql.connect(host='remotemysql.com',
                                         user='HtuP1mmwZ4',
                                         password='QbvpkZsOwM',
                                         database='HtuP1mmwZ4')
    cursor=connection.cursor()

    query="""select * from songs where name=%s"""

    cursor.execute(query,(song_name,))
    record=cursor.fetchall()

    print (record)
    (name)=record
    x=name[0][1]
    write(x)

# #upload("happier","/Users/Vaibhav/Downloads/happier ft bastille - [BiggyMp3].mp3")
# read("happier")

# mp3=input("enter mp3 file:")
# playsound(mp3)

