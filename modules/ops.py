def ops_join(phenny, input):
	phenny.say('Hello. Giving you ops')
	phenny.say(' /mode ' + str(input) + ' +o ' + str(input.nick))
	phenny.write(['MODE', input, "+o",  input.nick])

ops_join.event = 'JOIN'
ops_join.rule = '.*'
