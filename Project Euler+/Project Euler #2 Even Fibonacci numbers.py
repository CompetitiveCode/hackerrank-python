#Answer to Problem 2: Even Fibonacci numbers

for a in range(int(input())):
    n = int(input())
    if(n==1):
        print('0')
    elif(n==2):
        print('2')
    else:
        x=1
        y=2
        sum = y
        for b in range(n-2):
            z = x + y
            x = y
            y = z
            if z > n:
                break;
            if z%2 == 0:
                sum+=z
        print(sum)