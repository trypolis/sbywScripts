#roomBuilder.py
#Builds rooms (idea taken from EnvSuite).
#Copyright (C) 2020, Ty Gillespie. All rights reserved.
#This file is covered by the GNU General Public License Version 3.
#See the file LICENSE for more details.

import pyperclip
import sys

try:
	minX=int(input("Enter the starting X of the room."))
	maxX=int(input("Enter the maximum X of the room."))
	minY=int(input("Enter the minimum Y of the room."))
	maxY=int(input("Enter the maximum Y of the room."))
	#Todo: make the user able to select wall/floor type, as well as zone name.
	theString="""
wall """+str(minX-1)+""" """+str(maxX+1)+""" """+str(minY-1)+""" """+str(maxY+1)+""" wallgeneric
platform """+str(minX)+""" """+str(maxX)+""" """+str(minY+1)+""" """+str(maxY-1)+""" 
platform """+str(minX)+""" """+str(maxX)+""" """+str(minY)+""" """+str(maxY)+""" tile
"""
	print("Room generated. It's on your clipboard.")
	pyperclip.copy(theString)
	sys.exit()
except ValueError:
	print("There was an error.")
	sys.exit()
