from pytube import YouTube 
from sys import argv

link = input("Please enter YouTube link to download: ")
dest = input("Please enter destination to download? Leave blank if no destination")
#link = argv[1]
#link = "https://www.youtube.com/watch?v=vEQ8CXFWLZU"
yt = YouTube(link)

#yd = yt.streams.get_highest_resolution()
#yd.download(r"C:/Users/Black/Documents/GitHub/ytboi/Downloads")
#print("Download Successful!")


def downloader():
    yd = yt.streams.get_highest_resolution()
    yd.download(dest)
    #yd.download(r"C:/Users/Black/Documents/GitHub/ytboi/Downloads")
    print("Downloading: ", yt.title)
    print("This video has: ", yt.views)
    print("Download Successful!")
    
def ask_continue():



downloader()
ask_continue()