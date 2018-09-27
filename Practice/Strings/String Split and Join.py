#Answer to String Split and Join

def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

"""
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 
"""