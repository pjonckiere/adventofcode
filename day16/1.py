#!/usr/bin/env python

import itertools
import re

f = open('input.txt')

aunts = {}
for line in f:
	regex = re.compile(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')
	m = re.findall(regex, line)[0]
	aunts[m[0]] = {}
	aunts[m[0]][m[1]] = int(m[2])
	aunts[m[0]][m[3]] = int(m[4])
	aunts[m[0]][m[5]] = int(m[6])

for a in aunts:
	if 'akitas' in aunts[a] and aunts[a]['akitas'] <> 0:
		continue
	if 'perfumes' in aunts[a] and aunts[a]['perfumes'] <> 1:
		continue
	if 'vizslas' in aunts[a] and aunts[a]['vizslas'] <> 0:
		continue
	if 'children' in aunts[a] and aunts[a]['children'] <> 3:
		continue
	if 'cats' in aunts[a] and aunts[a]['cats'] <> 7:
		continue	
	if 'samoyeds' in aunts[a] and aunts[a]['samoyeds'] <> 2:
		continue	
	if 'pomeranians' in aunts[a] and aunts[a]['pomeranians'] <> 3:
		continue
	if 'goldfish' in aunts[a] and aunts[a]['goldfish'] <> 5:
		continue
	if 'trees' in aunts[a] and aunts[a]['trees'] <> 3:
		continue
	if 'cars' in aunts[a] and aunts[a]['cars'] <> 2:
		continue
	print a 
	break

#	children: 3
#	cats: 7
#	samoyeds: 2
#	pomeranians: 3
#	akitas: 0
#	vizslas: 0
#	goldfish: 5
#	trees: 3
#	cars: 2
#	perfumes: 1
