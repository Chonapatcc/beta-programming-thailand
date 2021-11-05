n=int(input())

l=0
if n%2==0:
    l=n-1
else:
    l=n
lis=["*"]
for i in range(1,(n-2)+1,2):
    line="*"+"-"*i+"*"
    lis.append(line)
lis2=[]
for alis in lis:
    if len(alis)!=l:
        solve=(l-len(alis))/2
        solve=int(solve)
        alis="-"*solve+alis+"-"*solve
        lis2.append(alis)
    else:
        lis2.append(alis)

if n%2==0:
    for x in range(int(n/2)):
        print(lis2[x])
    for x in range(int(n/2)):
        num=int(n/2)-1
        print(lis2[num-x])
else:
    for x in range(int((n-1)/2)+1):
        print(lis2[x])
    for x in range(1,int((n-1)/2)+1):
        num=((n-1)/2)-x
        print(lis2[int(num)])
