#!/usr/bin/env python

class A(object):
	def func1(self):
		print("func1 in A")
	def func2(self):
		print("func2 in A")

class B(A):
	def func1(self):
		print("func1 in B")
class C(A):
	def func2(self):
		print("func2 in C")

obj1 = A()
obj2 = B()
obj3 = C()

obj1.func1()
obj2.func1()
obj3.func1()


obj1.func2()
obj2.func2()
obj3.func2()
