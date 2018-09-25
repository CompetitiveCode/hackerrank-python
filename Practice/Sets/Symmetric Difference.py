#Answer to Symmetric Difference

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
c = a&b #This gives the common element in both the sets
d = set()
d = sorted(d.union(a - c).union(b - c)) #Taking the union of both the sets with the difference from set c and sorting it
for i in d:
    print(i)