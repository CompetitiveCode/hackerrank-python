#Answer to Collections.OrderedDict()

from collections import OrderedDict
a=OrderedDict()
for i in range(int(input())):
    b=input().split()
    if(len(b) == 2):
        if(b[0] in a):
            a[b[0]] += int(b[-1])
        else:
            a[b[0]] = int(b[-1])            
    else:
        if(b[0]+" "+b[1] in a):
            a[b[0]+" "+b[1]] += int(b[-1])
        else:
            a[b[0]+" "+b[1]] = int(b[-1])            
for i in a:
    print(i,a[i])
    
"""
>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
"""