#Answer to ginortS

a=input()
b,c,d,e=[],[],[],[]
for i in a:
    if(i.islower()):
        b.append(i)
    elif(i.isupper()):
        c.append(i)
    elif(i.isnumeric()):
        i=int(i)
        if(i%2!=0):
            d.append(i)
        else:
            e.append(i)
for i in sorted(b):
    print(i,end="")
for i in sorted(c):
    print(i,end="")
for i in sorted(d):
    print(i,end="")
for i in sorted(e):
    print(i,end="")