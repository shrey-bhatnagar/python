
# Python 3.4+
from abc import ABC, abstractmethod
class Abstract(ABC):
    @abstractmethod
    def foo(self):
        pass

# Python 3.0+
from abc import ABCMeta, abstractmethod
class Abstract(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

# Python 2
from abc import ABCMeta, abstractmethod
class Abstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def foo(self):
        pass


1) we can not instanciate an object of "abstract class"
2) mandatory to define a function for abstract class function in sub-class


Concrete Methods in Abstract Base Classes :
--------------------------------------------
Concrete classes contain only concrete (normal)methods, whereas abstract class contains both concrete methods as well as abstract methods.



Abstract Property:
====================
Since Python 3.3 a bug was fixed meaning the property() decorator is now correctly identified as abstract when applied to an abstract method.

Note: Order matters, you have to use @property before @abstractmethod

Python 3.3+: 
class C(ABC):
    @property
    @abstractmethod
    def my_abstract_property(self):
        ...

Python 2: 
class C(ABC):
    @abstractproperty
    def my_abstract_property(self):
        ...
