#Answer to Map and Lambda Function

cube = lambda x: x*x*x
def fibonacci(n):
    if n==0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        a=0
        b=1
        c=[0,1]
        for i in range(n-2):
            c.append(a+b)
            d=a
            a=b
            b+=d
        return c

"""
>> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
[4, 3, 3]

>> sum = lambda a, b, c: a + b + c
>> sum(1, 2, 3)
6
"""