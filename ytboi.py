from pytube import YouTube 
from sys import argv

#link = argv[1]
link = "https://www.youtube.com/watch?v=vEQ8CXFWLZU"
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
yd = yt.streams.get_highest_resolution()
yd.download(r"C:/Users/Black/Documents/GitHub/ytboi/")
#yd.download(r"C:/Users/Blac/Desktop/YTBOI_DL/")