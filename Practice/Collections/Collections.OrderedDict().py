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