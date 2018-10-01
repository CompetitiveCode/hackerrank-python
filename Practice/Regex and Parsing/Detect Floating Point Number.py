#Answer to Detect Floating Point Number

import re
for i in range(int(input())):
    print(bool(re.match("^[+-]?[0-9]*\.[0-9]+$",input())))

"""
re
A regular expression (or RegEx) specifies a set of strings that matches it.

A regex is a sequence of characters that defines a search pattern, mainly for the use of string pattern matching.


The re.search() expression scans through a string looking for the first location where the regex pattern produces a match. 
It either returns a MatchObject instance or returns None if no position in the string matches the pattern.

Code

>>> import re
>>> print bool(re.search(r"ly","similarly"))
True

The re.match() expression only matches at the beginning of the string. 
It either returns a MatchObject instance or returns None if the string does not match the pattern. 

Code

>>> import re
>>> print bool(re.match(r"ly","similarly"))
False
>>> print bool(re.match(r"ly","ly should be in the beginning"))
True
"""

"""
Another way to solve this:

for i in range(int(input())):
    try:
        a=float(input())
        if(a==0):
            print(False)
        else:
            print(True)
    except ValueError:
        print(False)
"""