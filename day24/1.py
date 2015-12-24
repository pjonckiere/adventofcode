#!/usr/bin/env python

import itertools

weights = []
for l in open('input.txt'):
    weights.append(int(l.strip()))

total_weight = sum(weights)

results = []
for i in range(25):
    for combo in (x for x in itertools.combinations(weights, i) if sum(x) == total_weight / 3):
        results.append(combo)
    if len(results) > 0:
        break

min_entanglement = 10000000000000
for result in results:
    entanglement = 1
    for r in result:
        entanglement *= r
    min_entanglement = min(entanglement, min_entanglement)

print min_entanglement
