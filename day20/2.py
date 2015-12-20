#!/usr/bin/env python

goal = 36000000
limit = 1000000

houses = limit * [int(0)];

for elf in xrange(1, limit):
    if elf + 50 * elf < limit:
        end = elf + 50 * elf
    else:
        end = limit
        
    for house in xrange(elf, end, elf):
        houses[house] += elf * 11

    if elf % 10000 == 0:
        print "%s: %s" % (elf, max(houses))

    if houses[elf] > goal:
        print elf
        break
