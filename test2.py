import misc_fn
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path + "/music"
music_list_name = "music_list.json"
data = misc_fn.load(music_list_name)
for filename in os.listdir(dir_path):
    print(filename)
    if filename.endswith(".json") and os.path.splitext(filename)[0] not in data:
        data[os.path.splitext(filename)[0]] = "music/" + filename

misc_fn.dump(data, music_list_name)

