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