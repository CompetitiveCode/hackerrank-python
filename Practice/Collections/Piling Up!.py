#Answer to Piling Up!

for j in range(int(input())):
    l = int(input()) - 1
    lst = list(map(int, input().split()))
    i = 0
    while i < l and lst[i] >= lst[i+1]:
        i += 1
    while i < l and lst[i] <= lst[i+1]:
        i += 1
    print("Yes" if i == l else "No")