import math
x,y=map(int,input().split())


if x==0 or y==0 or (x==0 and y==0):
    print(0)
else:
    times=math.ceil(y/x)
    if x>y:
        print(2)
    else:
        print(times)