
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
