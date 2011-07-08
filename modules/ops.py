def ops_join(phenny, input):
	phenny.write(['MODE', input, "+o",  input.nick])

ops_join.event = 'JOIN'
ops_join.rule = '.*'
