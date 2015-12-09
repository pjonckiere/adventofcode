#!/usr/bin/env python

f = open('input.txt')
total = 0
for dimline in f.readlines():
	dim = dimline.split('x')
	dim.sort(key=int)
	l = int(dim[0])
	w = int(dim[1])
	h = int(dim[2])
	total += l + l + w + w + (l*w*h)

print total
