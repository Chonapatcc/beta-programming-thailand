scorelis=[]


for i in range(5):
    scorelis.append((list(map(int, input().split()))))
lis=[]
for alis in scorelis:
    ans=0
    for s in alis:
        ans+=s
    lis.append(ans)
check=max(lis)
index=lis.index(check)
print(index+1,lis[index])
