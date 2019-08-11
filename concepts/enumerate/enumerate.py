#!/usr/bin/env python

a = ['a', 'b', 'c']
b=list(enumerate(a,0))
print(b)
for count,element in enumerate(a,2):
	print count,element
