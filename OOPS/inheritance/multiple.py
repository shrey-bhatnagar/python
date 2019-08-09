"""

class-A   class B
      |   |
     class c

"""

class A(object):
	def __init__(self):
		print("init of class A")

class B(object):
	def __init__(self):
		print("init of class B")

class C(A,B):
	def __init__(self):
		#super().__init__() ## python3 - this will work
		#super(B,self).__init__()
		A.__init__(self)
		B.__init__(self)
		print("init of class C")
obj1 = C()
