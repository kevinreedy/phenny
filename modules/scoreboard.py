"""
scoreboard.py - Phenny Scoreboard Module
Author: Kevin Reedy, kevinreedy.net
About: https://github.com/kevinreedy/phenny
"""

import simplejson as json
import os
import re


# initialize points list
points = []


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


def scoreboard(phenny, input):
	p = re.compile('(\S)+\s*([\+-][\+-=])\s*((\d+)|())')
	m = p.match(input.group(0))
	if m:
		print 'match found'

	
	phenny.say(input.nick + " gives somes points ftw")
	phenny.say(input.group(0))

# TODO move the whole regexp here
scoreboard.rule = r'.*\w+\s*[\+-][\+-=].*'
scoreboard.priority = 'medium'

