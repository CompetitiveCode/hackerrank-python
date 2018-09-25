#Answer to Collections.namedtuple()

from collections import namedtuple
n = int(input())
a = namedtuple('a',input().split())
total = 0
for i in range(n):
    one, two, three, four = input().split()
    b = a(one, two, three, four)
    total += int(b.MARKS)
print('%.2f' %(total/n))