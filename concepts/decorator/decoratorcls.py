#!/usr/bin/env python

class memoize():
	def __init__(self, f):
		self.f = f
		self.memo = {}

	def __call__(self, *args):
		if args not in self.memo:
			self.memo[args] = self.f(*args)
		return self.memo[args]

@memoize
def fib(n):
	if(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return fib(n-1)+fib(n-2)

#fib = memoize(fib)

if __name__ == '__main__':
	print(fib(int(raw_input("enter the number: "))))
