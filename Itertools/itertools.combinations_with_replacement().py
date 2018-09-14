#Answer to itertools.combinations_with_replacement()

from itertools import combinations_with_replacement
a = input().split()
for i in list(combinations_with_replacement(sorted(a[0]),int(a[1]))):
    for j in i:
        print(j,end="")
    print("")