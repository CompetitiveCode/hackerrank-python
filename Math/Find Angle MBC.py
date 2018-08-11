#Answer to Find Angle MBC

import math
a = int(input())
b = int(input())
h = math.sqrt(a**2 + b**2)
h = h / 2.0
adj = b / 2.0
print (str(int(round(math.degrees(math.acos(adj/h))))) + "°")