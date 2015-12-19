#!/usr/bin/env python

import random

f = open('input.txt')

repl = {}
mol = False
molecule = ''
result = set()
for l in f:
    input = l.strip()
    if input == '':
        mol = True
    elif not mol:
        r = input.split(' => ')
        repl[r[1]] = r[0]
    else:
        molecule = input

keys = list(repl.keys())
random.shuffle(keys)

replacement = molecule
steps = 0
prevsteps = 0
while replacement <> 'e':
    for ro in keys:
        if ro in replacement:
            index = replacement.find(ro)
            replacement = replacement[:index] + repl[ro] + replacement[index + len(ro):]
            # print replacement
            steps += 1

    if steps == prevsteps:
        print "Got stuck. Retrying, got to %s" % replacement
        replacement = molecule
        steps = 0
        random.shuffle(keys)
    else:
        prevsteps = steps

print steps