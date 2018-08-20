#Answer to Day 5: Loops

n = int(input())
j=0
for i in range(10):
    j+=n
    print(str(n)+" x "+str((i+1))+" = "+str(j))