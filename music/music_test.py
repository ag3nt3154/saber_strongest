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
        [1700, 1, 1, "NE"],
        [2100, 2, 2, "N"],
        [2500, 3, 1, "SE"],
        [4500, 4, 2, "SE"],
        [5000, 5, 1, "SE"],
        [5500, 6, 2, "SE"],
        [6000, 7, 1, "SE"],
        [6500, 8, 2, "NW"],
        [7000, 9, 1, "NW"],
        [7500, 10, 2, "NW"],
        [8000, 11, 1, "NW"],
        [8500, 12, 2, "NW"],
        [10000, 1, 1, "NW"],
        [10000, 2, 2, "NW"],
        [10000, 3, 1, "SW"],
        [10000, 4, 2, "SW"],
        [10000, 5, 1, "SW"],
        [10000, 6, 2, "SW"],
        [10000, 7, 1, "SW"],
        [10000, 8, 2, "SW"],
        [10000, 9, 1, "SW"],
        [10000, 10, 2, "SW"],
        [10000, 11, 1, "SW"],
        [10000, 12, 2, "SW"],

        
    ]

}

print(new_divide)

misc_fn.dump(new_divide, 'new_divide.json')