#Answer to Find the Runner-Up Score!
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    j=-100
    k=max(arr)
    for i in arr:
        if(i>j):
            if(i!=k):
                j=i
    print(j)