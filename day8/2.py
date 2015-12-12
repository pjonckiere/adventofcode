#!/usr/bin/env python

import re

f = open('input.txt')

count = 0
for line in f:
	line = line.strip()
	count -= len(line)
	line = line.replace('"', '##')
	line = line.replace('\\', '##')
	count += len(line)
	count += 2

print count
