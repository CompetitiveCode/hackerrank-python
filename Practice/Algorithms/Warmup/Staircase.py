#Answer to Staircase - https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    m = 1
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(m):
            print("#",end="")
        m += 1
        print("")

if __name__ == '__main__':
    n = int(input())

    staircase(n)