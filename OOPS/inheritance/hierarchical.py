"""

           ------class-A------
           |                 |
     class B               class C
      |   |                 |   |
class D   class E     class F   class G

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
class C(A):
        def __init__(self):
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

class F(C):
        def __init__(self):
                C.__init__(self)
                print("init of class C")

class G(C):
        def __init__(self):
                C.__init__(self)
                print("init of class C")

obj1 = D()
obj2 = E()
obj3 = F()
obj4 = G()
