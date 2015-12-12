#!/usr/bin/env python

import re

f = open('input.txt')

signals = {}
for line in f:
	op = line.partition(' -> ')
	signals[op[2].rstrip()] = op[0]

# print signals

found = False
cycle = 0
while not found:
	for key, signal in signals.iteritems():
		if isinstance(signal, int) or signal.isdigit():
			signals[key] = int(signal)
			# print "%s is %d" % (key, signals[key])
		else:
			parts = signal.split()
			if len(parts) == 1:
				# always direct assignment
				dependency = parts[0]
				if isinstance(signals[dependency], int):
					signals[key] = signals[dependency]
			elif len(parts) == 2:
				# always NOT
				operation = parts[0]
				dependency = parts[1]
				if isinstance(signals[dependency], int):
					#signals[key] = ~int(signals[dependency])
					signals[key] = 65535 - int(signals[dependency])
					
			else:
				dependency1 = parts[0]
				operation = parts[1]
				dependency2 = parts[2]
				if dependency1.isdigit():
					# always AND
					if isinstance(signals[dependency2], int):
						signals[key] = int(dependency1) & int(signals[dependency2])
				elif dependency2.isdigit():
					# always RSHIFT or LSHIFT
					if isinstance(signals[dependency1], int):
						if operation == 'RSHIFT':
							signals[key] = int(signals[dependency1]) >> int(dependency2)
						if operation == 'LSHIFT':
							signals[key] = int(signals[dependency1]) << int(dependency2)
				else:
					# always AND or OR
					if isinstance(signals[dependency1], int) and isinstance(signals[dependency2], int):
						if operation == 'AND':
							signals[key] = int(signals[dependency1]) & int(signals[dependency2])
						if operation == 'OR':
							signals[key] = int(signals[dependency1]) | int(signals[dependency2])

	# print "\n"
	cycle += 1
	if isinstance(signals['a'], int):
		found = True

# for key, signal in signals.iteritems():
# 	print "%s is %s" % (key, signal)
# print cycle
print signals['a']
