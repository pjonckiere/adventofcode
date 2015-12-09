#!/usr/bin/env python

import hashlib

input = "ckczppom"

found = False
i = int(0)
while(not found):
	attempt = "%s%d" % (input, i)
	hash = hashlib.md5(attempt).hexdigest()
	# print hash
	if hash[:5] == "00000":
		print i
		found = True
	else :
		i += 1
