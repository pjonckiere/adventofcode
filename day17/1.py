#!/usr/bin/env python

import itertools

f = open('input.txt')

c = []
for line in f:
    c.append(line.strip())

count = 0
for r in range(3, len(c) - 1):
    for cc in itertools.combinations(c, r):
        t = int(0)
        for ccc in cc:
            t += int(ccc)

        if t == 150:
            count += 1

print count