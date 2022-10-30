# Import libraries
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
import numpy as np
import os

# Set directories here
music_dir = "/home/celer/Continents/"

# Create variables here
## Get the base music dir list
dir_list = np.array(os.listdir(music_dir))

## Parse the list to only include mp3
### Create empty filter array first
filter_array = []

### Create the substring for the array - mp3 in this case
substring = str("mp3")

### Now, go through each array item to find only mp3's
for element in dir_list:
    if substring in element:
        filter_array.append(True)
    else:
        filter_array.append(False)

### Finally save this filtered array as a new one for later use
mp3_arr = dir_list[filter_array]
print(filter_array)
print(mp3_arr)
# Create the floor - start at 0 always
counter = 0

# Create ceiling for the loop
dir_ceiling = len(mp3_arr)

# get info with mutagen
## Define the MP3 File
for i in dir_list:
    if counter < dir_ceiling:
        dir_iterator = mp3_arr[counter]
        mp3_file_base = music_dir + dir_iterator
        mp3_file = MP3(mp3_file_base)

        ## Define the proper title of the file to fix weird file names
        mp3_id3 = ID3(mp3_file_base)
        mp3_title = mp3_id3['TIT2'].text[0]
        mp3_number = mp3_id3['TRCK'].text[0]

        ## Get the bitrate
        mp3_bitrate=str(int((mp3_file.info.bitrate)/1000))
        
        ## New Filename Fixing
        ### Replace forward slashes with a '-' to not break the file path
        mp3_title = mp3_title.replace("/","-")
        ### Add a 0 to the track number if there isn't one
        if int(mp3_number) < 10:
            mp3_number = str("0" + mp3_number)
        else:
            mp3_number = str(mp3_number)
    
        ### At the current moment this simply names it '# - Title'
        new_filename = str(mp3_number + " - " + mp3_title)

        # Pydub Section
        ## Save the song as a var
        song = AudioSegment.from_mp3(mp3_file_base)
        ## Save the file as an ogg
        song.export(music_dir + new_filename + ".ogg", bitrate=mp3_bitrate + "k")
        print(music_dir + new_filename + ".ogg Converted!")
        # add 1 to the counter
        counter = counter + 1
