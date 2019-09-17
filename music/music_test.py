import misc_fn

# "game_play": { time in ms: [[position, colour/controller, direction]]
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
        [3000, 1, 1, 1],
        [5000, 2, 2, 2.5],
        [9500, 1, 1, 1],
        [9500, 2, 2, 2.5],
        [10000, 1, 1, 1],
        [10000, 2, 1, 1],
        [10000, 3, 1, 1],
    ]

}

print(new_divide)

misc_fn.dump(new_divide, 'new_divide.json')