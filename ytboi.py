from pytube import YouTube 
from sys import argv
import time
import os

dest = input("Please enter destination to download? Leave blank if no destination")

def downloader():
    link = input("Please enter YouTube link to download: ")
    print("Downloading: ", yt.title)
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download(dest)

    print("This video has: ", yt.views)
    print("Download Successful!")
    time.sleep(.69)

def ask_continue():
    continue_downloading = input("Want to download another video? y/n: ")
    if continue_downloading == "Y":
        return
    if continue_downloading == "y":
        return
    else:
        quit()
        


while True:
    downloader()
    ask_continue()
    continue