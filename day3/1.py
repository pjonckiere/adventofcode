#!/usr/bin/env python

f = open('input.txt')

grid = {0:{0: 1}}
x = 0
y = 0
amount = 1
total = 1

arrows = {
	"^": [0, 1],
	">": [1, 0],
	"<": [-1, 0],
	"v": [0, -1]
}

for directions in f:
	for dir in directions: 
		coords = arrows.get(dir)
		if coords is None:
			continue

		# print coords
		x += coords[0]
		y += coords[1]
		# print x
		if x not in grid:
			grid[x] = {}

		if y not in grid[x]:
			grid[x][y] = 1
			total += 1
		#	print grid

print total
