#Answer to itertools.product()

from itertools import product
for i in list(product(list(map(int, input().split())), list(map(int, input().split())))):
    print(i,end=" ")