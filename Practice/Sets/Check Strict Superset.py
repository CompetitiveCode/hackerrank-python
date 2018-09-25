#Answer to Check Strict Superset

a, c, z = set(map(int, input().split())), set(), 0
for i in range(int(input())):
    c.update(set(map(int, input().split())))
for i in c:
    if(i not in a):
        z = 1
print(False if z == 1 else True)