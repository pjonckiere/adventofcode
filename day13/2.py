#!/usr/bin/env python

import itertools
import re

f = open('input.txt')

p = set()
h = {}
for line in f:
	regex = re.compile(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)')
	m = re.findall(regex, line)
	p.add(m[0][0])
	p.add(m[0][3])

	sign = '-' if m[0][1] == 'lose' else ''
	if m[0][0] not in h:
		h[m[0][0]] = {}
	h[m[0][0]][m[0][3]] = "%s%s" % (sign, m[0][2])

p.add('me')
h['me'] = {}
for person in p:
	h['me'][person] = 0
	h[person]['me'] = 0

arr = list(itertools.permutations(p, len(p)))
best = 0
current = 0
for a in arr:
	for person in range(0, len(a)):
		if person == len(a) - 1 :
			current += int(h[a[person]][a[0]])
			current += int(h[a[0]][a[person]])
		else:
			current += int(h[a[person]][a[person + 1]])
			current += int(h[a[person + 1]][a[person]])
		
		if person == len(a) - 1 and current > best:
			best = current

		if person == len(a) - 1:
			current = 0
print best
