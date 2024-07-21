import os
import sys
from player import Player
from evaluater import Evaluater

_players = []

# if there are arguments
if len(sys.argv) > 1:
    _path = sys.argv[1]
else:
    _path = str(input("Enter path for stats files: "))
    print()

# listing through files and creating users
try:
    for file in os.listdir(_path):
        _players.append(Player(file.split(".")[0], _path))
except FileNotFoundError:
    print("Failed to find stats files. Make sure the path is correct and try again")
    exit(1)

evaluater = Evaluater(*_players)
evaluater.print_points()
