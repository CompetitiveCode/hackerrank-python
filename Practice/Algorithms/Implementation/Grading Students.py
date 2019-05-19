# Answer to Grading Students
# https://www.hackerrank.com/challenges/grading/problem


#!/bin/python3

import os
import sys

# Complete the gradingStudents function below.
def gradingStudents(grades):
    grade = []
    for i in grades:
        if i < 38:
            grade.append(i)
        else:
            temp = i
            for j in range(i,i+3):
                if j%5 == 0:
                    temp = j
            grade.append(temp)
    return grade
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
