import misc_fn

# "game_play": { time in ms, position, colour/controller, direction }
# position: from 1 to 12
# colour/controller: 0 -> mine, 1 -> controller1, 2 -> controller2
# direction:
#      -0.5     1     2.5
#          \    |    /
#           \   |   /
#            \  |  /
#      -1.5-----0-----1.5
#            /  |  \
#           /   |   \
#          /    |    \
#      -2.5    -1      0.5

new_divide = {

    "artist": "Linkin Park",
    "music_path": "music/new_divide.mp3",
    "game_play": [
        [4300, 2, 1, "N"],
        #[4300, 3, 2, "N"],
        [5080, 10, 1, "S"],
        #[5080, 11, 2, "S"],
        #[6450, 2, 1, "N"],
        [6450, 3, 2, "N"],
        #[7130, 10, 1, "S"],
        [7130, 11, 2, "S"],
        [8400, 2, 1, "N"],
        #[8400, 3, 2, "N"],
        [9100, 10, 1, "S"],
        #[9100, 11, 2, "S"],
        #[10550, 2, 1, "N"],
        [10550, 3, 2, "N"],
        #[11120, 10, 1, "S"],
        [11120, 11, 2, "S"],

        [12450, 2, 1, "N"],
        [12450, 3, 2, "N"],
        [13020, 10, 1, "S"],
        [13020, 11, 2, "S"],
        [14360, 2, 1, "N"],
        [14360, 3, 2, "N"],
        [15060, 10, 1, "S"],
        [15060, 11, 2, "S"],
        [16360, 2, 1, "N"],
        [16360, 3, 2, "N"],
        [17030, 10, 1, "S"],
        [17030, 11, 2, "S"],
        [18320, 2, 1, "N"],
        [18320, 3, 2, "N"],
        [19100, 10, 1, "S"],
        [19100, 11, 2, "S"],
    ]

}

for entry in new_divide["game_play"]:
    entry[0] -= 1100

#print(new_divide)

misc_fn.dump(new_divide, 'new_divide.json')