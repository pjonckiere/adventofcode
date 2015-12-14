#!/usr/bin/env python

import itertools
import operator
import re

regex = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')

r = {}
time = 2503
distances = {}

for t in range(1, time + 1):
	f = open('input.txt')
	for index, l in enumerate(f):
		m = re.findall(regex, l)	
		c = m[0]	
		if c[0] not in r:
			r[c[0]] = 0
	
		dist = int(c[1]) * int(c[2]) 
		cycles = int(t) / (int(c[2]) + int(c[3]))
		left = int(t) % (int(c[2]) + int(c[3]))
		if int(left) > int(c[2]):
			left = c[2]
		d = int(left) * int(c[1])
		dist = cycles * dist + int(left) * int(c[1])
		distances[c[0]] = dist
	f.close()

	furthest = max(distances.iteritems(), key=operator.itemgetter(1))[0]
	furthest = distances[furthest]
	
	for res in distances:
		if distances[res] == furthest:
			r[res] += 1
print r
