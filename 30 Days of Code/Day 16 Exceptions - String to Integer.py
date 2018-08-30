#Answer to Day 16: Exceptions - String to Integer

import sys
S = input().strip()
try: 
    print (int(S))
except ValueError: 
    print ("Bad String")
#else:
#    print (int(S))
#The above will result in the compiler to think that we are not including exception handler, so the above method.