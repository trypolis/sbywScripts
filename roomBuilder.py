# room_builder.py
# Builds rooms (idea taken from EnvSuite).
# Copyright (C) 2020, Ty Gillespie. All rights reserved.
# This file is covered by the GNU General Public License Version 3.
# See the file LICENSE for more details.

import pyperclip
import sys

try:
	min_x = int(input("Enter the starting X of the room."))
	max_x = int(input("Enter the maximum X of the room."))
	min_Y = int(input("Enter the minimum Y of the room."))
	max_Y = int(input("Enter the maximum Y of the room."))
	# Todo: make the user able to select wall/floor type, as well as zone name.
	the_string = (
		"""
wall """
		+ str(min_x - 1)
		+ """ """
		+ str(max_x + 1)
		+ """ """
		+ str(min_Y - 1)
		+ """ """
		+ str(max_Y + 1)
		+ """ wallgeneric
platform """
		+ str(min_x)
		+ """ """
		+ str(max_x)
		+ """ """
		+ str(min_Y + 1)
		+ """ """
		+ str(max_Y - 1)
		+ """ 
platform """
		+ str(min_x)
		+ """ """
		+ str(max_x)
		+ """ """
		+ str(min_Y)
		+ """ """
		+ str(max_Y)
		+ """ tile
"""
	)
	print("Room generated. It's on your clipboard.")
	pyperclip.copy(the_string)
	sys.exit()
except ValueError:
	print("There was an error.")
	sys.exit()
