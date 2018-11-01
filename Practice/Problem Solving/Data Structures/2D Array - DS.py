#Answer to 2D Array - DS

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    high=-70 #It is initialised as -70 because the input values in the array can also be negative values upto -9
    sums=0
    for i in range(4):
        for j in range(4):
            for k in range(3):
                sums+=arr[i][k+j]
                sums+=arr[i+2][k+j]
            sums+=arr[i+1][j+1]
            if(high<=sums):
                high=sums
            print(sums)
            sums=0
    return high
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
