#Answer to itertools.combinations()

from itertools import combinations
a = input().split()
a[0] = sorted(a[0])
for i in range(1,int(a[1])+1):
    b = list(combinations(a[0],i))
    for j in b:
        for k in range(i):
            print(j[k],end="")
        print("")
        
"""
>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
"""