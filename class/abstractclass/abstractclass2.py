#!/usr/bin/env python
"""
* we cant instantiate an instance of abstract class
* we are suppose to implement the abstract-func() in sub-class()

"""
from abc import ABCMeta, abstractmethod

class A():
	__metaclass__ = ABCMeta

	@abstractmethod
	def do_something(self):
		pass

class B(A):
        def __init__(self,val):
                self.val=val
                #super().__init__()
                #super(A,self).__init__()
                A.__init__(val)

        def do_something(self):
		print("the value is %d"%(self.val))
                pass

obj1 = B(10)
obj1.do_something()
