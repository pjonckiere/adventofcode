#!/usr/bin/env python

filename = "input.txt"

with open(filename) as fn:
	content = fn.readlines()

floor = 0
for index, parantheses in enumerate(content[0]):
	if parantheses == "(":
		floor += 1
	elif parantheses == ")":
		floor -= 1

	if floor == -1:
		print "Going to basement on index %d" % index
