Absolute Imports:
eg: from package1.subpackage2.subpackage3.subpackage4.module5 import function6

Relative Imports:
A single dot means that the module or package referenced is in the same directory as the current location
Two dots mean that it is in the parent directory of the current location—that is, the directory above
Three dots mean that it is in the grandparent directory, and so on

eg:
from .some_module import some_class
from ..some_package import some_function
from . import some_class
