#|x1y2 + x2y3 + x3y1 − y1x2 − y2x3 − y3x1|/2

n=int(input())
lis=[]
for i in range(n):
    x,y=list(map(int,input().split(" ")))
    lis.append([x,y])
prob=[]

for l1 in range(1,n-1):
    for l2 in range(l1+1,n):
        for l3 in range(l2+1,n+1):
            if l1!=l2!=l3:
                prob.append([l1,l2,l3])
anslis=[]
for l1,l2,l3 in prob:              
    ans=(lis[l1-1][0]*lis[l2-1][1])+(lis[l2-1][0]*lis[l3-1][1])+(lis[l3-1][0]*lis[l1-1][1])-(lis[l1-1][1]*lis[l2-1][0])-(lis[l2-1][1]*lis[l3-1][0])-(lis[l3-1][1]*lis[l1-1][0])
    ans=abs(ans)/2
    anslis.append(ans)
anslis.sort()
print("{:.3f}".format(anslis[-1]))

