#!/usr/bin/env python

import re

input = 'cqjxjnds'
input = 'cqjxxyzz'

def increment_char(c):
    return chr(ord(c) + 1) if c != 'z' else 'a'

def increment_str(s):
    lpart = s.rstrip('z')
    num_replacements = len(s) - len(lpart)
    new_s = lpart[:-1] + increment_char(lpart[-1]) if lpart else 'a'
    new_s += 'a' * num_replacements
    return new_s

def is_valid(i):
	valid = False
	for c in range(0, len(i) - 2):
		if ord(i[c]) == ord(i[c+1]) - 1 and ord(i[c]) == ord(i[c+2]) - 2:
			valid = True
			break

	if 'i' in i or 'o' in i or 'l' in i:
		valid = False

	regex = re.compile(r'(\w)\1')
	m = re.findall(regex, i)
	if not len(m) >= 2:
		valid = False

	return valid		

valid = False
while not valid:
	input = increment_str(input)	
	valid = is_valid(input)

print input
