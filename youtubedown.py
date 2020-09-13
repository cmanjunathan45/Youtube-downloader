from pytube import *
link=input("Enter the YOUTUBE video link\n")
yt=YouTube(link)
y = yt.streams.get_highest_resolution()
y.download('videos')