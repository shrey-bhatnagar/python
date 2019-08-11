
Declaring Docstrings: 
----------------------
The docstrings are declared using “””triple double quotes””” just below the class, method or function declaration. All functions should have a docstring.

Accessing Docstrings: 
----------------------
The docstrings can be accessed using the __doc__ method of the object or using the help function.

##################################################################


One-line Docstrings
----------------------
As the name suggests, one line docstrings fit in one line. They are used in obvious cases. The closing quotes are on the same line as the opening quotes. This looks better for one-liners.
For example:

def power(a, b): 
    """Returns arg1 raised to power arg2."""
    return a**b 
  
print power.__doc__ 
Output:

Returns arg1 raised to power arg2.



Multi-line Docstrings:
-----------------------
Multi-line docstrings consist of a summary line just like a one-line docstring, followed by a blank line, followed by a more elaborate description. The summary line may be on the same line as the opening quotes or on the next line.
The example below shows a multi-line docstring.

def my_function(arg1): 
    """ 
    Summary line. 
  
    Extended description of function. 
  
    Parameters: 
    arg1 (int): Description of arg1 
  
    Returns: 
    int: Description of return value 
  
    """
    return arg1 
  
print my_function.__doc__ 
