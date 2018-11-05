#Answer to Simple Array Sum

def simpleArraySum(ar):
    j=0
    for i in ar:
        j+=i
    return j
ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
result = simpleArraySum(ar)
print(result)