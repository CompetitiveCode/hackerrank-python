#Answer to Day 20: Sorting

import sys
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
num = 0
for i in range(n):
    numberOfSwaps = 0
    for j in range(n - 1):
        if (a[j] > a[j + 1]):
            t = a[j]
            a[j] = a[j + 1]
            a[j + 1] = t
            numberOfSwaps += 1
            num+=1
    if (numberOfSwaps == 0):
        break;
print("Array is sorted in "+str(num)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[n - 1]))