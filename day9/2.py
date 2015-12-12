#!/usr/bin/env python

import itertools

f = open('input.txt')

cities = set()
distances = {}
for line in f:
	parts = line.split(' to ')
	c1 = parts[0].strip()
	cities.add(c1)
	c2 = parts[1].split('=')
	c2 = c2[0].strip()
	cities.add(c2)

	if c1 not in distances:
		distances[c1] = {}
	if c2 not in distances:
		distances[c2] = {}
	distance = line[line.find('=') + 2:].rstrip()
	distances[c1][c2] = distance
	distances[c2][c1] = distance

print distances

routes = list(itertools.permutations(cities, len(cities)))
longest = 0
for route in routes:
	current = 0
	for city in range(0, len(route) - 1):
		tostring = "%s to %s" % (route[city], route[city+1])
		current += int(distances[route[city]][route[city+1]])
	if current > longest:
		longest = current

print longest
