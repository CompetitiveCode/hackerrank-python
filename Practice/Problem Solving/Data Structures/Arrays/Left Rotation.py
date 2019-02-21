#Answer to Left Rotation - https://www.hackerrank.com/challenges/array-left-rotation/problem

n,d = input().split()
d = int(d)
a = list(map(int, input().rstrip().split()))
b = a[d:]+a[:d]
for i in b:
    print(i,end=" ")