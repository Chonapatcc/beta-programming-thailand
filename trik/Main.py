n=input()
lis=[1,0,0]
for i in n:
    if i=="A":
        if lis[0]==1:
            lis[0],lis[1]=0,1
        elif lis[1]==1:
            lis[0],lis[1]=1,0
    elif i=="B":
        if lis[1]==1:
            lis[1],lis[2]=0,1
        elif lis[2]==1:
            lis[1],lis[2]=1,0
    else:
        if lis[2]==1:
            lis[0],lis[2]=1,0
        elif lis[0]==1:
            lis[0],lis[2]=0,1
for y in range(len(lis)):
    if lis[y]==1:
        print(y+1)