#!/usr/bin/env python

def func(a,b,c=10,d=20):
	return a+b+c+d

func(1,2)     #result = 33
func(1,2,3)   #result = 26
func(1,2,3,4) #result = 10
