"""

class-A
  |
class B

"""

class A(object):
	def __init__(self):
		print("init of class A")

class B(A):
	def __init__(self):
		#super().__init__() ## python3 - this will work
		#super(B,self).__init__()
		A.__init__(self)
		print("init of class B")

#obj1 = A()
obj2 = B()
