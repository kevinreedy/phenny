"""
klout.py - Klout Module
Author: Kevin Reedy, kevinreedy.net
About: https://github.com/kevinreedy/phenny
"""

import simplejson as json
import urllib

# listen for .klout
def klout_check(phenny, input):
    if hasattr(phenny.config, 'klout_key'):
        klout_users = input.group(2).lower().split()[0]
        if(klout_users):
            klout_json = urllib.urlopen('http://api.klout.com/1/klout.json?key=' + phenny.config.klout_key + '&users=' + klout_users).read()
            if(klout_json):
                result = json.loads(klout_json)
                if(result['users']):
                    for user in result['users']:
                        phenny.say(user['twitter_screen_name'] + "'s Klout Score is " + str(int(round(user['kscore']))))
            else:
                # TODO: Need to actually error check for bad JSON
                phenny.say("Didn't find any user named " + klout_users)
    else:
        phenny.say("Klout API Key missing")

klout_check.commands = ['klout']
klout_check.priority = 'medium'

