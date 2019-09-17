import misc_fn
import os

# Path of directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Update music list to include all available tracks
mus_path = dir_path + "/music/"
music_list_filename = "music_list.json"
music_list = misc_fn.load(music_list_filename)
print(music_list)

# Check for all available tracks
for filename in os.listdir(mus_path):
    print(filename)
    if filename.endswith(".json"):
        
        music_list[os.path.splitext(filename)[0]] = misc_fn.load(mus_path + filename)
        
        print(misc_fn.load(mus_path + filename))


# Save to music list
misc_fn.dump(music_list, music_list_filename)
