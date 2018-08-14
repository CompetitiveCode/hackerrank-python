#Answer to Designer Door Mat

n=input().split(" ")
m=int(int(n[0])/2)
for i in range(m):
    print((".|."*(i+i+1)).center(int(n[1]),'-'))
print("WELCOME".center(int(n[1]),'-'))
i=m
while i>0:
    print((".|."*(i+i-1)).center(int(n[1]),'-'))
    i-=1