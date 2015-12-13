#!/usr/bin/env python

import re

f = open('input.txt').read()

regex = re.compile(r'(-?\d+)')
m = re.findall(regex, f)
print sum(map(int, m))
