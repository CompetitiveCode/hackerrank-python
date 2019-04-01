#Answer to Plus Minus - https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus,minus,zero = 0,0,0
    for i in arr:
        if i < 0:
            minus += 1
        elif i > 0:
            plus += 1
        else:
            zero += 1
    length = len(arr)
    print(plus/length,minus/length,zero/length,sep = "\n")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
