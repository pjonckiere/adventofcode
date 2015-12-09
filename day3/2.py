#!/usr/bin/env python

f = open('input.txt')

grid = {0:{0:1}}

total = 1

arrows = {
	"^": [0, 1],
	">": [1, 0],
	"<": [-1, 0],
	"v": [0, -1]
}

def updateGrid(x, y) :
	global grid, total
	if x not in grid:
		grid[x] = {}

	if y not in grid[x]:
		grid[x][y] = 1
		total += 1

for directions in f:
	xsanta = 0
	ysanta = 0
	xrobo = 0
	yrobo = 0

	for index, dir in enumerate(directions): 
		coords = arrows.get(dir)
		if coords is None:
			continue

		if (index % 2 == 1) :
			# print "santa"
			xsanta += coords[0]
			ysanta += coords[1]
			updateGrid(xsanta, ysanta)
		else :
			# print "robo"
			xrobo += coords[0]
			yrobo += coords[1]
			updateGrid(xrobo, yrobo)

print total
