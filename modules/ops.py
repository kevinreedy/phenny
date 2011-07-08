ops=['kreedy', 'codexile', 'jlapenna', 'nukes', 'passi', 'clambert']

def ops_join(phenny, input):
	if input.nick in ops:
		phenny.write(['MODE', input, "+o",  input.nick])

ops_join.event = 'JOIN'
ops_join.rule = '.*'
