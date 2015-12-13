#!/usr/bin/env python

import re
import json

f = open('input.txt').read()

def h(o):
	if 'red' in o.values():
		return {}	
	else :
		return o

j = json.loads(f, object_hook=h)

regex = re.compile(r'(-?\d+)')
m = re.findall(regex, str(j))
print sum(map(int, m))
