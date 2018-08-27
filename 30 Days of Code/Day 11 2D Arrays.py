#Answer to Day 11: 2D Arrays

if __name__ == '__main__':
    arr = []
    total, temp = -100,0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(len(arr)-2):
        k=i
        for j in range(len(arr[i])-2):
            l=j
            while(l<j+3):
                temp+=arr[k][l]
                temp+=arr[k+2][l]
                l+=1
            temp+=arr[k+1][j+1]
            if(temp>total):
                total=temp
            temp=0
    print(total)