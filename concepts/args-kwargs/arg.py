#!/usr/bin/env python

def func(*args):
	for arg in args:
		print(arg)

l = [11,22,33,44,55]
func(1,2,3,4,5)
func('a','b','c')
func(l,66,88,99)
