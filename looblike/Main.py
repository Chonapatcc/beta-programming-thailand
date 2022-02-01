n=int(input())
lis=input().split(" ")
lis.sort()
lisnum=[]
lisal=[]
num=0
for i in range(n):
    if i==0:
        num+=1
        lisal.append(lis[i])
    else:
        if i==n-1:
            if lis[i]==lis[i-1]:
                num+=1
                lisnum.append(num)
            else:
                lisnum.append(num)
                num=1
                lisal.append(lis[i])
                lisnum.append(num)
        else:
            if lis[i]==lis[i-1]:
                num+=1
            else:
                lisnum.append(num)
                num=1
                lisal.append(lis[i])

            


check=0
for alisnum in lisnum:
    if alisnum>check:
        check=alisnum
    else:
        pass
toprint=[]
for last in range(len(lisnum)):
    if check == lisnum[last]:
        toprint.append(int(lisal[last]))
toprint.sort()
sprint=""
for aprint in toprint:
    sprint+=str(aprint)+" "
print(sprint.rstrip(" "))






