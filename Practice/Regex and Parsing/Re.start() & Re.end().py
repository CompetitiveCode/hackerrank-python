#Answer to Re.start() & Re.end()

import re
a=input()
b=input()
i=0
if(b in a):
    while i < (len(a)-len(b)-1):
        m=re.search(b,a[i:])
        c=str(i+m.start())
        d=str(i+m.end()-1)
        print('('+c+', '+d+')')
        i+=m.start()+1
else:
    print('(-1, -1)')

"""
start() & end()

These expressions return the indices of the start and end of the substring matched by the group.

Code

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0

"""