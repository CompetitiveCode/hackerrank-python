#Answer to Day 26: Nested Logic

n = list(map(int, input().split()))
m = list(map(int, input().split()))
fine = 0
if(n[2] > m[2]):
    fine = 10000
else:
    if(n[1] > m[1] and n[2] == m[2]):
        fine = 500 * (n[1] - m[1])
    else:
        if(n[0] > m[0] and n[1] == m[1] and n[2] == m[2]):
            fine = 15 * (n[0] - m[0])
print(fine)

#Another way shown below, either use the above code, or the below code. Not both together.

n = list(map(int, input().split()))
m = list(map(int, input().split()))
fine = 0
if(n[2] == m[2]):
    if(n[1] == m[1]):
        if(n[0] > m[0]):
            fine = 15 * (n[0] - m[0])
    elif(n[1] > m[1]):
        fine = 500 * (n[1] - m[1])
elif(n[2] > m[2]):
    fine = 10000
print(fine)