from pytube import YouTube 
from sys import argv
import time
import os

dest = input("Please enter destination to download? Leave blank if no destination: ")

def downloader():
    link = input("Please enter YouTube link to download: ")
    if link == None or link == '':
    	link = "https://www.youtube.com/watch?v=eBGIQ7ZuuiU"
    
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()

    print("Downloading: ", yt.title)
    print("This video has: {} views ".format(yt.views))
    print('Downloading to: {}'.format(dest))
    yd.download(dest)
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
    time.sleep(.69)
    ask_continue()
    time.sleep(.69)

    continue