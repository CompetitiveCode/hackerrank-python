#Answer to Validating phone numbers

import re
for i in range(int(input())):
    print('YES' if bool(re.match("^[789][0123456789]{9}$",input())) else 'NO')