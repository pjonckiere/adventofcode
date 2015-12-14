#!/usr/bin/env python

import itertools
import re

f = open('input.txt')
regex = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')

time = 2503
farthest = 0
for l in f:
	m = re.findall(regex, l)	
	c = m[0]	
	dist = int(c[1]) * int(c[2]) 
	cycles = int(time) / (int(c[2]) + int(c[3]))
	left = int(time) % (int(c[2]) + int(c[3]))
	if int(left) > int(c[2]):
		left = c[2]
	dist = cycles * dist + int(left) * int(c[1])
	if dist > farthest :
		farthest = dist

print farthest
