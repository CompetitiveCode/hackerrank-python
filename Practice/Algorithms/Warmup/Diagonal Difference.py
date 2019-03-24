#Answer to Diagonal Difference - https://www.hackerrank.com/challenges/diagonal-difference/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    val1 = 0
    val2 = 0
    for i in range(len(arr)):
        val1 += arr[i][i]
        val2 += arr[i][len(arr)-i-1]
    return max(val1,val2) - min(val1,val2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
