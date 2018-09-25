#Answer to itertools.permutations()

from itertools import permutations
a = list(input().split())
b = sorted(list(permutations(a[0],int(a[1]))))
for i in b:
    for j in range(int(a[1])):
        print(i[j],end="")
    print("")