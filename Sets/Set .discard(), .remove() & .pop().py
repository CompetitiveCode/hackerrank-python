#Answer to Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
m = int(input())
j = 0
for i in range(m):
    a = list(input().split())
    if(a[0] == 'pop'):
        s.pop()
    if(a[0] == 'discard'):            
        s.discard(int(a[1]))
    if(a[0] == 'remove'):
        if(int(a[1]) in s):
            s.remove(int(a[1]))
print(sum(s))