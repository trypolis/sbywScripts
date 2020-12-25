# map_counter.py
# Map Counter script - tells you the number of objects in your map.
# Copyright (C) 2020, Ty Gillespie. All rights reserved.
# This file is covered by the GNU General Public License Version 3.
# See the file LICENSE for more details.

import os
import sys


def string_left(s, amount):
	""" "Removes the given number of characters from the string (s).
	Emulates a BGT function to do this."""
	return s[:amount]


map_file = input("Enter a map file to search.")
if map_file == "":
	print("Nothing was typed.")
	sys.exit()
if not os.path.isfile(map_file):
	print("No file with that name was found. Remember to include the extention.")
	sys.exit()

f = open(map_file, "r")
text = f.read()
f.close()

platforms = (
	walls
) = (
	staircases
) = (
	signs
) = (
	doors
) = travelpoints = zones = sources = belts = vanishes = checkpoints = hazards = 0
final_text = text.split("\n")

for i in final_text:
	if string_left(i, 8) == "platform" and len(i) >= 16:
		platforms += 1
	if string_left(i, 4) == "sign" and len(i) >= 10:
		signs += 1
	if string_left(i, 4) == "door" and len(i) >= 12:
		doors += 1
	if string_left(i, 11) == "travelpoint" and len(i) >= 18:
		travelpoints += 1
	if string_left(i, 12) == "sound_source" and len(i) >= 18:
		sources += 1
	if string_left(i, 4) == "belt" and len(i) >= 12:
		belts += 1
	if string_left(i, 4) == "zone" and len(i) >= 12:
		zones += 1
	if string_left(i, 9) == "staircase" and len(i) >= 16:
		staircases += 1
	if string_left(i, 4) == "wall" and len(i) >= 8:
		walls += 1
	if string_left(i, 6) == "hazard" and len(i) >= 12:
		hazards += 1
	if string_left(i, 10) == "checkpoint" and len(i) >= 14:
		checkpoints += 1
	if string_left(i, 9) == "vanishing" and len(i) >= 16:
		vanishes += 1

print(
	"You have "
	+ str(platforms)
	+ " platforms, "
	+ str(walls)
	+ " walls, "
	+ str(staircases)
	+ " staircases, "
	+ str(doors)
	+ " doors, "
	+ str(signs)
	+ " signs, "
	+ str(zones)
	+ " zones, "
	+ str(sources)
	+ " sound sources, "
	+ str(travelpoints)
	+ " travelpoints, "
	+ str(belts)
	+ " conveyer belts, "
	+ str(hazards)
	+ " hazards, and "
	+ str(vanishes)
	+ " vanishing platforms in your map."
)
sys.exit()
