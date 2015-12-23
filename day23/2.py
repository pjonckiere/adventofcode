#!/usr/bin/env python

program = []
for l in open('input.txt'):
    program.append(l.strip())

a = 1
b = 0
index = 0
while index < len(program):
    instr = program[index][:3]
    offset = 1
    if instr == 'jio' and a == 1:
        offset = int(program[index][program[index].find('+') + 1:])
    elif instr == 'inc':
        reg = program[index][program[index].find(' ') + 1:]
        if reg == 'b':
            b += 1
        else:
            a += 1
        offset = 1
    elif instr == 'tpl':
        reg = program[index][program[index].find(' ') + 1:]
        a *= 3
        offset = 1
    elif instr == 'jmp':
        offset = int(program[index].split(' ')[1])
    elif instr == 'jie':
        if a % 2 == 0:
            offset = int(program[index][program[index].find('+') + 1:])
        else:
            offset = 1
    elif instr == 'hlf':
        a //= 2
        offset = 1
    index += offset

print b