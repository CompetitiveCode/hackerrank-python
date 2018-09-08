#Answer to Set .intersection() Operation

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
print(len(a.intersection(b)))