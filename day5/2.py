#!/usr/bin/env python

import re

f = open('input.txt')

total = 0
for word in f:

	doubleLetter = re.compile(r'(..).*\1', re.IGNORECASE)
	hits = re.findall(doubleLetter, word)
	if not len(hits) :	
		continue

	repeatingLetter = re.compile(r'(.).\1', re.IGNORECASE)
	if re.findall(repeatingLetter, word) :
		total += 1

print total
