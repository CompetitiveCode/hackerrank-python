# Answer to Apple and Orange
# https://www.hackerrank.com/challenges/apple-and-orange/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple, orange = 0, 0
    for i in range(len(apples)):
        apples[i] += a
    for i in range(len(oranges)):
        oranges[i] += b
    for i in apples:
        if i >= s and i <= t:
            apple += 1
    for i in oranges:
        if i >= s and i <= t:
            orange += 1
    print(apple,orange,sep='\n')

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
