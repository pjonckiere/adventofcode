#!/usr/bin/env python

import re

regex = re.compile(r'(\d)(\1*)')

input = '3113322113'

for i in range(0, 40):
	newinput = ''
	for matches in re.findall(regex, input):
		seq = "%s%s" % (matches[0], matches[1])
		newinput += "%s%s" % (len(seq), matches[0])
	input = newinput

print len(input)
