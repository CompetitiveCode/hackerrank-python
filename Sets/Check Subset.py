#Answer to Check Subset

n = int(input())
for i in range(n):
    m = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    z = True
    for i in a:
        if i not in b:
            z=False
    print(z)