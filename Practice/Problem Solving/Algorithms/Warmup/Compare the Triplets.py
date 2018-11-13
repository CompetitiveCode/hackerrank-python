#Answer to Compare the Triplets

def compareTriplets(a, b):
    alice=0
    bob=0
    for i in range(3):
        if(a[i]>b[i]):
            alice+=1
        elif(a[i]<b[i]):
            bob+=1
    return alice,bob

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
print(' '.join(map(str, compareTriplets(a, b))))