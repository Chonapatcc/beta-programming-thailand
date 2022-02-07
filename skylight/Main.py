import math
N,M=map(int,input().split())
L,K=map(int,input().split())
p=int(input())
num=0
for i in range(int(N)):
    price=list(map(int,input().split()))
    for y in price:
        num+=y
num+=L*K*p
ans=num/p
print(math.ceil(ans))
