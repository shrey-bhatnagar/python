"""

     class A
      | | |
class B | class C
      | | |
     class D

"""

class A(object):
	def __init__(self):
		print("init of class A")

class B(A):
	def __init__(self):
		A.__init__(self)
		print("init of class B")


class C(A):
	def __init__(self):
		A.__init__(self)
		print("init of class C")

class D(A,B,C):
	def __init__(self):
		#super().__init__() ## python3 - this will work
		#super(B,self).__init__()
		A.__init__(self)
		B.__init__(self)
		C.__init__(self)
		print("init of class D")
obj1 = C()
