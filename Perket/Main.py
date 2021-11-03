from math import *
from itertools import combinations


n = int(input())
p = []
ans = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(1,n+1):
    com = list(combinations(p, i))
    for lis in com:
        S=1
        B=0
        for a,b in lis:
            S*=a
            B+=b
            diff=abs(S-B)
            ans.append(diff)

print(min(ans))