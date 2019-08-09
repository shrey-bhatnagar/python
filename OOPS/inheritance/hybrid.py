"""

           ------class-A------     class Z
           |                 |     |
     class B                 class C
      |   |          
class D   class E     

"""

class A(object):
	def __init__(self):
		print("init of class A")

class Z(object):
	def __init__(self):
		print("init of class Z")

class B(A):
	def __init__(self):
		#super().__init__() ## python3 - this will work
		#super(B,self).__init__()
		A.__init__(self)
		print("init of class B")
class C(Z,A):
        def __init__(self):
                Z.__init__(self)
                A.__init__(self)
                print("init of class C")
class D(B):
        def __init__(self):
                B.__init__(self)
                print("init of class C")

class E(B):
	def __init__(self):
		B.__init__(self)
		print("init of class C")

obj1 = D()
obj2 = E()
