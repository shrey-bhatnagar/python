Advantages of Inheritance
--------------------------
1)Reduce code redundancy.
2)Provides code reusability.
3)Reduces source code size and improves code readability.
4)The code is easy to manage and divided into parent and child classes.
5)Supports code extensibility by overriding the base class functionality within child classes.

Disadvantages of Inheritance:
-------------------------------
1)In Inheritance base class and child class, both are tightly coupled. Hence If you change the code of parent class, it will affect all the child classes.
2)In a class hierarchy, many data members remain unused and the memory allocated to them is not utilized. Hence it affects the performance of your program if you have not implemented inheritance correctly.
-----------------------------------------------------------
Name   |Notation  |Behaviour
-----------------------------------------------------------
  name |Public    |Can be accessed from inside and outside
 _name |Protected |Like a public member, but they shouldn't be directly accessed from outside.
__name |Private   |Can't be seen and accessed from outside
-----------------------------------------------------------

Super function:
---------------
1) to use super function in python-2 use "object" 
==> class A(object): ..... 
class B(A):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        super(B,self).__init__(x,y)
2) if __init__ is redefined it has to be handled properly.(pyth-2 we need to call super(base class, self) in python-3 super() works)
class A(object):
    def __init__(self,x1,y1):
        self.x1=x1
        self.y2=y1
class B(A):
    def __init__(self,x2,y2):
        #super(B,self).__init__(x2,y2)
        #super().__init__(x2,y2) #===> python3
        A.__init__(self,x2,y2)
        self.x3=x2
        self.y4=y2
class C(B):
    def __init__(self,x3,y3):
        super(C, self).__init__(x3,y3) ## note here we call local class name in super with its self.
        #super().__init__(x3,y3) #===> python3
        #B.__init__(self,x3,y3)

