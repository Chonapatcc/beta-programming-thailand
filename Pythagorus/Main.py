import math
a,b=input().split()
a=float(a)
b=float(b)
py=a**2+b**2
py=math.sqrt(py)
py="%.6f" %py
print(py)