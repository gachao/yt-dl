from yt_dlp import YoutubeDL
import glob
import os
file_list = glob.glob("*.mp4")
for file in file_list:
    print("remove:{0}".format(file))
    os.remove(file)

ydl_opts = {'format': 'best'}
url = input('Plese enter URL')
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url]);

from google.colab import files
file_list = glob.glob("*.mp4")
for file in file_list:
    print("download:{0}".format(file))
files.download(file)
