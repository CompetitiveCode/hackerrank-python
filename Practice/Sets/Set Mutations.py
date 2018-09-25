#Answer to Set Mutations

n = int(input())
a = set(map(int, input().split()))
for i in range(int(input())):
    b = input().split()
    if(b[0] == 'intersection_update'):
        a.intersection_update(set(map(int, input().split())))
    if(b[0] == 'update'):
        a.update(set(map(int, input().split())))
    if(b[0] == 'symmetric_difference_update'):
        a.symmetric_difference_update(set(map(int, input().split())))
    if(b[0] == 'difference_update'):
        a.difference_update(set(map(int, input().split())))
print(sum(a))