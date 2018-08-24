#Answer to Day 10: Binary Numbers

n = int(input())
r, s, t=0, 0, 0
while n>0:
    if(n%2==1):
        s=1
    else:
        s=0
    if(s==1 and n%2==1):
        r+=n%2
    if(s==0 or n==1):
        if(t<r):
            t=r
        r=0
    n//=2
print(t)