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
