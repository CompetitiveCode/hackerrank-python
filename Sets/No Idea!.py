#Answer to No Idea!

n = list(input().split())
m = list(input().split())
o = set(input().split())
p = set(input().split())
q = 0
for i in range(int(n[0])):
    if(m[i] in o):
        q+=1
    if(m[i] in p):
        q-=1
print(q)