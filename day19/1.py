#!/usr/bin/env python

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
        if r[0] not in repl:
            repl[r[0]] = {}
        repl[r[0]][len(repl[r[0]])] = r[1]
    else:
        molecule = input

for option in repl:
    for ch in repl[option]:
        for j in range(len(molecule)):
            if molecule[j:j + len(option)] == option:
                tm = molecule[:j] + repl[option][ch] + molecule[j + len(option):]
                result.add(tm)
                # print tm

# print repl
# print molecule
# print '\n'
# print result
print len(result)