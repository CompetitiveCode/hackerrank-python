#Answer to Validating and Parsing Email Addresses

import email.utils
import re
for i in range(int(input())):
    b=input()
    a=email.utils.parseaddr(b)
    if bool(re.match(r'^[A-Za-z]{1}(\w|_|-|\.)*@[A-Za-z]+\.[A-Za-z]{1,3}$',a[1])):
        print(b)
        
"""
Code:

import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))

produces this output:

('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>
"""