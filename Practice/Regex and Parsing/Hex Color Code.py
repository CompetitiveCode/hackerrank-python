#Answer to Hex Color Code

import re
for i in range(int(input())):
    m = re.findall(r'#[0-9a-fA-F]{3,6}', input()[1:]) #input()[1:] to avoid the selectors
    if len(m):
        print(*m, sep = '\n')