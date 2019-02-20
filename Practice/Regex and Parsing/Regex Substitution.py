#Answer to Regex Substitution - https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

for i in range(int(input())):
    value = input()
    value = re.sub(r" &&(?= )"," and",value)
    value = re.sub(r" \|\|(?= )"," or",value)
    print(value)