import urllib.request
import re
from youtube_dl import YoutubeDL
import AudioConverter
# Getting input from user and converting it to a format as "you+searched+this+"
searchKeyword_temp = input().split()
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
audioDownloader = YoutubeDL({'format':'bestaudio',
                            'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                                }]})
# Downloads the song in the folder containing the .py file. I have to change this will do
audioDownloader.extract_info(videoURL)

