Class and Object:
 While the class is the blueprint, an instance is a copy of the class with actual values.


Encapsulation: < Information hiding or system complexity hiding >
 1) Encapsulation is a mechanism of binding the data member & member function into a single unit known as class.
 2) Encapsulation provides a way for abstraction.<restricting the access to some of the object’s components, this means internal implementation of object cant be seen from outside>

 eg: (class is kind of a container or capsule or a cell, which encapsulate the set of methods and attribute)


Abstraction: < Implementation hiding >
 1) Data abstraction is a mechanism to provide the essential features without describing the background details. Means provide the functions to access the hidden (private) data.


Data Encapsulation/Hiding: < data security >
 1) Data hiding is a mechanism to hide the internal structure of an object from rest of the program

 eg: private variable - "__val" ==> object._class.__val


Polymorphism: < many form's>
Polymorphism means one thing in many form. Basically polymorphism is capability of one object to behave in multiple ways.

 1) Static polymorphism(compile time) : It is achieved using function overloading and operator overloading.
 2) Dynamic polymorphism(runtime time) : It is achieved using method overriding means using virtual function.

   a)inbuilt <Static - function overloading>
   b)user defined function <Static - function overloading>
   c)class methods (for call on object tupple)
   d)Method Overriding
   e)Function and objects (pass object in function)


Inheritance:
A class can inherit attributes and behaviour (methods) from other classes, called super-classes. A class which inherits from super-classes is called a Sub-class. Super-classes are sometimes called ancestors as well. There exists a hierarchy relationship between classes.

a)single
b)multilevel
b)multiple
c)multipath
d)hirarical
e)hybrid


Constructor: < __init__() >
There is no real constructor in python,because a new instance is already constructed by the time __init__() is called.
this is the first function to be called in class.


Destructor: < __del__() >
There is no "real" destructor, but something similiar, i.e. the method __del__. It is called when the instance is about to be destroyed.
