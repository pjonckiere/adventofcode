#!/usr/bin/env python

f = open('input.txt')

steps = 100
s = 100
g = [[0] * s for i in range(s)]
r = 0
for l in f:
    l = l.strip();
    for i, c in enumerate(l):
        g[r][i] = c
    r += 1


def findvalue(x, y):
    if x >= 0 and y >= 0 and x < s and y < s and g[x][y] == '#':
        return 1
    else:
        return 0


def getgrid():
    global g
    return g


def setgrid(gr):
    global g
    g = list(gr)


def printgrid():
    print '\n'
    global g
    for d in g:
        print d

# printgrid()
for step in range(steps):
    tg = [[0] * s for i in range(s)]
    for j, gg in enumerate(getgrid()):
        for k, ggg in enumerate(gg):
            value = 0
            if ggg == '#':
                value = 1

            value += findvalue(j - 1, k - 1)
            value += findvalue(j - 1, k)
            value += findvalue(j - 1, k + 1)
            value += findvalue(j, k - 1)
            value += findvalue(j, k + 1)
            value += findvalue(j + 1, k - 1)
            value += findvalue(j + 1, k)
            value += findvalue(j + 1, k + 1)

            if ggg == '#' and (value == 3 or value == 4):
                # print j
                # print k
                # print 'on0'
                tg[j][k] = '#'
            elif ggg == '.' and value == 3:
                # print j
                # print k
                # print 'on1'
                tg[j][k] = '#'
            else:
                # print j
                # print k
                # print 'off'
                tg[j][k] = '.'
    setgrid(tg)

printgrid()
print '\n'
print sum(p.count('#') for p in g)