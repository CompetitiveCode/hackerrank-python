#Answer to String Validators

if __name__ == '__main__':
    s = input()
    a = b = c = d = e = False
    for i in s:
        if(i.isalnum()):
            a=True
        if(i.isalpha()):
            b=True
        if(i.isdigit()):
            c=True
        if(i.islower()):
            d=True
        if(i.isupper()):
            e=True
    print(a,b,c,d,e,sep="\n")
    
"""
str.isalnum() 
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
str.isalpha() 
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
str.isdigit() 
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
str.islower() 
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
str.isupper() 
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
"""