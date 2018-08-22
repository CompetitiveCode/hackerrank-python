#Answer to Day 8: Dictionaries and Maps

n=int(input())
d={}
for i in range(n):
    arr = list(input().rstrip().split())
    d[arr[0]]=arr[1]
a=input()
while(a!=None):
    if(a in d):
        print(a+"="+d[a])
    else:
        print("Not found")
    a=None
    a=input()
    
    #Ignore the last error, as that won't affect the answer. This is because, there is no way we can find the no. of query to be made.