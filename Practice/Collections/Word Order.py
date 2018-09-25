#Answer to Word Order

from collections import OrderedDict
n=int(input())
a=OrderedDict()
for i in range(n):
    j=input()
    if(j in a):
        a[j]+=1
    else:
        a[j]=1
print(len(a))
for i in a:
    print(a[i],end=" ")