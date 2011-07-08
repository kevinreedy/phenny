"""
mod.py - Phenny Moderators Module
Author: Kevin Reedy, kevinreedy.net
About: https://github.com/kevinreedy/phenny
"""

import simplejson as json
import os


# initialize ops list
ops = []


# load ops[] from file
# TODO error checking
# TODO define file location in config file
def load_json():
	global ops
	with open(os.getenv("HOME") + '/.phenny/ops.json', mode='r') as f:
		ops = json.load(f)	


# save ops[] to file
# TODO error checking
# TODO define file location in config file
def save_json():
	with open(os.getenv("HOME") + '/.phenny/ops.json', mode='w') as f:
		ops.sort(key=lambda x: x.lower())
		json.dump(ops, f, indent=4)


# when a user joins, see give them ops if they are in the list of operators
def ops_join(phenny, input):
	load_json()
	if input.nick in ops:
		phenny.write(['MODE', input, "+o",  input.nick])

ops_join.event = 'JOIN'
ops_join.rule = '.*'
ops_join.priority = 'medium'


# listen for .addops and add that operator to the list
# TODO basic checking on field data
def ops_add(phenny, input):
	load_json()
	# make sure a current op is doing this
	if input.nick in ops:
		newop = input.group(2).lower().split()[0]
		ops.append(newop)
		save_json()
		phenny.write(['MODE', input.sender, "+o",  newop])
		phenny.say('Added ' + newop + ' to the operators list')

ops_add.commands = ['addops']
ops_add.priority = 'medium'


# list for .delops and delete operators from the list
def ops_del(phenny, input):
	load_json()
	# make sure a current op is doing this
	if input.nick in ops:
		oldop = input.group(2).lower().split()[0]
		# make sure op is in list
		if oldop in ops:	
			ops.remove(oldop)
			save_json()
			phenny.write(['MODE', input.sender, "-o",  oldop])
			phenny.say('Deleted ' + oldop + ' from the operators list')
		else:
			phenny.say(oldop + ' was not on the operators list')

ops_del.commands=['delops']
ops_del.priority= 'medium'


# listen for .listops and list all of the operators
def ops_list(phenny, input):
	load_json()
	op_string = 'Your operators are'
	for o in ops:
		op_string += ', ' + o
	phenny.say(op_string)

ops_list.commands = ['listops']
ops_list.priority = 'medium'


