#Answer to Collections.deque()

from collections import deque
d = deque()
for i in range(int(input())):
    a=input().split()
    if(a[0] == "append"):
        d.append(a[1])
    elif(a[0] == "appendleft"):
        d.appendleft(a[1])
    elif(a[0] == "pop"):
        d.pop()
    elif(a[0] == "popleft"):
        d.popleft()
    elif(a[0] == "clear"):
        d.clear()
    elif(a[0] == "extend"):
        d.extend(a[1])
    elif(a[0] == "extendleft"):
        d.extendleft(a[1])
    elif(a[0] == "count"):
        d.count(a[1])
    elif(a[0] == "remove"):
        d.remove(a[1])
    elif(a[0] == "reverse"):
        d.reverse()
    elif(a[0] == "rotate"):
        d.rotate(a[1])
for i in d:
    print(i,end=" ")
    
"""
>>> from collections import deque
>>> d = deque()
>>> d.append(1)
>>> print d
deque([1])
>>> d.appendleft(2)
>>> print d
deque([2, 1])
>>> d.clear()
>>> print d
deque([])
>>> d.extend('1')
>>> print d
deque(['1'])
>>> d.extendleft('234')
>>> print d
deque(['4', '3', '2', '1'])
>>> d.count('1')
1
>>> d.pop()
'1'
>>> print d
deque(['4', '3', '2'])
>>> d.popleft()
'4'
>>> print d
deque(['3', '2'])
>>> d.extend('7896')
>>> print d
deque(['3', '2', '7', '8', '9', '6'])
>>> d.remove('2')
>>> print d
deque(['3', '7', '8', '9', '6'])
>>> d.reverse()
>>> print d
deque(['6', '9', '8', '7', '3'])
>>> d.rotate(3)
>>> print d
deque(['8', '7', '3', '6', '9'])
"""