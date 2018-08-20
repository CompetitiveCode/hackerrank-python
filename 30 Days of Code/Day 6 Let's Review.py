#Answer to Day 6: Let's Review

n=int(input())
for j in range(n):
    str=input()
    for i in range(len(str)):
        if(i%2==0):
            print(str[i],end="")
    print(" ",end="")
    for i in range(len(str)):
        if(i%2==1):
            print(str[i],end="")
    print("",end="\n")