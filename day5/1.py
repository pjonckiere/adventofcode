#!/usr/bin/env python

import re

f = open('input.txt')

total = 0
for word in f:
	vowels = "aeiuoAEIOU"
	vowelCount = len([letter for letter in word if letter in vowels])
	if vowelCount < 3:
		continue

	doubleLetter = re.compile(r'.*(.)\1.*', re.IGNORECASE)
	if not doubleLetter.match(word):
		continue

	if word.find("ab") == -1 and word.find("cd") == -1 and word.find("pq") == -1 and word.find("xy") == -1 :
		total += 1

print total
