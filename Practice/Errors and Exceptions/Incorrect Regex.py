#Answer to Incorrect Regex

import re
for i in range(int(input())):  
    try:
        print(bool(re.compile(input())))
    except:
        print('False')