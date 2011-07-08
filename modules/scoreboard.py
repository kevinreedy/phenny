"""
scoreboard.py - Phenny Scoreboard Module
Author: Kevin Reedy, kevinreedy.net
About: https://github.com/kevinreedy/phenny
"""

import simplejson as json
import os
import re


# initialize points dictionary
points = {}


# load points[] from file
# TODO error checking
# TODO define file location in config file
def load_json():
	global points
	with open(os.getenv("HOME") + '/.phenny/points.json', mode='r') as f:
		points = json.load(f)	


# save points[] to file
# TODO error checking
# TODO define file location in config file
def save_json():
	with open(os.getenv("HOME") + '/.phenny/points.json', mode='w') as f:
		# TODO figure out this sort fail
		#points.sort(key=lambda x: x.lower())
		json.dump(points, f, indent=4)

# add/subtract points from a nick
def add_points(nick, new_points):
	load_json()

	if nick not in points:
		points[nick] = 0

	points[nick] += new_points
	
	save_json()

	return points[nick]

def scoreboard(phenny, input):
	p = re.compile('(\S+)\s*([\+-][\+-=])\s*((\d+)|())')
	m = p.match(input.group(0))
	if m:
		who = m.groups()[0]
		symbol = m.groups()[1]
		ammount_s = m.groups()[2]
		if ammount_s:
			ammount = int(ammount_s)
		else:
			ammount = 0
		
		#TODO OVER 9000?!?!?

		if(symbol == "++"):
			phenny.say(who + ' gets a point for a total of ' + str(add_points(who, 1)))
		elif(symbol == "--"):
			phenny.say(who + ' loses a point for a total of '+ str(add_points(who, -1)))
		elif(symbol == "+="):
			phenny.say(who + ' gets ' + str(ammount) + ' poitns for a total of ' + str(add_points(who, ammount)))
		elif(symbol == "-="):
			phenny.say(who + ' loses ' + str(ammount) + ' points for a total of ' + str(add_points(who, (ammount * -1))))

# TODO move the whole regexp here
scoreboard.rule = r'.*\w+\s*[\+-][\+-=].*'
scoreboard.priority = 'medium'

