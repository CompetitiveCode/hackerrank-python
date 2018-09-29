#Answer to Athlete Sort

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(input())
k = int(input())
for row in sorted(arr, key=lambda row: int(row.split()[k])):
    print(row)