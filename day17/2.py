#!/usr/bin/env python

import itertools
import sys

f = open('input.txt')

c = []
for line in f:
    c.append(line.strip())

count = 0
combo = []
for r in range(0, len(c) - 1):
    if len(combo) != 0:
        break

    for cc in itertools.combinations(c, r):

        t = int(0)
        for ccc in cc:
            t += int(ccc)

        if t == 150:
            combo.append(cc)
            count += 1

print count