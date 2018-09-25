#Answer to Lists

if __name__ == '__main__':
    N = int(input())
    A = []
    j = []
    k = []
    l=-1
    for i in range(N):
        A.append(input().split())
    for i in range(N):
        j=A[i]
        if(j[0]=="insert"):
            k.insert(int(j[1]),int(j[2]))
        if(j[0]=="print"):
            print(k)
        if(j[0]=="remove"):
            l=k.index(int(j[1]))
            k.pop(l)
        if(j[0]=="pop"):
            k.pop()
        if(j[0]=="append"):
            k.append(int(j[1]))
        if(j[0]=="sort"):
            k.sort()
        if(j[0]=="reverse"):
            k.reverse()