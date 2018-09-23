#Answer to DefaultDict Tutorial

from collections import defaultdict
n=list(map(int,input().split()))
a=defaultdict(list)
for i in range(n[0]):
    b=input()
    a[b].append(i+1)
for i in range(n[1]):
    b=input()
    if(b in a):
        for j in a[b]:
            print(j,end=" ")
        print("")
    else:
        print("-1")