#!/usr/bin/env python

class A(object):
	def func1(self):
		print("func1 of A")
	def func2(self):
		print("func2 of A")
	def func3(self):
		print("func3 of A")
		
class B(object):
	def func1(self):
		print("func1 of B")
	def func2(self):
		print("func2 of B")
	def func3(self):
		print("func3 of B")

obj1 = A()
obj2 = B()

#inheritance with "CLASS METHODS"
for i in (obj1,obj2):
	i.func1()
	i.func2()
	i.func3()


