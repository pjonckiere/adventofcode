#!/usr/bin/env python

import re

f = open('input.txt')

count = 0
for line in f:
	line = line.strip()
	count += len(line)
	count -= len(eval(line))

print count
