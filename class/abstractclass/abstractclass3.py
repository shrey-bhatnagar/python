#!/usr/bin/env python3
"""
* we cant instantiate an instance of abstract class
* we are suppose to implement the abstract-func() in sub-class()

"""
from abc import ABC, abstractmethod

class A(ABC):
	def __init__(self,val):
		self.val=val
		super().__init__()
		#super(A,self).__init__()
		#ABC.__init__()

	@abstractmethod
	def do_something(self):
		pass

class B(A):
	def __init__(self,val):
		self.val=val
		super().__init__(val)
		#super(A,self).__init__()
		#ABC.__init__()

	def do_something(self):
		print("the value is {}".format(self.val))
		pass

#obj2 = A(10)
"""
TypeError: Can't instantiate abstract class A with abstract methods do_something
"""
obj1 = B(10)
obj1.do_something()
