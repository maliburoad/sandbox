from pytubefix import YouTube
from sys import argv
from pathlib import Path


#link = argv[1]
link = ("https://www.youtube.com/watch?v=RhBl85uNigU&list=PLdV78aYad4w_mDimKJ9gJxpgetzAToNUH&index=3")
# link = input("Pass the link: ")
yt = YouTube(link)

print("Author: ", yt.author)
print("Title: ", yt.title)
print("Views: ", yt.views)


yd = yt.streams.get_highest_resolution()

yd.download('./YoutubeDownloads')
print('Download Done')