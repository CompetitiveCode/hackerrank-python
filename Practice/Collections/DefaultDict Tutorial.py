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
        
"""
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i

This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])
"""