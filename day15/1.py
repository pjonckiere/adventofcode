#!/usr/bin/env python

import itertools
import re

ins = {}
f = open('input.txt')
regex = re.compile(r'(\w+)\: (\w+) (-?\d*), (\w+) (-?\d*), (\w+) (-?\d*), (\w+) (-?\d*), (\w+) (-?\d*)')
index = 0
for l in f:
	m = re.findall(regex, l)[0]
	ins[index] = {}
	ins[index][m[1]] = int(m[2]) # capacity
	ins[index][m[3]] = int(m[4]) # durability
	ins[index][m[5]] = int(m[6]) # flavor
	ins[index][m[7]] = int(m[8]) # texture
	ins[index][m[9]] = int(m[10]) # calories
	index += 1
								
best = 0
for a in range(0, 100):
	for b in range(0, 100 - a):
		for c in range(0, 100 - a - b):
			d = 100 - a - b - c
			cap = ins[0]['capacity'] * a + ins[1]['capacity'] * b + ins[2]['capacity'] * c + ins[3]['capacity'] * d
			dur = ins[0]['durability'] * a + ins[1]['durability'] * b + ins[2]['durability'] * c + ins[3]['durability'] * d
			fl = ins[0]['flavor'] * a + ins[1]['flavor'] * b + ins[2]['flavor'] * c + ins[3]['flavor'] * d
			tex = ins[0]['texture'] * a + ins[1]['texture'] * b + ins[2]['texture'] * c + ins[3]['texture'] * d
				
			if cap < 0 or dur < 0 or fl < 0 or tex < 0:
				v = 0
			else:
				v = cap * dur * fl * tex
	
			best = max(best, v)
	
print ins
print best
