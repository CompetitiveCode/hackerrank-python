#Answer to Exceptions

for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)

"""
ZeroDivisionError 
This error is raised when the second argument of a division or modulo operation is zero.

>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero
ValueError 
This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'

#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e
"""