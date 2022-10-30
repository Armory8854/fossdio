# Import libraries
import ffmpeg
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
import os

# Set directories here
music_dir = "/home/celer/Continents/"

# Create variable functions here, or whatever you call them. Objects?
dir_list = os.listdir(music_dir)

print(dir_list[0])

# get info with mutagen
## Define the MP3 File
mp3_file = MP3(music_dir + dir_list[0])

## Define the proper title of the file to fix weird file names
mp3_id3 = ID3(music_dir + dir_list[0])
print(mp3_id3['TIT2'].text[0])
print(mp3_id3['TRCK'].text[0])

## Get the bitrate
mp3_bitrate=int((mp3_file.info.bitrate)/1000)
print(mp3_bitrate)

