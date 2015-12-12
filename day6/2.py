#!/usr/bin/env python

import re

f = open('input.txt')

grid = [[0]*1000 for i in range(1000)]
for line in f:
	# print line
	regex = re.compile(r'^((\w| )[^\d]+)((\d|,)+) through ((\d|,)+)$')
	matches = regex.match(line)
	action = matches.group(1).strip()
	coord1 =  matches.group(3)
	x1 = int(coord1[:coord1.find(',')])
	y1 = int(coord1[coord1.find(',') + 1:])
	coord2 =  matches.group(5)
	x2 = int(coord2[:coord2.find(',')])
	y2 = int(coord2[coord2.find(',') + 1:])

	for i in range(x1, x2 + 1):
		for j in range(y1, y2 + 1):
			if action == 'turn on':
				grid[i][j] += 1
			elif action == 'turn off':
				if grid[i][j] > 0:
					grid[i][j] -= 1
			else:
				grid[i][j] += 2

print sum(sum(x) for x in grid)
