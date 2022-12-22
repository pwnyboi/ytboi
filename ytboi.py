from pytube import YouTube
from sys import argv
from moviepy.editor import *
import moviepy.editor as mp
import time
import os

og_dir = os.getcwd()


def new_project():
    project_name = input('Project Name: ')
    while project_name == None or project_name == '':
        print("Error...Must Name Project!")
        project_name = input('Project Name: ')
        os.system('cls')
    os.chdir(og_dir)
    os.chdir(f'./Downloads')
    os.mkdir(project_name)
    os.chdir(f'./{project_name}')
    dir_path = print(f'Moving to: {os.getcwd()}')
    return dir_path

#dest = input("Please enter destination to download? Leave blank if no destination: ")
# os.chdir()


def downloader():
    link = input("Please enter YouTube link to download: ")
    if link == None or link == '':
        link = "https://www.youtube.com/watch?v=eBGIQ7ZuuiU"
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    print("Downloading... ", yt.title)
    print("This video has: {} views ".format(yt.views))
    print('Downloading to: {}'.format(dir_dest))
    yd.download(dir_dest)
    os.system('cls')
    print(f"You downloaded {yt.title}!")
    time.sleep(2)
    os.system('cls')
    return yt.title


def ask_continue():
    print("Please select a command: \n1. Continue (Y) \n2. Close (Exit) \n3. New Project (new) \n4. Last download name (last)")
    continue_downloading = input("Want to download another video? y/n: ")
    if continue_downloading == "Y":
        return
    if continue_downloading == "y":
        return
    if continue_downloading == 'new project':
        new_project()
        return
    if continue_downloading == 'last':
        os.system('cls')
        print(f'Your last download was: {vid_title}')
        time.sleep(3)
        ask_continue()
        return
    else:
        quit()


dir_dest = new_project()
while True:
    vid_title = downloader()
    time.sleep(.69)
    my_clip = mp.VideoFileClip(f"{vid_title}.mp4")
    print("converting audio tack...")
    time.sleep(.9)
    my_clip.audio.write_audiofile(f"{vid_title}.mp3")
    os.system('cls')
    ask_continue()
    time.sleep(.69)
    continue


# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
