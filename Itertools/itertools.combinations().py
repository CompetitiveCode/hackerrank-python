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