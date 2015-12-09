#!/usr/bin/env python

f = open('input.txt')
total = 0
for dimline in f.readlines():
	dim = dimline.split('x')
	l = int(dim[0])
	w = int(dim[1])
	h = int(dim[2])
	extra = min(l*w, w*h, h*l)
	total += 2*l*w + 2*w*h + 2*h*l + extra

print total
