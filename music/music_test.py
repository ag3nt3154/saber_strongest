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
        [3000, 1, 1, 1],
        [3000, 2, 2, 1],
        [4000, 3, 1, 1],
        [5000, 4, 2, 1],
        [6000, 5, 1, 1],
        [7000, 6, 2, 1],
        [8000, 7, 1, 1],
        [9000, 8, 2, 1],
        [10000, 9, 1, 1],
        [11000, 10, 2, 1],
        [12000, 11, 1, 1],
        [13000, 12, 2, 1],

        
    ]

}

print(new_divide)

misc_fn.dump(new_divide, 'new_divide.json')