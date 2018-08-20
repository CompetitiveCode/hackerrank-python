#Answer to Day 3: Intro to Conditional Statements

n = int(input())
if n%2==1:
    print("Weird")
elif n%2==0:
    if n>5 and n<21:
        print("Weird")
    else:
        print("Not Weird")