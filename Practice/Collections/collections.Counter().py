#Answer to collections.Counter()

from collections import Counter
n = input()
size = Counter(map(int, input().split()))
total = 0
for i in range(int(input())):
    a = input().split()
    if(size[int(a[0])]):
        total += int(a[1])
        size[int(a[0])] -= 1
print(total)

"""
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
"""